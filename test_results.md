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

Để tư vấn chuyến đi phù hợp nhất, mình cần biết thêm một vài thông tin:

1. **Ngân sách dự kiến**: Bạn có khoảng bao nhiêu tiền cho chuyến đi này?
2. **Xuất phát từ đâu**: Bạn ở thành phố nào? (Hà Nội, TP.HCM, Đà Nẵng...)
3. **Thời gian**: Bạn dự định đi bao nhiêu ngày? Hoặc có khung thời gian cụ thể nào không?
4. **Sở thích**: Bạn thích biển, núi, thành phố, hay khám phá văn hóa?

Với thông tin này, mình sẽ gợi ý cho bạn những điểm đến phù hợp nhất với ngân sách và sở thích của bạn nhé! 🌏

```

---


## Test 2 — Single Tool Call
**User**: `Tìm giúp tôi chuyến bay từ Hà Nội đi Đà Nẵng`
**Kỳ vọng**: Gọi search_flights("Hà Nội", "Đà Nẵng"), liệt kê 4 chuyến bay.

**Log & Output**:
```text
TravelBuddy đang suy nghĩ...
Trả lời trực tiếp

TravelBuddy:
Mình cần thêm vài thông tin để tư vấn tốt hơn nhé:

- **Ngày đi** và **ngày về** dự kiến?
- **Số người** đi cùng?
- **Ngân sách** tổng cho chuyến đi khoảng bao nhiêu?
- Có cần tìm khách sạn luôn không?

Nếu bạn chỉ cần xem giá vé máy bay trước, mình sẽ tìm các chuyến bay phổ biến từ Hà Nội đi Đà Nẵng cho bạn ngay!

```

---


## Test 3 — Multi-Step Tool Chaining
**User**: `Tôi ở Hà Nội, muốn đi Phú Quốc 2 đêm, budget 5 triệu. Tư vấn giúp!`
**Kỳ vọng**: Agent chuỗi nhiều bước: search_flights, search_hotels, calculate_budget.

**Log & Output**:
```text
TravelBuddy đang suy nghĩ...
Gọi tool: search_flights({'origin': 'Hà Nội', 'destination': 'Phú Quốc'})
Gọi tool: search_hotels({'city': 'Phú Quốc'})
Gọi tool: calculate_budget({'total_budget': 5000000, 'expenses': 'vé_máy_bay:1100000,khách_sạn_2_đêm:400000'})
Trả lời trực tiếp

TravelBuddy:
Xong rồi! Đây là phương án tối ưu cho chuyến đi Phú Quốc 2 đêm của bạn:

## **Chuyến bay:**
- **VietJet Air** | 16:00 - 18:15 | **1.100.000đ** (khứ hồi)
  *(Chọn chuyến chiều vì rẻ nhất, tiết kiệm được 1 triệu so với Vietnam Airlines)*

## **Khách sạn:**
- **9Station Hostel** | 2 sao | Dương Đông | Rating: 4.5 | **200.000đ/đêm**
  *(Tổng 2 đêm: 400.000đ - sạch sẽ, gần trung tâm, đánh giá tốt)*

## **Tổng chi phí ước tính:**
- Vé máy bay: 1.100.000đ
- Khách sạn (2 đêm): 400.000đ
- **Tổng: 1.500.000đ**
- **Còn lại: 3.500.000đ** cho ăn uống, thuê xe, tham quan

## **Gợi ý thêm:**

✅ **Với 3.5 triệu còn lại, bạn thoải mái:**
- Thuê xe máy: ~150k/ngày (300k/2 ngày)
- Ăn uống: ~500k/ngày (1 triệu/2 ngày)
- Vé tham quan (VinWonders, cáp treo Hòn Thơm): ~1.5 triệu
- Còn dư ~500k cho chi phí phát sinh

💡 **Phương án nâng cấp (nếu muốn):**
- Nếu muốn khách sạn tốt hơn, có thể chọn **Lahana Resort 3 sao** (800k/đêm = 1.6 triệu/2 đêm), tổng chi ~2.7 triệu, còn lại 2.3 triệu vẫn đủ thoải mái.

Chuyến đi này rất fit với budget 5 triệu của bạn! Có gì cần tư vấn thêm không? 😊

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

Để tư vấn chính xác nhất, bạn cho mình biết thêm một vài thông tin nhé:

- **Bạn muốn đặt khách sạn ở đâu?** (ví dụ: Đà Nẵng, Phú Quốc, Hồ Chí Minh...)
- **Ngân sách của bạn là bao nhiêu?** (tổng ngân sách hoặc giá tối đa/đêm)
- **Bạn ở mấy đêm?**

Với thông tin này, mình sẽ tìm cho bạn những lựa chọn tốt nhất về giá và vị trí! 😊

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
Mình là Trợ lý Du lịch của TravelBuddy, chuyên tư vấn về chuyến đi, vé máy bay, khách sạn và ngân sách du lịch tại Việt Nam thôi bạn nhé 😊

Mình không thể giúp bạn với bài tập lập trình Python được. Nếu bạn cần hỗ trợ về:
- Lên kế hoạch du lịch
- Tìm vé máy bay giá tốt
- Đặt khách sạn phù hợp ngân sách
- Tính toán chi phí chuyến đi

Thì cứ hỏi mình nhé! Bạn đang có kế hoạch đi du lịch nào không? 🌴✈️

```

---

