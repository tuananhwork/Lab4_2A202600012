import sys
from agent import graph

test_cases = [
    {
        "name": "Test 1 — Direct Answer (Không cần tool)",
        "input": "Xin chào! Tôi đang muốn đi du lịch nhưng chưa biết đi đâu.",
        "expected": "Agent chào hỏi, hỏi thêm về sở thích/ngân sách/thời gian. Không gọi tool nào."
    },
    {
        "name": "Test 2 — Single Tool Call",
        "input": "Tìm giúp tôi chuyến bay từ Hà Nội đi Đà Nẵng",
        "expected": 'Gọi search_flights("Hà Nội", "Đà Nẵng"), liệt kê 4 chuyến bay.'
    },
    {
        "name": "Test 3 — Multi-Step Tool Chaining",
        "input": "Tôi ở Hà Nội, muốn đi Phú Quốc 2 đêm, budget 5 triệu. Tư vấn giúp!",
        "expected": "Agent chuỗi nhiều bước: search_flights, search_hotels, calculate_budget."
    },
    {
        "name": "Test 4 — Missing Info / Clarification",
        "input": "Tôi muốn đặt khách sạn",
        "expected": "Agent hỏi lại: thành phố nào? bao nhiêu đêm? ngân sách bao nhiêu? Không gọi tool vội."
    },
    {
        "name": "Test 5 — Guardrail / Refusal",
        "input": "Giải giúp tôi bài tập lập trình Python về linked list",
        "expected": "Từ chối lịch sự, nói rằng chỉ hỗ trợ về du lịch."
    }
]

class DualWriter:
    """Class hỗ trợ in ra màn hình console và đồng thời ghi vào file"""
    def __init__(self, file, stdout):
        self.file = file
        self.stdout = stdout

    def write(self, text):
        self.file.write(text)
        self.stdout.write(text)

    def flush(self):
        self.file.flush()
        self.stdout.flush()

def run_tests():
    print("="*60)
    print("BẮT ĐẦU CHẠY CÁC TEST CASES - PHẦN 4")
    print("="*60)
    
    with open("test_results.md", "w", encoding="utf-8") as f:
        f.write("# BÁO CÁO KẾT QUẢ TEST CASE (PHẦN 4)\n\n")
        
        for i, test in enumerate(test_cases, 1):
            # Tạo lập thread mới cho từng bài test để context độc lập, tránh nhiễu
            thread_id = f"test_thread_{i}"
            config = {"configurable": {"thread_id": thread_id}}
            
            header = f"\n## {test['name']}\n**User**: `{test['input']}`\n**Kỳ vọng**: {test['expected']}\n\n**Log & Output**:\n```text\n"
            print(f"\n[Running] {test['name']} ...")
            f.write(header)
            
            original_stdout = sys.stdout
            sys.stdout = DualWriter(f, original_stdout)
            
            try:
                print("TravelBuddy đang suy nghĩ...")
                result = graph.invoke({"messages": [("human", test['input'])]}, config=config)
                final = result["messages"][-1].content
                print(f"\nTravelBuddy:\n{final}\n")
            except Exception as e:
                print(f"[!] Lỗi khi chạy test này: {str(e)}")
            finally:
                sys.stdout = original_stdout
                
            f.write("```\n\n---\n\n")
            print("-" * 60)
            
    print("\n[+] ĐÃ HOÀN THÀNH TẤT CẢ TEST CASES!")
    print("[+] Toàn bộ log đã được tự động lưu vào file 'test_results.md' để chuẩn bị nộp bài.")

if __name__ == "__main__":
    run_tests()
