# BÁO CÁO KẾT QUẢ TEST CASE (PHẦN 4)


## Test 1 — Direct Answer (Không cần tool)
**User**: `Xin chào! Tôi đang muốn đi du lịch nhưng chưa biết đi đâu.`

**Kỳ vọng**: Agent chào hỏi, hỏi thêm về sở thích/ngân sách/thời gian. Không gọi tool nào.

**Log & Output**:
```text
TravelBuddy đang suy nghĩ...
Trả lời trực tiếp

TravelBuddy:
Chào bạn! Mình rất vui được hỗ trợ bạn lên kế hoạch du lịch 😊

Để tư vấn chính xác hơn, mình cần biết thêm một vài thông tin nhé:

**Thông tin cơ bản:**
- Bạn xuất phát từ đâu? (Hà Nội, TP.HCM, Đà Nẵng...?)
- Ngân sách dự kiến bao nhiêu?
- Đi trong bao nhiêu ngày? (hoặc cuối tuần/nghỉ lễ?)
- Đi một mình hay cùng gia đình/bạn bè?

**Sở thích:**
- Bạn thích kiểu du lịch nào? 
  - Biển đảo thư giãn (Phú Quốc, Nha Trang, Đà Nẵng...)
  - Núi rừng khám phá (Sapa, Đà Lạt, Mộc Châu...)
  - Văn hóa lịch sử (Huế, Hội An...)
  - Ẩm thực - mua sắm (TP.HCM, Hà Nội...)

Với thông tin này, mình sẽ tìm cho bạn những chuyến bay và khách sạn phù hợp nhất, đảm bảo tối ưu cả ngân sách lẫn trải nghiệm! 🎒✈️

```

---


## Test 2 — Single Tool Call
**User**: `Tìm giúp tôi chuyến bay từ Hà Nội đi Đà Nẵng`

**Kỳ vọng**: Gọi search_flights("Hà Nội", "Đà Nẵng"), liệt kê 4 chuyến bay.

**Log & Output**:
```text
TravelBuddy đang suy nghĩ...
Gọi tool: search_flights({'origin': 'Hà Nội', 'destination': 'Đà Nẵng'})
Trả lời trực tiếp

TravelBuddy:
**Chuyến bay Hà Nội → Đà Nẵng:**

- **VietJet Air** | 08:30 - 09:50 | **890.000đ** (rẻ nhất)
- **Bamboo Airways** | 11:00 - 12:20 | 1.200.000đ
- **Vietnam Airlines** | 06:00 - 07:20 | 1.450.000đ
- **Vietnam Airlines** | 14:00 - 15:20 | 2.800.000đ (business)

---

**Gợi ý của mình:**

Nếu bạn muốn tiết kiệm, chọn **VietJet Air 890k** là hợp lý nhất. Nếu muốn thoải mái hơn và giờ bay linh hoạt, **Bamboo Airways 1.2 triệu** cũng là lựa chọn tốt.

Để mình tư vấn chi tiết hơn về khách sạn và tổng ngân sách, bạn cho mình biết thêm:
- **Ngày đi và về** (hoặc số đêm ở Đà Nẵng)?
- **Tổng ngân sách** dự kiến cho chuyến đi?
- Bạn muốn ở khu vực nào (gần biển Mỹ Khê, trung tâm, hay gần sân bay)?

Mình sẽ lên cho bạn phương án tối ưu nhất! 😊

```

---


## Test 3 — Multi-Step Tool Chaining
**User**: `Tôi ở Hà Nội, muốn đi Phú Quốc 2 đêm, budget 5 triệu. Tư vấn giúp!`

**Kỳ vọng**: Agent chuỗi nhiều bước: search_flights, search_hotels, calculate_budget.

**Log & Output**:
```text
TravelBuddy đang suy nghĩ...
Gọi tool: search_flights({'origin': 'Hà Nội', 'destination': 'Phú Quốc'})
Gọi tool: calculate_budget({'total_budget': 5000000, 'expenses': 'vé_máy_bay:1100000'})
Gọi tool: search_hotels({'city': 'Phú Quốc', 'max_price_per_night': 1500000})
Gọi tool: calculate_budget({'total_budget': 5000000, 'expenses': 'vé_máy_bay:1100000,khách_sạn:1600000'})
Trả lời trực tiếp

TravelBuddy:
Xong rồi! Đây là phương án tối ưu cho chuyến đi Phú Quốc 2 đêm của bạn:

**Chuyến bay:**
- VietJet Air | 16:00 - 18:15 | 1.100.000đ (khứ hồi) | hạng economy
  *(Chọn chuyến chiều này vì rẻ nhất, giúp tiết kiệm ngân sách)*

**Khách sạn:**
- Lahana Resort | 3 sao | Khu vực: Dương Đông | Rating: 4.0 | 800.000đ/đêm
  *(Tổng 2 đêm: 1.600.000đ - vị trí thuận tiện, chất lượng tốt, giá hợp lý)*

**Tổng chi phí ước tính:**
- Vé máy bay: 1.100.000đ
- Khách sạn (2 đêm): 1.600.000đ
- **Tổng: 2.700.000đ**
- **Còn lại: 2.300.000đ**

**Gợi ý thêm:**
- 2,3 triệu còn lại đủ cho ăn uống (khoảng 300-400k/ngày), thuê xe máy (150-200k/ngày), tham quan (vé VinWonders ~600k, cáp treo Hòn Thơm ~600k)
- Nên ăn hải sản tại chợ đêm Dương Đông để vừa ngon vừa tiết kiệm
- Thuê xe máy tự túc sẽ rẻ hơn taxi/grab nhiều

**Phương án thay thế nếu muốn tiết kiệm hơn:**
- Chọn 9Station Hostel (200k/đêm = 400k/2 đêm) → tiết kiệm thêm 1,2 triệu cho hoạt động vui chơi

Chúc bạn có chuyến đi vui vẻ! 🌴

```

---


## Test 4 — Missing Info / Clarification
**User**: `Tôi muốn đặt khách sạn`

**Kỳ vọng**: Agent hỏi lại: thành phố nào? bao nhiêu đêm? ngân sách bao nhiêu? Không gọi tool vội.

**Log & Output**:
```text
TravelBuddy đang suy nghĩ...
Trả lời trực tiếp

TravelBuddy:
Chào bạn! Mình sẵn sàng hỗ trợ bạn tìm khách sạn phù hợp. 

Để tư vấn chính xác nhất, bạn cho mình biết thêm một số thông tin nhé:

1. **Bạn muốn đặt khách sạn ở đâu?** (ví dụ: Đà Nẵng, Phú Quốc, Hà Nội, Hồ Chí Minh...)
2. **Ngân sách của bạn là bao nhiêu?** (tổng ngân sách hoặc giá tối đa/đêm)
3. **Bạn ở mấy đêm?**
4. **Có yêu cầu gì đặc biệt không?** (gần biển, trung tâm thành phố, có hồ bơi...)

Với thông tin này, mình sẽ tìm cho bạn những lựa chọn tốt nhất! 😊

```

---


## Test 5 — Guardrail / Refusal
**User**: `Giải giúp tôi bài tập lập trình Python về linked list`

**Kỳ vọng**: Từ chối lịch sự, nói rằng chỉ hỗ trợ về du lịch.

**Log & Output**:
```text
TravelBuddy đang suy nghĩ...
Trả lời trực tiếp

TravelBuddy:
Mình là Trợ lý Du lịch của TravelBuddy, chuyên tư vấn về chuyến đi, vé máy bay, khách sạn và lập kế hoạch du lịch tại Việt Nam thôi bạn ơi 😊

Mình không thể giúp bạn với bài tập lập trình được. Nhưng nếu bạn đang cần:
- Lên kế hoạch cho chuyến du lịch
- Tìm vé máy bay giá tốt
- Đặt khách sạn phù hợp ngân sách
- Tư vấn lịch trình và chi phí

Thì cứ hỏi mình nhé! Bạn có dự định đi du lịch đâu không? 🌴✈️

```

---


## Test 6 — Reverse Route & Non-existent City
**User**: `Mình muốn bay từ Đà Nẵng sang Hà Nội, tiện thể xem có chuyến nào đến Cà Mau luôn không?`

**Kỳ vọng**: Với Đà Nẵng - Hà Nội: Tự tra ngược chiều. Với Cà Mau: Báo không có dữ liệu.

**Log & Output**:
```text
TravelBuddy đang suy nghĩ...
Gọi tool: search_flights({'origin': 'Đà Nẵng', 'destination': 'Hà Nội'})
Gọi tool: search_flights({'origin': 'Đà Nẵng', 'destination': 'Cà Mau'})
Trả lời trực tiếp

TravelBuddy:
Mình vừa kiểm tra xong rồi nhé! Đây là thông tin cho bạn:

## Chuyến bay Đà Nẵng → Hà Nội:

Hiện tại hệ thống đang trả về thông tin chuyến **Hà Nội → Đà Nẵng** (chiều ngược lại), các hãng thường có chuyến khứ hồi với giá tương đương:

- **VietJet Air** | 08:30 - 09:50 | **890.000đ** | economy (rẻ nhất)
- **Bamboo Airways** | 11:00 - 12:20 | **1.200.000đ** | economy
- **Vietnam Airlines** | 06:00 - 07:20 | **1.450.000đ** | economy
- **Vietnam Airlines** | 14:00 - 15:20 | **2.800.000đ** | business

## Chuyến bay Đà Nẵng → Cà Mau:

❌ **Không có chuyến bay trực tiếp** từ Đà Nẵng đến Cà Mau.

### Gợi ý thay thế:

**Để đến Cà Mau từ Đà Nẵng, bạn có 2 phương án:**

1. **Bay Đà Nẵng → TP.HCM**, sau đó:
   - Bay tiếp TP.HCM → Cà Mau (khoảng 45 phút bay)
   - Hoặc đi xe khách/ô tô (khoảng 6-7 tiếng)

2. **Bay Đà Nẵng → Cần Thơ** (nếu có), rồi đi xe xuống Cà Mau (khoảng 2-3 tiếng)

Bạn muốn mình tìm chuyến bay Đà Nẵng → TP.HCM để transit xuống Cà Mau không? Hoặc bạn có ngân sách và thời gian cụ thể để mình tư vấn phương án tối ưu nhất nhé! 😊

```

---


## Test 7 — Impossible Constraints (Budget Overflow)
**User**: `Tôi có đúng 1 triệu rưỡi. Muốn đi từ Hồ Chí Minh đến Đà Nẵng bằng Vietnam Airlines và ở khách sạn Mường Thanh.`

**Kỳ vọng**: Gọi flights và hotels, nhận ra cấu hình vượt xa 1.5tr, báo cáo cháy túi và đề xuất đổi hãng/khách sạn.

**Log & Output**:
```text
TravelBuddy đang suy nghĩ...
Gọi tool: search_flights({'origin': 'Hồ Chí Minh', 'destination': 'Đà Nẵng'})
Gọi tool: search_hotels({'city': 'Đà Nẵng'})
Gọi tool: calculate_budget({'total_budget': 1500000, 'expenses': 'vé_máy_bay_Vietnam_Airlines:1300000,khách_sạn_Mường_Thanh_1_đêm:1800000'})
Trả lời trực tiếp

TravelBuddy:
Mình thấy với ngân sách 1,5 triệu, yêu cầu của bạn **không khả thi** vì:

**Chi phí thực tế:**
- Vé Vietnam Airlines (1 chiều): 1.300.000đ
- Khách sạn Mường Thanh Luxury (1 đêm): 1.800.000đ
- **Tổng chỉ riêng 2 khoản này: 3.100.000đ** → vượt ngân sách 1.600.000đ

---

## 🎯 Phương án thay thế phù hợp ngân sách 1,5 triệu:

**Chuyến bay:**
- VietJet Air | 13:00 - 14:20 | **780.000đ** (tiết kiệm 520k so với Vietnam Airlines)

**Khách sạn:**
- Memory Hostel | 2 sao | Hải Châu | Rating 4.6 | **250.000đ/đêm** (1 đêm)
- *Hoặc* Christina's Homestay | 3 sao | An Thượng | Rating 4.3 | **350.000đ/đêm** (tốt hơn một chút)

**Tổng chi phí ước tính (phương án tiết kiệm):**
- Vé máy bay: 780.000đ
- Khách sạn (1 đêm): 250.000đ
- **Tổng: 1.030.000đ**
- **Còn lại: ~470.000đ** cho ăn uống, di chuyển

---

**Gợi ý thêm:**
- Nếu muốn giữ Vietnam Airlines + Mường Thanh, bạn cần tối thiểu **3,5 triệu** (bao gồm vé khứ hồi + 1 đêm + ăn uống)
- Với 1,5 triệu, bạn chỉ đủ đi **1 chiều** và ở khách sạn bình dân
- Nếu muốn trải nghiệm tốt hơn, cân nhắc tăng ngân sách hoặc chọn điểm đến gần hơn

Bạn muốn mình tư vấn thêm phương án nào không? 😊

```

---


## Test 8 — Implicit City Inference & Math
**User**: `Tôi ở Hà Nội, định trốn việc đi nghỉ dưỡng ở Vinpearl Resort 3 đêm cùng vợ. Ngân sách gộp cả đi cả về là 15 triệu.`

**Kỳ vọng**: Tự hiểu Vinpearl ở Phú Quốc. Tính tiền vé máy bay x2 (người), tiền phòng x3, gọi calculate_budget trừ vào 15 triệu.

**Log & Output**:
```text
TravelBuddy đang suy nghĩ...
Trả lời trực tiếp

TravelBuddy:
Mình sẽ giúp bạn lên kế hoạch chuyến nghỉ dưỡng Vinpearl nhé! Để tư vấn chính xác nhất, mình cần biết thêm:

**Bạn muốn đi Vinpearl ở đâu?** (Phú Quốc, Nha Trang, Hội An, Đà Nẵng, Nam Hội An...?)

Trong khi đó, mình có thể chia sẻ sơ bộ về ngân sách 15 triệu cho 2 người, 3 đêm:

**Phân bổ ngân sách dự kiến:**
- Vé máy bay khứ hồi 2 người: 3-5 triệu (tùy điểm đến)
- Khách sạn 3 đêm: 6-9 triệu (Vinpearl thường 2-3 triệu/đêm)
- Ăn uống + di chuyển: 2-3 triệu

**Gợi ý điểm đến phù hợp ngân sách:**

1. **Vinpearl Nha Trang** - vé máy bay rẻ nhất từ Hà Nội, nhiều lựa chọn resort
2. **Vinpearl Phú Quốc** - đẹp nhất nhưng vé máy bay đắt hơn
3. **Vinpearl Nam Hội An** - cân bằng giá và trải nghiệm

Bạn cho mình biết muốn đi đâu để mình tìm chuyến bay và khách sạn cụ thể nhé! 😊

```

---


## Test 9 — Distracted / Rambling Prompt
**User**: `Nóng quá làm tôi lười code. Đi từ Hồ Chí Minh ra Phú Quốc ngân sách 3 triệu có đủ cho 1 đêm không? Sếp đang giục task mà chán quá.`

**Kỳ vọng**: Lọc bỏ rác (code, sếp). Gọi flights, hotels (1 đêm) để chứng minh 3 triệu là đủ.

**Log & Output**:
```text
TravelBuddy đang suy nghĩ...
Gọi tool: search_flights({'origin': 'Hồ Chí Minh', 'destination': 'Phú Quốc'})
Gọi tool: calculate_budget({'total_budget': 3000000, 'expenses': 'vé_máy_bay_khứ_hồi:1300000'})
Gọi tool: search_hotels({'city': 'Phú Quốc', 'max_price_per_night': 1700000})
Gọi tool: calculate_budget({'total_budget': 3000000, 'expenses': 'vé_máy_bay_khứ_hồi:1300000,khách_sạn_1_đêm:800000'})
Trả lời trực tiếp

TravelBuddy:
**Đủ rồi bạn ơi! Nghỉ code đi biển được luôn 🏖️**

---

**Chuyến bay:**
- VietJet Air | 15:00 - 16:00 (khứ hồi) | 1.300.000đ

**Khách sạn:**
- Lahana Resort | 3 sao | Dương Đông | 800.000đ/đêm | Rating: 4.0

**Tổng chi phí ước tính:**
- Vé máy bay khứ hồi: 1.300.000đ
- Khách sạn 1 đêm: 800.000đ
- **Tổng: 2.100.000đ**
- **Còn lại: 900.000đ**

---

**Gợi ý thêm:**
- 900k còn lại đủ cho ăn uống (hải sản chợ đêm Dương Đông ~300k), thuê xe máy (~150k/ngày), và vài ly bia biển
- Nếu muốn tiết kiệm hơn, chọn 9Station Hostel (200k/đêm) thì còn 1.5 triệu xài thoải mái
- Bay chiều 15h thì sáng còn làm việc được, chiều đến Phú Quốc kịp ăn tối ngắm hoàng hôn

**Đi đi, task để mai lo! 😎**

```

---


## Test 10 — Broad Comparison Search
**User**: `Tôi ở Hà Nội, vứt tôi đến thẳng Đà Nẵng hoặc Phú Quốc đều được, kiểm tra xem vé máy bay chỗ nào rẻ hơn thì đi.`

**Kỳ vọng**: Tự động gọi search_flights 2 lần cho 2 tuyến, so sánh giá rẻ nhất (VietJet đi ĐN 890k) để rủ rê người dùng.

**Log & Output**:
```text
TravelBuddy đang suy nghĩ...
Gọi tool: search_flights({'origin': 'Hà Nội', 'destination': 'Đà Nẵng'})
Gọi tool: search_flights({'origin': 'Hà Nội', 'destination': 'Phú Quốc'})
Trả lời trực tiếp

TravelBuddy:
## So sánh giá vé máy bay:

**Đà Nẵng - RẺ HƠN** ✈️
- VietJet Air | 08:30 - 09:50 | **890.000đ** (rẻ nhất)
- Bamboo Airways | 11:00 - 12:20 | 1.200.000đ
- Vietnam Airlines | 06:00 - 07:20 | 1.450.000đ

**Phú Quốc**
- VietJet Air | 16:00 - 18:15 | **1.100.000đ** (rẻ nhất)
- VietJet Air | 10:00 - 12:15 | 1.350.000đ
- Vietnam Airlines | 07:00 - 09:15 | 2.100.000đ

---

## Kết luận:

**→ Đà Nẵng rẻ hơn 210.000đ** (chỉ tính vé 1 chiều)

Nếu tính khứ hồi, bạn tiết kiệm được khoảng **420.000đ** khi chọn Đà Nẵng thay vì Phú Quốc.

**Gợi ý của mình:**
- **Đà Nẵng**: Phù hợp nếu bạn thích khám phá đô thị, ăn uống đa dạng, gần Hội An/Bà Nà. Chi phí ăn uống và di chuyển cũng rẻ hơn Phú Quốc.
- **Phú Quốc**: Chọn nếu bạn muốn nghỉ dưỡng biển, lặn ngắm san hô, không ngại chi thêm một chút.

Bạn có ngân sách bao nhiêu và dự định đi mấy ngày để mình tư vấn chi tiết hơn về khách sạn và tổng chi phí nhé? 😊

```

---

