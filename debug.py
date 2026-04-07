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
    },
    {
        "name": "Test 6 — Reverse Route & Non-existent City",
        "input": "Mình muốn bay từ Đà Nẵng sang Hà Nội, tiện thể xem có chuyến nào đến Cà Mau luôn không?",
        "expected": "Với Đà Nẵng - Hà Nội: Tự tra ngược chiều. Với Cà Mau: Báo không có dữ liệu."
    },
    {
        "name": "Test 7 — Impossible Constraints (Budget Overflow)",
        "input": "Tôi có đúng 1 triệu rưỡi. Muốn đi từ Hồ Chí Minh đến Đà Nẵng bằng Vietnam Airlines và ở khách sạn Mường Thanh.",
        "expected": "Gọi flights và hotels, nhận ra cấu hình vượt xa 1.5tr, báo cáo cháy túi và đề xuất đổi hãng/khách sạn."
    },
    {
        "name": "Test 8 — Implicit City Inference & Math",
        "input": "Tôi ở Hà Nội, định trốn việc đi nghỉ dưỡng ở Vinpearl Resort 3 đêm cùng vợ. Ngân sách gộp cả đi cả về là 15 triệu.",
        "expected": "Tự hiểu Vinpearl ở Phú Quốc. Tính tiền vé máy bay x2 (người), tiền phòng x3, gọi calculate_budget trừ vào 15 triệu."
    },
    {
        "name": "Test 9 — Distracted / Rambling Prompt",
        "input": "Nóng quá làm tôi lười code. Đi từ Hồ Chí Minh ra Phú Quốc ngân sách 3 triệu có đủ cho 1 đêm không? Sếp đang giục task mà chán quá.",
        "expected": "Lọc bỏ rác (code, sếp). Gọi flights, hotels (1 đêm) để chứng minh 3 triệu là đủ."
    },
    {
        "name": "Test 10 — Broad Comparison Search",
        "input": "Tôi ở Hà Nội, vứt tôi đến thẳng Đà Nẵng hoặc Phú Quốc đều được, kiểm tra xem vé máy bay chỗ nào rẻ hơn thì đi.",
        "expected": "Tự động gọi search_flights 2 lần cho 2 tuyến, so sánh giá rẻ nhất (VietJet đi ĐN 890k) để rủ rê người dùng."
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
            
            header = f"\n## {test['name']}\n**User**: `{test['input']}`\n\n**Kỳ vọng**: {test['expected']}\n\n**Log & Output**:\n```text\n"
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
