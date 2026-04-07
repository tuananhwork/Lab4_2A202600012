from pypdf.generic import Destination
from langchain_core.tools import tool

FLIGHTS_DB = {
    ("Hà Nội", "Đà Nẵng"): [
        {"airline": "Vietnam Airlines", "departure": "06:00", "arrival": "07:20", "price": 1_450_000, "class": "economy"},
        {"airline": "Vietnam Airlines", "departure": "14:00", "arrival": "15:20", "price": 2_800_000, "class": "business"},
        {"airline": "VietJet Air", "departure": "08:30", "arrival": "09:50", "price": 890_000, "class": "economy"},
        {"airline": "Bamboo Airways", "departure": "11:00", "arrival": "12:20", "price": 1_200_000, "class": "economy"},
    ],
    ("Hà Nội", "Phú Quốc"): [
        {"airline": "Vietnam Airlines", "departure": "07:00", "arrival": "09:15", "price": 2_100_000, "class": "economy"},
        {"airline": "VietJet Air", "departure": "10:00", "arrival": "12:15", "price": 1_350_000, "class": "economy"},
        {"airline": "VietJet Air", "departure": "16:00", "arrival": "18:15", "price": 1_100_000, "class": "economy"},
    ],
    ("Hà Nội", "Hồ Chí Minh"): [
        {"airline": "Vietnam Airlines", "departure": "06:00", "arrival": "08:10", "price": 1_600_000, "class": "economy"},
        {"airline": "VietJet Air", "departure": "07:30", "arrival": "09:40", "price": 950_000, "class": "economy"},
        {"airline": "Bamboo Airways", "departure": "12:00", "arrival": "14:10", "price": 1_300_000, "class": "economy"},
        {"airline": "Vietnam Airlines", "departure": "18:00", "arrival": "20:10", "price": 3_200_000, "class": "business"},
    ],
    ("Hồ Chí Minh", "Đà Nẵng"): [
        {"airline": "Vietnam Airlines", "departure": "09:00", "arrival": "10:20", "price": 1_300_000, "class": "economy"},
        {"airline": "VietJet Air", "departure": "13:00", "arrival": "14:20", "price": 780_000, "class": "economy"},
    ],
    ("Hồ Chí Minh", "Phú Quốc"): [
        {"airline": "Vietnam Airlines", "departure": "08:00", "arrival": "09:00", "price": 1_100_000, "class": "economy"},
        {"airline": "VietJet Air", "departure": "15:00", "arrival": "16:00", "price": 650_000, "class": "economy"},
    ],
}

HOTELS_DB = {
    "Đà Nẵng": [
        {"name": "Mường Thanh Luxury", "stars": 5, "price_per_night": 1_800_000, "area": "Mỹ Khê", "rating": 4.5},
        {"name": "Sala Danang Beach", "stars": 4, "price_per_night": 1_200_000, "area": "Mỹ Khê", "rating": 4.1},
        {"name": "Memory Hostel", "stars": 2, "price_per_night": 250_000, "area": "Hải Châu", "rating": 4.6},
        {"name": "Christina's Homestay", "stars": 3, "price_per_night": 350_000, "area": "An Thượng", "rating": 4.3},
        {"name": "Fivitel Danang", "stars": 4, "price_per_night": 650_000, "area": "Sơn Trà", "rating": 4.7},
    ],
    "Phú Quốc": [
        {"name": "Vinpearl Resort", "stars": 5, "price_per_night": 3_500_000, "area": "Bãi Dài", "rating": 4.4},
        {"name": "Sol by Meliá", "stars": 4, "price_per_night": 1_500_000, "area": "Bãi Trường", "rating": 4.2},
        {"name": "Lahana Resort", "stars": 3, "price_per_night": 800_000, "area": "Dương Đông", "rating": 4.0},
        {"name": "9Station Hostel", "stars": 2, "price_per_night": 200_000, "area": "Dương Đông", "rating": 4.5},
    ],
    "Hồ Chí Minh": [
        {"name": "Rex Hotel", "stars": 5, "price_per_night": 2_800_000, "area": "Quận 1", "rating": 4.3},
        {"name": "Liberty Central", "stars": 4, "price_per_night": 1_400_000, "area": "Quận 1", "rating": 4.1},
        {"name": "Cochin Zen Hotel", "stars": 3, "price_per_night": 550_000, "area": "Quận 3", "rating": 4.4},
        {"name": "The Common Room", "stars": 2, "price_per_night": 180_000, "area": "Quận 1", "rating": 4.6},
    ],
}

@tool
def search_flights(origin: str, destination: str) -> str:
    """
    Tìm kiếm các chuyến bay giữa hai thành phố.
    Tham số:
    - origin: thành phố khởi hành (VD: 'Hà Nội', 'Hồ Chí Minh')
    - destination: thành phố đến (VD: 'Đà Nẵng', 'Phú Quốc')
    Trả về danh sách chuyến bay với hãng, giờ bay, giá vé.
    Nếu không tìm thấy tuyến bay, trả về thông báo không có chuyến.
    """
    # Cố gắng tra cứu chiều đi
    flights = FLIGHTS_DB.get((origin, destination))
    is_reverse = False
    
    # Nếu không có chiều đi, thử tra ngược
    if not flights:
        flights = FLIGHTS_DB.get((destination, origin))
        is_reverse = True
        
    # Nếu cả chiều đi và về đều không có
    if not flights:
        return f"Không tìm thấy chuyến bay từ {origin} đến {destination}."
        
    # Format kết quả
    if is_reverse:
        result = [f"Không có chuyến bay từ {origin} đến {destination}. Dưới đây là chuyến khứ hồi ngược lại ({destination} - {origin}):"]
    else:
        result = [f"Danh sách chuyến bay từ {origin} đến {destination}:"]
        
    for f in flights:
        price_formatted = f"{f['price']:,}".replace(",", ".") + "đ"
        result.append(f"- {f['airline']} | {f['departure']} - {f['arrival']} | Giá: {price_formatted} | hạng {f['class']}")
        
    return "\n".join(result)

@tool
def search_hotels(city: str, max_price_per_night: int = 99999999) -> str:
    """
    Tìm kiếm khách sạn tại một thành phố, có thể lọc theo giá tối đa mỗi đêm.
    Tham số:
    - city: tên thành phố (VD: 'Đà Nẵng', 'Phú Quốc', 'Hồ Chí Minh')
    - max_price_per_night: giá tối đa mỗi đêm (VNĐ), mặc định không giới hạn
    Trả về danh sách khách sạn phù hợp với tên, số sao, giá, khu vực, rating.
    """
    hotels = HOTELS_DB.get(city)
    if not hotels:
        return f"Không có dữ liệu khách sạn cho thành phố {city}."
        
    filtered_hotels = [h for h in hotels if h["price_per_night"] <= max_price_per_night]
    
    if not filtered_hotels:
        max_price_str = f"{max_price_per_night:,}".replace(",", ".") + "đ"
        return f"Không tìm thấy khách sạn tại {city} với giá dưới {max_price_str}/đêm. Hãy thử tăng ngân sách."
        
    filtered_hotels.sort(key=lambda x: x["rating"], reverse=True)
    
    result = [f"Danh sách khách sạn tại {city}:"]
    for h in filtered_hotels:
        price_str = f"{h['price_per_night']:,}".replace(",", ".") + "đ"
        result.append(f"- {h['name']} | {h['stars']} sao | Khu vực: {h['area']} | Rating: {h['rating']} | Giá: {price_str}/đêm")
        
    return "\n".join(result)

@tool
def calculate_budget(total_budget: int, expenses: str) -> str:
    """
    Tính toán ngân sách còn lại sau khi trừ các khoản chi phí.
    Tham số:
    - total_budget: tổng ngân sách ban đầu (VNĐ)
    - expenses: chuỗi mô tả các khoản chi, mỗi khoản cách nhau bởi dấu phẩy,
      định dạng 'tên_khoản:số_tiền' (VD: 'vé_máy_bay:890000,khách_sạn:650000')
    Trả về bảng chi tiết các khoản chi và số tiền còn lại.
    Nếu vượt ngân sách, cảnh báo rõ ràng số tiền thiếu.
    """
    try:
        expense_dict = {}
        if expenses.strip():
            for item in expenses.split(','):
                name, str_price = item.split(':')
                expense_dict[name.strip()] = int(str_price.strip())
    except Exception:
        return "Lỗi định dạng expenses. Vui lòng nhập đúng định dạng 'tên_khoản:số_tiền', ví dụ: 'vé_máy_bay:890000,khách_sạn:650000'."
        
    total_expenses = sum(expense_dict.values())
    remaining = total_budget - total_expenses
    
    result = ["Bảng chi phí:"]
    for name, amount in expense_dict.items():
        formatted_name = name.replace("_", " ").capitalize()
        formatted_amount = f"{amount:,}".replace(",", ".") + "đ"
        result.append(f"- {formatted_name}: {formatted_amount}")
        
    result.append("---")
    
    total_exp_str = f"{total_expenses:,}".replace(",", ".") + "đ"
    budget_str = f"{total_budget:,}".replace(",", ".") + "đ"
    remaining_str = f"{remaining:,}".replace(",", ".") + "đ"
    
    result.append(f"Tổng chi: {total_exp_str}")
    result.append(f"Ngân sách: {budget_str}")
    result.append(f"Còn lại: {remaining_str}")
    
    if remaining < 0:
        over_budget_str = f"{abs(remaining):,}".replace(",", ".") + "đ"
        result.append(f"Vượt ngân sách {over_budget_str}! Cần điều chỉnh.")
        
    return "\n".join(result)

# DEBUG
flights = search_flights.invoke({"origin": "Hà Nội", "destination": "Hồ Chí Minh"})
print("flights:", flights)

hotels = search_hotels.invoke({"city": "Hồ Chí Minh", "max_price_per_night": 1_400_000})
print("hotels:", hotels)

budget = calculate_budget.invoke({"total_budget": 5000000, "expenses": "vé_máy_bay:1800000,khách_sạn:650000"})
print("budget:", budget)