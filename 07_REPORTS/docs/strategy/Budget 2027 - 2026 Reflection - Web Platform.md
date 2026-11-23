# 2026 REFLECTION & 2027 DIRECTION - WEB PLATFORM

---

## EXECUTIVE SUMMARY

**Web Platform đã chuyển từ đội kỹ thuật thực thi sang Growth Unit. 2027 đề xuất 1,996 tỷ đ để biến lưu lượng tự nhiên thành kết quả đo được, trong khi Organic đang là kênh cần bảo vệ nhất.**

1. **Web Platform chuyển dịch vai trò.** Năm 2026, Web Platform vận hành hạ tầng dùng chung và đồng hành 3 Hub: Cinema, Financial, Vehicle. 16 Cell Teams được Web Platform hỗ trợ, trong đó 6 tự vận hành Mini Web qua MoSpark. Hạ tầng đã chuyển từ AWS sang FPT Cloud 100% (36 frontend, 11 backend, 3 database), không có downtime.

2. **Traffic Web tạo ra Install, MAU và GMV ngoài PageView.** Cinema ghi nhận ==168.884 vé== và ==15,91 tỷ đ GMV== từ luồng Web-to-App trong 10 tháng. Lượt cài đặt từ Web tăng từ 5.239 (T7) lên 11.143 (T10), gấp 2,1 lần. Tháng 10 có 3.902 đăng ký và 1.284 MAU.

3. **Đo lường Full Funnel Web-to-App đã vận hành.** Tracking GA4 đưa vào BigQuery và Dashboard, chạy từ T5/2026. 100% liên kết đã chuẩn hóa sang OneLink, và Identity Platform theo dõi người dùng từ Web sang App. Tháng 10, !!35,0%!! lượt cài đặt đăng ký và 61,2% đăng ký liên kết ngân hàng. Điểm nghẽn nằm ở bước cài đặt sang đăng ký.

4. **Có tín hiệu AI Traffic nhưng quy mô còn nhỏ.** Lưu lượng GEO tháng 10 đạt 18.547 PageView (GA4, 31 ngày), tăng 36,4% MoM, tương đương khoảng 0,5% tổng PageView. Phạt Nguội nhận ==660 trích dẫn== từ AI trong 28 ngày đầu, là bằng chứng cho quy trình GEO đã kiểm chứng.

5. **Organic đang chịu áp lực từ AI Overview và AI Agent.** Tháng 10, Organic Search chỉ tăng !!5,7%!! MoM và đạt 1,72M PageView, tương đương 47,6% tổng PageView. Non-Paid bù được 52% phần Paid giảm, nhưng Organic chưa tự tăng trưởng bền vững. AI Search đang làm giảm lượt nhấp vào nội dung kiến thức chung. Vì vậy 2027 chuyển đầu tư sang công cụ tương tác và nội dung có dữ liệu thời gian thực.

**Đề xuất ngân sách:** 1,996 tỷ đ, giải ngân theo quý cho ba dự án Cinema, CIC & Tín dụng và Tích lũy & Đầu tư, với phần đồng tài trợ từ BU. Kỳ vọng tăng thêm ==6,1-8,3M PageView==, tương đương ==6,3-8,8 tỷ đ GMV Cinema== và 84-113 nghìn lượt mở App Financial. Chuyển đổi là chỉ số đo, không phải cam kết của khoản đầu tư. So sánh này chưa cùng kỳ (mục tiêu 12 tháng so với 10 tháng thực tế), nên mức tăng có thể cao hơn thực tế khoảng 20%. Financial giải ngân 2 đợt; đợt 2 (790 triệu đ) chỉ khi đạt ngưỡng cuối Q2.

**Rủi ro lớn nhất:** để đạt ==55,57M PageView Non-Paid== trong năm 2027, phần Non-Paid ngoài ba dự án có ngân sách phải tăng thêm khoảng 14,5-16,7M PageView, chiếm khoảng 64-73% mức tăng Non-Paid (22,80M). Phần này chưa có kế hoạch riêng. Nếu Q1/2027 tăng dưới 15%, Web Platform sẽ rà soát lại mục tiêu trước khi giải ngân đợt 2.

---

## PHẦN 1: REFLECTION 2026

Web Platform phụ trách nền tảng công nghệ dùng chung (Shared Platform) cho Web MoMo. Đội ngũ phối hợp với ITC để cung cấp hạ tầng, thư viện, công cụ và quy trình, phục vụ các Mini Web trên momo.vn của Cell Teams, BUs và Division.

Web Platform tạo giá trị ở 3 tầng:

- **Tầng MoMo:** Xây dựng Content Authority cho các Theme theo User Journey, để Google Search và AI Chatbot (ChatGPT, Gemini, Perplexity) trích dẫn MoMo là nguồn uy tín. Từ đó chuyển thị trường chưa được phục vụ thành lưu lượng chất lượng cao vào các Mini Web.
- **Tầng User:** Thay vì nội dung tĩnh, Web Platform xây dựng Utility Tools giải quyết nhu cầu cụ thể trong quá trình tìm kiếm, tạo giá trị thực để tăng tỷ lệ chuyển đổi sang App.
- **Tầng BUs:** Web Platform đóng vai trò Platform-as-a-Service nội bộ: tư vấn giải pháp, cung cấp nền tảng, đồng hành phát triển các dự án chiến lược theo chuẩn Product-Led Growth.

**Hai mô hình phục vụ:**

- **Mô hình 1, CMS tự phục vụ (BUs Self-serve):** Phối hợp với BMC xây dựng công cụ Admin Panel cho BU tự tạo, chỉnh sửa và xuất bản Web Page. Mục tiêu H2/2026 là giảm việc thủ công lặp lại của cả hai bên.
- **Mô hình 2, Phát triển trực tiếp (Dedicated Build):** Đồng hành với Cell Teams phát triển các Web Product có UI/UX và nghiệp vụ riêng, tuân thủ Mobase Design System. Tùy năng lực từng Cell Team, Web Platform tham gia theo 3 hình thức: tư vấn, đồng hành phát triển, hoặc chuyển giao để Cell Team tự vận hành. Điển hình là Cinema Hub, Vehicle Hub, Financial Hub và Student Hub.

**Giá trị kinh tế:** Thay vì mỗi Cell Team tự duy trì đội kỹ thuật Web và tên miền riêng, tất cả kết nối vào momo.vn để thừa hưởng uy tín thương hiệu, Domain Authority và hạ tầng đã chuẩn hóa.

**Chuyển dịch chiến lược 2026:** Từ đội kỹ thuật nhận yêu cầu và thực thi, Web Platform trở thành Platform-powered Growth Unit: vận hành nền tảng dùng chung, phối hợp Out-App Traffic Team thiết kế giải pháp PLG, và cùng Cell Teams tạo tác động kinh doanh đo được trên kênh Web.

**Out-App Traffic Team:** Năng lực mở rộng của Web Platform, tập trung vào tư vấn và phối hợp có chọn lọc do nguồn lực còn mỏng.

### 1.1. Objectives 2026

Năm 2026, Web Platform thực hiện bốn Objective, chia thành hai hoạt động lớn:

| Objective | Hoạt động | Kết quả chính đến 10/2026 |
| :--- | :--- | :--- |
| Objective 1: Phát triển Strategic Themes theo PLG | Tăng trưởng | Phân tích hơn 30 Theme; triển khai PLG cho Cinema, Financial, Vehicle và Student. Cinema đạt 9,1M PageView trong 10 tháng; Financial đạt 273.705 PageView tháng 10. |
| Objective 2: CMS tự phục vụ bằng AI | Nền tảng | MoSpark đưa vào vận hành từ Q2. 16 Cell Teams được hỗ trợ, trong đó 6 tự vận hành. Landing page rút từ 1-2 tuần xuống 1-2 ngày. |
| Objective 3: Đo lường Full Funnel Web-to-App | Nền tảng | Tracking GA4 và OneLink đầy đủ, Dashboard live từ T5. Tháng 10 có 11.143 lượt cài đặt từ Web. |
| Objective 4: Hạ tầng vận hành ổn định | Nền tảng | Chuyển AWS sang FPT Cloud: 36/36 frontend, 11/11 backend, 3/3 database, không rollback và không downtime. |

### 1.2. Tăng trưởng: kết quả trên Web

**Objective 1, Strategic Themes Dominance:** Phân tích thị trường, tư vấn và hợp tác Cell Teams xây dựng Web Product theo PLG. Từ hơn 30 Theme được rà soát, Web Platform đã triển khai PLG Solution cho các dự án chiến lược trong H2/2026.

**Tổng quan lưu lượng Web, T1-T10/2026**

Web đạt ==32,9M PageView== trong 10 tháng. Tháng 9 là tháng cao nhất với 3,95M PageView. Tỷ trọng lưu lượng tự nhiên tăng dần khi Paid giảm: 77-80% trong quý 1 đến quý 3, và 86,9% trong tháng 10.

| Tháng | PageView Web (triệu) | Click to App hợp lệ (lượt) | Tỷ lệ trên PageView |
| :--- | :---: | :---: | :---: |
| T1/2026 | 2,60 | 3.955 | 0,2% |
| T2/2026 | 3,47 | 5.924 | 0,2% |
| T3/2026 | 3,22 | 2.244 | 0,1% |
| T4/2026 | 2,70 | 1.119.858* | 41,7%* |
| T5/2026 | 3,27 | 39.862 | 1,2% |
| T6/2026 | 3,41 | 79.018 | 2,3% |
| T7/2026 | 3,17 | 41.948 | 1,3% |
| T8/2026 | 3,47 | 86.149 | 2,5% |
| T9/2026 | 3,95 | 71.522 | 1,8% |
| T10/2026 | 3,60 | 83.801 | 2,3% |
| **Lũy kế (không tính T4)** | **30,16** | **414.423** | **1,4%** |

- Lưu lượng từ AI (kênh AI Assistant trên GA4): 70.758 PageView từ tháng 1 đến tháng 10, tăng từ 1.301 PageView (tháng 5) lên 18.547 PageView (tháng 10). Tháng 1-4 không có ghi nhận trong nguồn đo này.
- Click to App hợp lệ là sự kiện click_to_app có đường dẫn OneLink hợp lệ. Tháng 10 có 83.801 lượt, tương đương 2,3% PageView. Tháng 4 bị lỗi chuyển giao dữ liệu sang BigQuery làm đếm trùng (*), nên không đưa vào lũy kế và không dùng để đánh giá. Phần lớn sự kiện click_to_app thiếu tham số đường dẫn, cần sửa tracking GTM.
- Tháng 10: 3,60M PageView, giảm 8,9% so với tháng 9 sau khi cắt 723.612 PageView từ Paid kém hiệu quả. Lưu lượng tự nhiên đạt 3,13M (+13,5%): Organic Search 1,72M (+5,7%), Direct 0,93M (+23,3%), Referral và nguồn khác 0,48M (+27,9%), lưu lượng từ AI 18.547 PageView (+36,4%).
- Hub lớn nhất tháng 10 là Cinema với 1,13M PageView (khoảng 31% tổng lưu lượng), tiếp theo là Financial Hub với 273.705 PageView (+9,6% MoM, theo báo cáo tháng 10).

Các bảng Hub dưới đây đọc theo phễu: Impression → PageView → chuyển đổi (vé, đơn hàng, GMV, cài đặt).

**Impression (Google Search):** số lần các trang của Hub xuất hiện trên kết quả tìm kiếm Google trong tháng, tổng các URL thuộc Hub, lấy từ Google Search Console (tìm kiếm web). Một lượt tìm kiếm có thể làm nhiều trang xuất hiện, nên Impression không bằng số lượt tìm kiếm của thị trường.

**Cinema Hub.** Baseline lưu lượng lớn nhất trong 5 Strategic Hubs, và là dự án có vấn đề chuyển đổi cần xử lý sớm nhất.

| Tháng | Impression (Google Search) | PageView Cinema Hub | Vé | Đơn hàng | GMV thực thu (tỷ đ) |
| :--- | :---: | :---: | :---: | :---: | :---: |
| T1/2026 | 10.988.973 | 581.349 | 12.643 | 5.889 | 1,21 |
| T2/2026 (Tết) | 14.875.825 | 1.044.429 | 28.379 | 12.432 | 2,55 |
| T3/2026 | 11.505.959 | 759.142 | 20.600 | 9.881 | 2,03 |
| T4/2026 | 11.164.473 | 851.919 | 18.730 | 8.221 | 1,69 |
| T5/2026 | 12.779.934 | 994.719 | 12.561 | 5.777 | 1,18 |
| T6/2026 | 12.659.436 | 859.183 | 19.444 | 9.055 | 1,86 |
| T7/2026 | 13.009.013 | 822.859 | 5.211 | 2.425 | 0,50 |
| T8/2026 | 12.784.452 | 832.460 | 8.754 | 4.016 | 0,82 |
| T9/2026 | 11.288.422 | 1.220.075 | 20.983 | 9.807 | 2,01 |
| T10/2026 | 10.951.659 | 1.132.721 | 26.789 | 12.547 | 2,57 |
| **Lũy kế 10 tháng** | **122.008.146** | **9.098.856** | **168.884** | **77.625** | **15,91** |

- Lũy kế vé, đơn hàng, GMV lấy theo Dashboard In-App range T1-T10 (chốt 18/11/2026). Cộng các dòng tháng ra 174.094 vé / 80.050 đơn / 16,41 tỷ, cao hơn đúng bằng dòng T7; đang đối soát.

- So với mục tiêu tháng: T9 đạt 1.220.075 PageView, cao hơn mục tiêu 1,12M khoảng 9%.
- Tổng PageView 10 tháng: 9,1M, là cơ sở để tính tỷ lệ vé và GMV trên PageView trong mục 3.5.

**Financial Hub.** Financial Hub là dự án chiến lược cốt lõi, gồm bộ công cụ tài chính tương tác. Thị trường tìm kiếm tài chính khoảng 117,2 triệu lượt mỗi tháng, trong đó giá vàng chiếm 67% (78,9 triệu), chứng khoán 10,7% (12,5 triệu) và tỷ giá 7,3% (8,5 triệu). Tỷ trọng lượt truy cập của MoMo ở các nhóm này còn thấp.

- Kết quả T10/2026 theo báo cáo tháng 10: Financial Hub đạt 273.705 PageView (+9,6% MoM, đạt 109,5% target tháng theo mục tiêu 250.000 PageView). Cụm Trung Tâm Tài Chính và Tiện ích Tỷ giá đạt 43.495 PageView (+442,0%), Ví Trả Sau đạt 58.268 PageView (+38,2%), bù mức giảm 47.814 PageView của Vay Nhanh (-43,5%). Mục tiêu tháng 10 là 250.000 PageView theo báo cáo; nếu theo bảng Excel (450.000 PageView) thì tỷ lệ đạt là 60,8%.
- Sản phẩm đã go-live đến tháng 10: Tính Lương Gross/Net, Tỷ Giá, Giá Vàng (từ tháng 9), Chứng Chỉ Quỹ; công cụ ước tính khoản vay Vay Nhanh và Điểm Tín Dụng (CIC) với lượt mở App. Đang triển khai: Phân Bổ Lương 50/30/20.
- Phân chia trách nhiệm với Financial Services BU (mục tiêu cuối 2026 trong bản gốc): Web Platform cam kết 1M PageView mỗi tháng và W2A CTR 5-10%; Cell Team cam kết doanh thu, MAU và giao dịch tài chính đầu tiên tăng 25% MoM. Mô hình 2027 của Financial Hub giữ W2A CTR ở mức thực tế 2026 (CIC và Tín dụng 2,9%, Tích lũy và Đầu tư 4,0%), xem mục 3.5.
- Khoảng cách: đạt 1M PageView mỗi tháng vào cuối 2026 cần tăng khoảng !!3,7 lần!! so với mức 273.705 PageView của T10 theo báo cáo, trong 2 tháng còn lại.

**Lưu lượng Financial Hub theo use case, T1-T10/2026**

| Tháng | Impression (Google Search) | Tổng | Ví Trả Sau | Vay Nhanh | CIC & Tín dụng | Tài Chính |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| T1/2026 | 2.402.332 | 435.539 | 289.068 | 66.878 | 17.815 | 61.778 |
| T2/2026 | 1.888.547 | 448.954 | 339.153 | 50.866 | 10.379 | 48.556 |
| T3/2026 | 2.180.376 | 311.903 | 142.204 | 99.153 | 14.171 | 56.375 |
| T4/2026 | 1.428.846 | 272.962 | 119.965 | 102.129 | 13.360 | 37.508 |
| T5/2026 | 1.561.480 | 256.600 | 55.426 | 134.870 | 17.116 | 49.188 |
| T6/2026 | 1.520.476 | 235.915 | 100.783 | 88.039 | 17.864 | 29.229 |
| T7/2026 | 1.703.562 | 212.756 | 71.397 | 74.054 | 40.778 | 26.527 |
| T8/2026 | 1.782.127 | 322.059 | 81.162 | 119.652 | 92.371 | 28.874 |
| T9/2026 | 1.798.319 | 650.013 | 424.954 | 113.213 | 81.896 | 29.950 |
| T10/2026 | 2.584.523 | 273.705 | 76.224 | 53.004 | 64.676 | 79.801 |
| **Lũy kế** | **18.850.588** | **3.420.406** | **1.700.336** | **901.858** | **370.426** | **447.786** |

- **Hiệu suất công cụ (tháng 10):** công cụ tương tác đạt CTR 33,7-43,8%, gồm Ước tính khoản vay 43,8%, Tra cứu CIC 38,6% và Tính lương Gross-Net 33,7%. Bảng tĩnh (giá vàng, tỷ giá, lãi suất) đạt 0% CTR.
- **Tập trung:** ba công cụ trên chiếm 87,4% lượt tương tác công cụ của Hub (7.100 trên 8.120 lượt).
- **Utility đã triển khai:** Tính lương Gross-Net, Tỷ giá, Giá vàng (từ T9), Chứng chỉ quỹ, Ước tính khoản vay, Tra cứu điểm CIC, Trả góp Ví Trả Sau, Lãi tiết kiệm, Chuyển đổi ngoại tệ, BHXH và lương hưu.
- **Tiềm năng:** Tính Thuế TNCN và Thuế Hộ Kinh Doanh (go-live trước 10/11, mùa quyết toán thuế); gamification Điểm Tín Dụng CIC (tháng 11). Game Một Mùa Quýt có 7.097 người tham gia, 3.454 lượt click OneLink, trong đó 1.230 người dùng cài hoặc mở App.
- **Điểm yếu:** Tiết kiệm (1,5K PageView) và Chứng chỉ quỹ (458 PageView) còn lưu lượng tự nhiên thấp, cần mở rộng danh mục công cụ.
- **Cách đọc số:** bảng phân nhóm theo URL. Tháng 10 tổng theo báo cáo (273.705 PageView), phần 33.984 PageView chưa phân nhóm nằm trong Tài Chính. Ví Trả Sau tháng 10 theo báo cáo là 58.268 PageView, khác 76.224 PageView trong bảng.

**Vehicle Hub.** Dự án Phạt Nguội là Pioneer Project đã được xác nhận trong H1/2026, làm nền tảng để khởi động Vehicle Hub với sự đồng hành của VTTI và Insurtech.

- Tổng thị trường 23,2 triệu lượt tìm kiếm mỗi tháng. Giá xăng 10,52 triệu, Phạt Nguội 6,58 triệu, ETC 1,31 triệu, Trạm sạc EV 1,24 triệu.

| Tháng | Impression (Google Search) | Tổng | Phạt Nguội | Bảo hiểm ô tô | Bảo hiểm xe máy | Tiện ích giao thông |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| T5/2026 | 629.463 | 308.552 | 295.186 | 11.885 | 1.481 | - |
| T6/2026 | 692.775 | 610.152 | 597.471 | 11.112 | 1.569 | - |
| T7/2026 | 851.569 | 170.572 | 155.070 | 12.525 | 2.977 | - |
| T8/2026 | 1.002.150 | 230.333 | 213.946 | 13.105 | 3.277 | 5 |
| T9/2026 | 1.571.740 | 63.677 | 39.452 | 19.013 | 2.552 | 2.660 |
| T10/2026 | 1.973.851 | 72.954 | 24.195 | 25.502 | 2.832 | 20.425 |

- Lưu ý: T6 đạt mức cao nhất nhờ SEM. Tháng 9 giảm do API Phạt Nguội gián đoạn từ 01/09 đến 20/09. Tháng 10, lưu lượng Phạt Nguội giảm và cần SEO On-Page cùng liên kết nội bộ để phục hồi. Số liệu lấy từ GA4 theo đường dẫn, cùng một quy tắc cho tất cả các tháng: Phạt Nguội gồm các đường dẫn /phat-nguoi kể cả blog, không tính trang tin tức khuyến mãi; bảo hiểm và tiện ích theo nhóm đường dẫn tương ứng. Cột Tổng là tổng của bốn cột sản phẩm.

**InsurTech (bảo hiểm), 01/01-12/11/2026**

Web mang về 136.819 người dùng bảo hiểm, tăng 32% so với cả năm 2025. Có 44-51% người mua bảo hiểm trên web chưa có ví MoMo, là nhóm khách Web tiếp cận thêm ngoài App.

| Sản phẩm | Traffic web | So với 2025 | Kết quả từ web | Đầu tư SEO + SEM |
| :--- | :---: | :---: | :---: | :---: |
| BH thân vỏ (VCX) | 162.304 | +46% | 2.118 leads, 71 đơn (khoảng 462 triệu đ GMV) | 1,05 tỷ đ |
| BH xe máy (XMBB) | 90.522 | !!-52%!! | 1.948 đơn về App, 1.750 người mua trên web | 350 triệu đ |
| BHYT | 196.198 | Gấp 4,4 lần | 2.643 người mua, ==86% chốt ngay trên web== | 150 triệu đ |

- VCX: tỷ lệ chuyển từ lead sang đơn đạt !!3,3%!!, thấp hơn mục tiêu 7-10%. Đây là điểm cần tối ưu trước khi tăng đầu tư.
- XMBB: traffic web năm nay bằng !!48%!! cả năm 2025, dù đã có 10/10 từ khóa mục tiêu trong top 10. Nguyên nhân chưa được xác định.
- BHYT: chi phí SEO và SEM khoảng 57.000 đ cho mỗi người mua từ web, thấp nhất trong ba sản phẩm.
- Hành động 2027: chuyển trọng tâm từ đẩy thứ hạng sang tối ưu chuyển đổi trên từng trang.

**Sản phẩm khác đóng góp GMV trên Web, T1-T10/2026**

| Sản phẩm | Chỉ số đến tháng 10 | GMV | Ghi chú |
| :--- | :---: | :---: | :--- |
| Vé xe (/ve-xe) | 3.787 MAU giao dịch | - | Lưu lượng theo nhu cầu đi lại dịp lễ |
| eSIM du lịch | 824 giao dịch | 160,4 triệu đ | Tỷ lệ chuyển đổi 3,18%; không phát sinh chi phí quảng cáo |

**New Users: lượt cài đặt và phễu đăng ký từ Web**

Lượt cài đặt từ Web tăng từ 5.239 (T7) lên 11.143 (T10), gấp 2,1 lần. Riêng tháng 10 tăng 6,1% so với tháng 9.

Phần lớn lượt cài đặt đến từ banner Chào MoMo trên toàn Web: 8.517 lượt, chiếm 76% tổng cài đặt tháng 10. Cinema Hub đóng góp 1.931 lượt (17%), với tỷ lệ từ đăng ký sang liên kết ngân hàng đạt 25,1%. Tăng trưởng cài đặt đang phụ thuộc lớn vào một cơ chế dẫn dắt.

Phễu tháng 10:
- Cài đặt sang đăng ký: 3.902 (35,0%). Đây là bước rớt lớn nhất, khoảng 65% người cài đặt chưa đăng ký.
- Đăng ký sang liên kết ngân hàng: 2.389 (61,2%), mức cao nhất từ đầu năm.
- Liên kết ngân hàng sang sử dụng thực tế (MAU): 1.284 (khoảng 54%). Tổng từ cài đặt đến MAU đạt 11,5%.

Theo nền tảng, người dùng iOS chiếm 51% lượt cài đặt nhưng chiếm 57% số người liên kết ngân hàng và 59% MAU trong tháng 10.

Hành động: ưu tiên tối ưu bước đăng ký ngay sau khi cài đặt, vì đây là nơi mất nhiều người dùng nhất. Đồng thời mở rộng nguồn cài đặt ngoài banner toàn Web để giảm phụ thuộc vào một kênh.

### 1.3. Nền tảng: hạ tầng, CMS và đo lường

**Objective 2, AI-Powered CMS Self-serve:** Phát triển nền tảng CMS để Cell Teams tự tạo và xuất bản Web Page chuẩn SEO/GEO.

- MoSpark đưa vào vận hành thực tế từ Q2/2026, với các Module: Landing Page Builder, GenAI Content Pipeline, PLG Project Engine, Ads Manager, Chatbot và Knowledge Base.
- Landing Page Builder rút thời gian từ 1-2 tuần xuống 1-2 ngày. Cell Team tự xuất bản, không cần Dev. Đang thử nghiệm với GMC, BMC và MDS.
- GenAI Content Pipeline tự động hóa khoảng 80% quy trình sản xuất nội dung chuẩn SEO/GEO, rút từ nhiều ngày xuống vài giờ.
- 16 Cell Teams được hỗ trợ, trong đó 6 tự vận hành Mini Web.
- Ngoài phạm vi momo.vn, MoSpark được cung cấp cho các dự án khác như momo.career và L&D.
- Phối hợp với BMC: BMC phụ trách Brand Guideline và quy trình duyệt Creative/Legal. Web Platform cung cấp MoSpark CMS và hạ tầng.

**Objective 3, Full Funnel Tracking Pipeline:** Chuẩn hóa tracking và báo cáo chuyển đổi Web-to-App.

- Các hạng mục đã triển khai: GA4 và GTM vào BigQuery; Google Search Console vào BigQuery để theo dõi theo URL; chuẩn hóa 100% liên kết sang OneLink; Identity Platform (Edge Cookie) nhận diện và kết nối hành vi người dùng từ Web sang App; Dashboard Web Performance live từ T5/2026.
- Ý nghĩa: từ T5/2026, Web Platform có baseline để theo dõi toàn bộ hành trình từ điểm tiếp xúc đầu tiên trên Web đến hành động trong App. Đây là căn cứ để đặt mục tiêu theo tuần và tháng, xác định điểm nghẽn và phân bổ nguồn lực giữa các Hub.

**Objective 4, Stable Infrastructure Operations:** Vận hành hạ tầng ổn định, bảo mật và tuân thủ tiêu chuẩn ITC.

- Chuyển AWS sang FPT Cloud hoàn tất 100%: 36/36 Frontend, 11/11 Backend, 3/3 Database và 137 endpoint, không rollback, không downtime. Chuyển đổi diễn ra ngày 21-22/07/2026.
- Mobase V2 là Design System chuẩn thương hiệu MoMo, là Single Source of Truth cho toàn bộ Web Product. Đang mở rộng sang AI-Legible Design System.
- Quản lý 69 dự án GitLab, hoàn thiện bản vá Clickjacking, đảm bảo tuân thủ ITC.
- Boilerplate Source Code V1 chuẩn hóa quy trình phát triển Mini Web, rút ngắn thời gian khởi tạo dự án mới.
- Technical SEO: xử lý khoảng 8.600 URL giá trị thấp hoặc không có lưu lượng, tối ưu Crawl Budget, bổ sung sameAs Schema cho Organization để tăng nhận diện thực thể trên AI engine.

### 1.4. Đánh giá 8 sáng kiến theo hai hoạt động

| Initiative | Nhóm | Mục tiêu | Kết quả 2026 | Yếu tố thành công / thất bại | Khuyến nghị |
| :--- | :--- | :--- | :--- | :--- | :--- |
| Cloud Migration (AWS sang FPT Cloud) | Productivity | Chuẩn hóa hạ tầng theo chuẩn MoMo, tối ưu chi phí, tuân thủ data residency | Go-Live 21-22/07/2026; 36/36 FE, 11/11 BE, 3/3 DB; 137 endpoint; 0 rollback | Kế hoạch cutover chi tiết, Smoke Test trước và sau cutover, cutover ban đêm | Scale và tiếp tục: chuyển sang vận hành ổn định trên FPT Cloud |
| MoSpark / Admin Panel | Transformation | Nền tảng CMS thế hệ mới, hỗ trợ AI trong sản xuất nội dung và ứng dụng | Ra mắt trên Production; module GenAI sinh nội dung theo chuẩn brand | Đầu tư Next.js, Supabase, Refine; nhu cầu tự tạo Landing Page của PM/PO rõ ràng | Scale: định hướng thành CMS duy nhất cho nội dung, quảng cáo và analytics |
| Identity Platform (Authen, Deep-link, ROI Tracking) | Transformation | Định danh người dùng trên Web (SSO) và đo ROI Web-to-App | Hoàn thiện spec kỹ thuật; đưa core định danh đa nền tảng lên Production | Phụ thuộc phối hợp với User Growth và ITC để thống nhất kiến trúc | Tiếp tục: phân tích hành vi người dùng đa nền tảng |
| Umami Internal Tracking và Dashboard | Productivity | Tracking nội bộ độc lập với GA4, đối chiếu chéo và dashboard theo từng Project | Vận hành song song với GA4; dashboard theo Project phục vụ SEO Inventory | Chủ động dữ liệu, real-time hơn; đổi lại cần vận hành và bảo trì hạ tầng | Tiếp tục: mở rộng dashboard cho toàn bộ Mini Web, làm nguồn đối chiếu chính với GA4 |
| Utility Tools và Boilerplate (UI Kit, Component Library) | Productivity | Chuẩn hóa component dùng chung, rút ngắn thời gian phát triển Mini Web | Payment Component, Lead Form, JSON Form Builder, Boilerplate, UI Kit cho hàng chục Mini Web | Đồng bộ Tech Stack ITC; áp dụng JTBD trước khi xây module | Tiếp tục: mở rộng thư viện theo nhu cầu Cell Team |
| Hub mới (Phạt Nguội, Merchant, Cinema, Financial, Vehicle, Student) | Incubator | Tăng lưu lượng Out-App bằng tiện ích và nội dung ngách theo nhu cầu tìm kiếm thực tế | Ra mắt thêm nhiều Mini Web ngách trong 2026 | Bám sát nhu cầu tìm kiếm của người dùng chưa dùng MoMo | Scale các Hub có lưu lượng tốt; tiếp tục thử nghiệm các Hub còn lại |
| Chatbot AI và RAG Knowledge Base | Incubator | Trợ lý AI tra cứu thông tin dịch vụ, giảm bounce rate, tăng chuyển đổi | Module Chatbot và RAG Pipeline triển khai giới hạn trên Production | Chất lượng dữ liệu huấn luyện từ nội dung Web; giảm tải hỗ trợ thủ công | Tiếp tục thử nghiệm, đánh giá mở rộng phạm vi 2027 |
| Vận hành Mini Web hiện hữu (Vé máy bay, Vay nhanh, BHOT, Bus, Travel, Sim, CVS, Soundbox...) | Performance | Duy trì ổn định, đảm bảo uptime, hỗ trợ Cell Team | Toàn bộ Mini Web trong phạm vi Go-Live đạt 100% Smoke Test trên Production | Quy trình bảo trì định kỳ, SLA hỗ trợ rõ ràng | Tiếp tục hỗ trợ Cell Team theo tiêu chuẩn chất lượng ITC |

### 1.5. Thách thức và bài học

**Thách thức 1: Chuyển dịch từ Engineer Team sang Growth Unit.**
- Bài học: chuyển đổi vai trò phải đi kèm chuyển đổi KPI. Khi team được đánh giá bằng lưu lượng, lượt cài đặt và MAU thay vì số tính năng đã giao, tư duy thay đổi theo. Cần milestone rõ ràng và kết quả thực tế để team thấy giá trị của hướng đi mới.

**Thách thức 2: Organic chưa bền vững.**
- Số liệu: tổng lưu lượng T10/2026 giảm 8,9% MoM sau khi cắt Paid (T9 3,95M PageView, T10 3,60M PageView). Organic Search chỉ tăng 5,7% MoM, Non-Paid bù 52% phần Paid giảm. Tăng trưởng dựa vào Paid và Direct không bền vững về chi phí dài hạn, trong khi Organic mới là lợi thế cốt lõi của Web Platform.
- Bài học: SEO/GEO cần đầu tư sớm và liên tục, không phải khi lưu lượng đã giảm. Phạt Nguội là case study thuyết phục nhất: 28 ngày đầu với đúng chiến lược từ khóa đã tạo lưu lượng Organic bền vững và 660 trích dẫn từ AI. Đây là playbook cần nhân rộng cho các Hub.

**Thách thức 3: Phối hợp với BUs chưa chuẩn hóa.**
- Số liệu: trong H1/2026, mỗi dự án có cách làm khác nhau. Điểm nghẽn nằm ở khâu bàn giao dữ liệu nghiệp vụ, API, duyệt nội dung và pháp chế từ phía BU.
- Bài học: SOW và RACI rõ ràng từ đầu là điều kiện tiên quyết. Vehicle Hub và Cinema Hub áp dụng bảng RACI chi tiết và Sprint Planning 2 tuần, phối hợp tốt hơn rõ rệt. Đây sẽ là chuẩn bắt buộc cho các dự án chiến lược trong H2/2026.

**Thách thức 4: AI Search và xu hướng Zero-Click.**
- Số liệu: AI Search (ChatGPT, Gemini, Perplexity) trả lời trực tiếp nhiều câu hỏi mà không cần người dùng nhấp vào website. Nội dung tĩnh, thiếu chiều sâu ngày càng mất lưu lượng. Phân tích nội bộ cho thấy AI Search đang làm giảm lượt nhấp vào bài viết kiến thức chung.
- Bài học: GEO đã là thực tế. 660 trích dẫn từ AI và lưu lượng từ ChatGPT của Phạt Nguội là bằng chứng. llms.txt, Schema markup và Topical Authority là 3 hạng mục cần đầu tư xuyên suốt H2/2026.

---

## PHẦN 3: 2027 DIRECTION

### North Star 2027

**North Star: lượt cài đặt App từ Web (Install).** Chỉ số này đo trực tiếp đóng góp của Web vào tăng trưởng người dùng mới. Web Platform theo dõi từ T5/2026.

- **Mục tiêu:** 20.000-30.000 lượt mỗi tháng, khoảng 300.000 lượt cả năm 2027 (tháng 10/2026: 11.143).
- **Đầu vào:** PageView 63,49M cả năm 2027, gồm Paid 7,92M và Non-Paid 55,57M (mục 3.6).

### 3.1. Thị trường và cơ hội

Thị trường tìm kiếm đang chuyển từ tìm theo từ khóa sang khám phá bằng AI theo ý định. Web Platform cần chinh phục đồng thời hai xu hướng:

- **Google (tìm kiếm truyền thống):** vẫn chiếm phần lớn lưu lượng. SEO Inventory theo dõi 179,3 triệu lượt tìm kiếm mỗi tháng; nhóm lớn nhất là Giá vàng (65,8 triệu) nhưng SoV của MoMo mới 0,03%.
- **GEO/AEO (ChatGPT, Gemini, Perplexity):** tăng nhanh. Người dùng hỏi AI về tư vấn tài chính, so sánh dịch vụ và tra cứu thông tin.

**Ba khoảng trống lớn nhất MoMo chưa khai thác** (quy mô theo SEO Inventory, khác với phạm vi 117,2 triệu lượt ở mục 1.2):

| Nhóm | Lượt tìm kiếm mỗi tháng | Impression MoMo (Google Search, T10) | SoV (Impression / lượt tìm kiếm) |
| :--- | :---: | :---: | :---: |
| Giá vàng và đầu tư | 65,8 triệu | 20.053 | 0,03% |
| Tỷ giá và ngoại tệ | 11 triệu | 791.963 | 7,2% |
| Vay tiêu dùng và tín dụng | Hơn 3 triệu | 1.087.671 | Tối đa 36% |
| Giao thông và phương tiện | 23,2 triệu | 1.973.851 | 8,5% |
| Điện ảnh và giải trí | Hơn 9 triệu | 10.951.659 | Trên 100% |

SoV = Impression của MoMo trên Google Search chia cho lượt tìm kiếm thị trường. Lượt tìm kiếm lấy từ SEO Inventory theo tập từ khóa đang theo dõi, nên Impression có thể vượt 100%.

**Chiến lược theo 3 tầng ý định:**
- **Tầng 1, lưu lượng Evergreen (đầu phễu):** khai thác nhu cầu tra cứu hằng ngày (giá vàng, tỷ giá, giá xăng, lịch chiếu rạp) để tiếp cận người dùng với chi phí bằng 0 và tạo thói quen quay lại.
- **Tầng 2, công cụ tương tác (giữa phễu, PLG):** thay bài viết tĩnh bằng công cụ tính lịch trả nợ, mô phỏng hạn mức tín dụng, tra cứu phạt nguội. Người dùng tự đánh giá điều kiện trước khi nộp hồ sơ, giảm rớt phễu trong App.
- **Tầng 3, kêu gọi hành động (cuối phễu, Web-to-App):** đưa nút mở App và điều hướng sâu vào trang giao dịch trong App. Mục tiêu W2A CTR từ 4,5% trở lên.

**Theo dõi xu hướng 1-2 năm: tìm kiếm theo mục tiêu và hành trình**
- Google AI Mode tách một câu hỏi thành nhiều câu hỏi phụ, mỗi câu có một ý định riêng (query fan-out, [nguồn](https://www.aleydasolis.com/en/ai-search/google-query-fan-out/)).
- Intent graph (mục tiêu gốc, mục tiêu phụ, điều kiện) mới là hướng nghiên cứu, chưa phải hệ thống chính thức của Google, nên chưa dùng làm căn cứ kế hoạch.
- Hệ quả: thứ hạng từ khóa không còn đủ. Theo SEOClarity, nguồn AI trích dẫn có thể không trùng với kết quả đứng đầu ([nguồn](https://www.seoclarity.net/ai-mode-rankings-overlap)). Web cần phủ nhiều câu hỏi phụ của một chủ đề.
- Thử nghiệm 2027: chọn một cụm (ví dụ CIC), đo tỷ lệ được trích dẫn trên các câu hỏi phụ, tách khỏi thứ hạng; báo cáo go/no-go cuối mỗi quý.

### 3.2. Tiền đề kế thừa từ 2026

- **Web tạo giao dịch có GMV:** Cinema 15,91 tỷ đ GMV từ luồng Web-to-App trong 10 tháng; BHYT 2.643 người mua, 86% chốt ngay trên Web; eSIM du lịch 824 giao dịch, 160,4 triệu đ GMV; VCX 71 đơn, khoảng 462 triệu đ GMV. 2027 cần đặt mục tiêu GMV theo từng sản phẩm.
- **Web tạo người dùng chất lượng:** lượt cài đặt từ Web tăng liên tục 3 tháng gần nhất. 2027 Web Platform cam kết Business Metrics, không chỉ Web Metrics.
- **Công cụ tương tác hơn nội dung tĩnh:** CIC Simulator tăng 7 lần trong 3 tháng, Phạt Nguội đạt CTR 24,3%, blog tĩnh giảm đều. 2027 áp dụng Utility-first cho toàn bộ Hub.
- **GEO là kênh mới:** 660 trích dẫn từ AI; ChatGPT chiếm 95,6% lưu lượng GEO tháng 10. Web Platform đã có playbook, 2027 mở rộng.

### 3.3. Bốn trọng tâm chiến lược 2027

**Trọng tâm 1: MoSpark Platform (từ công cụ nội bộ thành nền tảng phục vụ BU)**
- **Module:** Landing Page Builder, GenAI Content Pipeline, PLG Project Engine, Ads Manager, Chatbot và Knowledge Base.
- **GenAI Content Pipeline:** hiện tự động khoảng 80% quy trình nội dung SEO/GEO (nghiên cứu từ khóa, dàn ý theo E-E-A-T, xuất bản), rút từ nhiều ngày xuống vài giờ. 2027 mở rộng cho Cell Teams, rút xuống vài phút, có AI Quality Gate chấm điểm trước khi xuất bản.
- **Chatbot AI và Knowledge Base:** từ thử nghiệm giới hạn sang mở rộng phạm vi, giúp tra cứu thông tin dịch vụ, giảm thoát trang và tăng chuyển đổi.
- **Ads Manager:** quản lý banner và quảng cáo trên Web ngay trong MoSpark, hỗ trợ các hạng mục của Trọng tâm 3.
- **Hạ tầng và sức khỏe Web:** FPT Cloud ổn định, uptime từ 99,9%; Core Web Vitals đạt ngưỡng; quản trị URL và index rate từ 80% sau 30 ngày; đối soát GA4 và Umami hằng tháng; bảo mật và quản trị mã nguồn (mục 3.7).

**Trọng tâm 2: SEO/GEO cho Strategic Project (3 Hub)**
- **Cinema Hub:** tái cấu trúc sang MoSpark, Native Web Payment, mở rộng OTT. Mục tiêu Top 3 SEO và GEO cho từ khóa điện ảnh.
  - Review và rating trên trang phim, trang rạp để kéo tìm kiếm "review phim" về trang đặt vé.
  - Landing page theo phim, suất chiếu, deal độc quyền, dựng trong 24-48 giờ trên MoSpark.
  - Trang đặt vé nhóm (Group Sale).
  - Nội dung từ người dùng và ambassador để làm mới trang phim.
  - Đo funnel từ khám phá, review, chọn suất đến thanh toán trên từng trang.
  - Dẫn người xem lịch chiếu chưa có App sang cài đặt và liên kết ngân hàng.
- **Financial Hub:** công cụ quản lý tài sản, phễu CIC → VTS → Vay Nhanh, GEO tài chính. Mục tiêu Top 3 cho từ khóa tài chính cá nhân trọng điểm và tăng SoV.
- **Vehicle Hub:** mở rộng pSEO theo nhu cầu tìm kiếm, hoàn thiện hồ sơ phương tiện, bán chéo bảo hiểm. Mục tiêu 5% SoV trên thị trường 23,2 triệu lượt tìm kiếm.
- **GEO dùng chung cho ba Hub:** bổ sung Schema, llms.txt và uy tín chủ đề cho toàn bộ Hub. Mục tiêu 100.000 PageView mỗi tháng từ AI vào T12/2027 (T10/2026: 18.164; T11 MTD 1-16/11: 25.340).
- **Đo lường:** theo dõi Impression (Google Search) và SoV theo từng Hub hằng tháng.

**Trọng tâm 3: New User Engine và Web-to-App (từ thử nghiệm sang tăng trưởng có hệ thống)**
- Balloon Ads 2026 đã thử nghiệm. 2027 xây thành hệ thống:
  - Personalized Promotion Schema theo Hub và phân khúc người dùng.
  - Web Product "thử trước, cài sau": trải nghiệm 50-60% giá trị MoMo ngay trên Web.
  - Retargeting Ads: nhắc người dùng bỏ dở luồng mua (vé, eSIM, bảo hiểm) để hoàn tất giao dịch.
  - Contextual Ads: CTA theo nội dung trang, như nút đặt vé ở trang lịch chiếu, nút vay ở trang tra cứu khoản vay.
  - Personalization theo trạng thái: chưa cài đặt, đã cài chưa đăng ký, đã đăng ký chưa liên kết ngân hàng; mỗi nhóm có thông điệp riêng.
- **Theo dõi người dùng từ Web sang App:** Identity Platform nối hành vi từ lúc xem trang đến cài đặt và dùng App, để đo hiệu quả từng kênh và cá nhân hóa. Đăng nhập (SSO) trên Web để đối chứng và ghi nhận Lead Activation, sau khi Legal phê duyệt hoặc hoàn tất xin giấy phép.
- **Công cụ tương tác và gamification:** bổ sung cơ chế gamification trên Web (ví dụ gamification Điểm Tín Dụng CIC, game Một Mùa Quýt đã có 7.097 người tham gia) để tăng Engagement, Time on Site và giảm Bounce Rate. Triển khai sau khi Legal xác nhận gamification có cần giấy phép hay không.

**Trọng tâm 4: Shared-Product for Self-Served**

Phục vụ các Cell Teams có nhu cầu xây dựng sản phẩm và business model trên Web nhưng không nằm trong định hướng ưu tiên của Web Platform.
- **Mô hình:** Cell Teams tự xây và tự vận hành (ví dụ HR với MoMo Talent và MoMo Career, L&D của Product, BMC); Web Platform cung cấp sản phẩm dùng chung và chuẩn kỹ thuật, không làm trực tiếp.
- **Sản phẩm dùng chung:** Payment Component, Lead Form, JSON Form Builder, Boilerplate, UI Kit, cùng Landing Page Builder và GenAI Content Pipeline trên MoSpark.
- **Điều kiện:** Permission System, mô hình self-serve giữa Cell Teams và Web Platform, Quality Gate tự động.
- **Mục tiêu:** 20 Cell Teams được hỗ trợ trong 2027 (hiện 16).

### 3.4. Mô hình vận hành 2027

Mỗi bên có một phần trách nhiệm riêng:

- **Web Platform:**
  - Nền tảng: vận hành MoSpark (Landing Page Builder, GenAI Content Pipeline, PLG Project Engine, Ads Manager, Chatbot và Knowledge Base) và momo.vn trên hạ tầng FPT Cloud.
  - Đo lường: duy trì Identity Platform, OneLink, tracking GA4 và Umami, dashboard theo từng Project.
  - Phát triển: đồng hành xây 2-3 Hub ưu tiên (mục 3.3); tư vấn kiến trúc cho Cell Teams tự xây trên Self-Served Platform.
  - Chuẩn kỹ thuật: Mobase Design System, Boilerplate, UI Kit và Quality Gate tự động trước khi xuất bản.
  - Vận hành: uptime từ 99,9%, Core Web Vitals đạt ngưỡng, bảo mật và quản trị mã nguồn (mục 3.7).
- **Out-App Traffic:** chịu trách nhiệm sức khỏe nền tảng (SEO kỹ thuật, index và chất lượng URL), tăng trưởng PageView, thứ hạng tìm kiếm và hoạt động Off-page. Nghiên cứu nhu cầu tìm kiếm, thiết kế phễu và quản lý ngân sách Off-site. Gói cơ sở là tư vấn Content và SEO/GEO cho mọi Hub. Gói mở rộng cấp nguồn lực chuyên trách cho Hub đáp ứng đủ ba điều kiện: BU cam kết KPI, cam kết ngân sách và có RACI rõ ràng.
- **BU (Cell Teams):** chịu trách nhiệm doanh thu, quảng cáo trả phí và duyệt nội dung chuyên môn. Báo trước các thay đổi lớn về sản phẩm và chính sách để Web chuẩn bị nội dung và hạ tầng.
- **Self-Served Platform:** Cell Teams như BMC, HR (MoMo Talent, MoMo Career) và L&D của Product tự xuất bản trang không cần Dev qua MoSpark; Quality Gate tự động chấm điểm nội dung.

### 3.5. Đầu tư 2027 và cơ chế giải ngân

**Ngân sách đề xuất:** 1.995.800.000 đ, khoảng 166,3 triệu đ mỗi tháng, gồm 1,95 tỷ đ cho 3 dự án và 45,8 triệu đ bản quyền công cụ. Web Platform không đề xuất ngân sách Paid. Ngân sách của Cinema và Financial không do GPD chi trả toàn bộ: một phần đến từ BU tương ứng, tỷ lệ đồng tài trợ thống nhất với từng BU trước khi giải ngân.

| Dự án | Ngân sách | PageView 2026 | PageView 2027 | PageView tăng thêm | Kết quả kinh doanh kỳ vọng | Chi phí đơn vị |
| :--- | :---: | :---: | :---: | :---: | :--- | :--- |
| **Cinema Hub** | 620 triệu đ | 9,1M (thực tế T1-T10) | 12,6 - 14,0M | 3,5 - 4,9M | Thêm 31 - 43 nghìn đơn hàng; 6,3 - 8,8 tỷ đ GMV | 130 - 180 đ/PageView; 1 đồng chi phí tạo 10,2 - 14,2 đồng GMV |
| **Financial Hub, CIC và Tín dụng** | 480 triệu đ | 0,42M (thực tế T1-T10) | 2,2 - 2,5M | 1,8 - 2,1M | 52 - 61 nghìn lượt mở App vào kiểm tra CIC, Vay Nhanh trên App | 230 - 270 đ/PageView; 7.900 - 9.200 đ/lượt mở App |
| **Financial Hub, Tích lũy và Đầu tư** | 850 triệu đ | 0,21M (thực tế T1-T10) | 1,0 - 1,5M | 0,8 - 1,3M | 32 - 52 nghìn lượt mở App vào Túi Sinh Lời, Tiết kiệm, Chứng chỉ quỹ | 650 - 1.060 đ/PageView; 16.300 - 26.600 đ/lượt mở App |
| **Bản quyền công cụ** | 45,8 triệu đ | | | | Figma Professional 9,8 triệu đ (2 người dùng); Semrush Pro 36 triệu đ (1 người dùng) | Phục vụ vận hành |
| **Tổng** | **1,996 tỷ đ** | **9,7M** | **15,8 - 18,0M** | **6,1 - 8,3M** | **6,3 - 8,8 tỷ đ GMV Cinema; 84 - 113 nghìn lượt mở App Financial** | **240 - 330 đ/PageView; 390 - 530 đ/phiên** (Paid SEM quy đổi: khoảng 1.235 đ/PageView) |

**Giả định tính toán:**
- Cinema dùng tỷ lệ thực tế 10 tháng 2026 trên baseline 9.098.856 PageView: 1.000 PageView tạo khoảng 19,1 vé và 8,8 đơn hàng. Đơn vị GMV là đơn hàng × AoV 205.000 đ (1 đơn trung bình khoảng 2,17 vé, nên không dùng số vé để tính GMV), tương đương khoảng 1,80 triệu đ GMV trên 1.000 PageView. Chưa tính phần tăng thêm nếu triển khai thanh toán QR trên Web.
- Financial dùng tỷ lệ mở App thực tế 10 tháng 2026 theo GA4: CIC và Tín dụng !!2,9%!!, Tích lũy và Đầu tư 4,0%. Để quy ra GMV, Financial Services BU cung cấp tỷ lệ từ lượt mở App sang hồ sơ vay hoặc tài khoản tích lũy.
- Baseline PageView 2026 theo GA4 T1-T10 (all channels, page-level): cụm CIC và Tín dụng đạt khoảng 417 nghìn PageView theo phạm vi CIC (diem-tin-dung + nội dung tín dụng, không gồm Vay Nhanh và Ví Trả Sau), cụm Tích lũy và Đầu tư đạt khoảng 210 nghìn PageView (tiết kiệm, chứng khoán, chứng chỉ quỹ, quản lý chi tiêu + nội dung đầu tư). Đây là số 10 tháng, không ngoại suy.
- Quy đổi sang phiên theo tỷ lệ Organic 1,62 PageView trên mỗi phiên (GA4 10 tháng 2026), để so sánh cùng đơn vị với giá thầu Paid SEM tính theo lượt nhấp.

**Mức tăng khi có đầu tư (3 dự án):**

| Chỉ số | Mức 2026 | Tăng thêm khi có đầu tư |
| :--- | :---: | :---: |
| PageView (3 dự án) | 9,7M | +63-86% |
| Ticket order Cinema (đơn đặt vé) | 80 nghìn | +39-54% |
| GMV Cinema | 16,4 tỷ đ | +38-54% |
| Lượt mở App từ Financial | khoảng 21 nghìn | +400-540% |

- Kịch bản không đầu tư giả định 3 cụm giữ nguyên lưu lượng 2026. Thực tế lưu lượng dễ giảm do AI Search, nên chênh lệch thực có thể lớn hơn.
- Cùng lượng truy cập tăng thêm, mua qua Paid SEM tốn 7,5-10,2 tỷ đ mỗi năm và mất ngay khi dừng chi tiêu (giá thầu thấp nhất 2.000 đ/click). Đầu tư nội dung tốn 1,95 tỷ đ và lưu lượng tiếp tục ở lại các năm sau.

**Financial Hub giải ngân 2 đợt (tổng 1,33 tỷ đ):**
- **Đợt 1 (Q1-Q2/2027), 540 triệu đ:** CIC và Tín dụng 240 triệu đ; Tích lũy và Đầu tư 300 triệu đ. Mục tiêu chứng minh chuyển đổi trước khi mở rộng.
- **Đợt 2 (Q3-Q4/2027), 790 triệu đ:** chỉ giải ngân khi cuối Q2 đạt đủ 3 ngưỡng:
  - PageView đạt ít nhất 80% KPI của 2 quý.
  - Tỷ lệ mở App không thấp hơn mức 2026 (CIC và Tín dụng 2,9%; Tích lũy và Đầu tư 4,0%).
  - Financial Services BU đã cung cấp tỷ lệ từ lượt mở App sang hồ sơ vay hoặc tài khoản tích lũy.
- **Không đạt ngưỡng:** dừng đợt 2 của dự án không đạt, chuyển ngân sách sang Cinema Hub (đã chứng minh được GMV) hoặc hoàn lại.

**Cơ chế giải ngân chung:** giải ngân theo quý. Dự án đạt dưới 80% KPI PageView và lượt mở App của quý sẽ được điều chỉnh hoặc chuyển ngân sách sang dự án khác.

### 3.6. Mục tiêu lưu lượng 2027 theo tháng

Mục tiêu 63,49M PageView, chia theo tháng theo kế hoạch ngân sách. Giả định: Paid giữ nguyên mức 2026 (7,92M, khoảng 0,66M mỗi tháng); phần tăng còn lại là Non-Paid.

| Tháng | Tổng PageView (triệu) | Paid (triệu) | Non-Paid (triệu) | Cài đặt mới (nghìn) |
| :--- | :---: | :---: | :---: | :---: |
| T1/2027 | 4,12 | 0,66 | 3,46 | 20,0 |
| T2/2027 | 4,45 | 0,66 | 3,79 | 20,9 |
| T3/2027 | 4,35 | 0,66 | 3,69 | 21,8 |
| T4/2027 | 4,52 | 0,66 | 3,86 | 22,7 |
| T5/2027 | 4,80 | 0,66 | 4,14 | 23,6 |
| T6/2027 | 5,10 | 0,66 | 4,44 | 24,5 |
| T7/2027 | 5,25 | 0,66 | 4,59 | 25,5 |
| T8/2027 | 5,45 | 0,66 | 4,79 | 26,4 |
| T9/2027 | 5,75 | 0,66 | 5,09 | 27,3 |
| T10/2027 | 6,15 | 0,66 | 5,49 | 28,2 |
| T11/2027 | 6,55 | 0,66 | 5,89 | 29,1 |
| T12/2027 | 7,00 | 0,66 | 6,34 | 30,0 |
| **Cả năm** | **63,49** | **7,92** | **55,57** | **300,0** |

Cài đặt mới tăng đều từ 20.000 (T1) lên 30.000 (T12), khớp KPI mục tiêu. Tương đương khoảng 0,4-0,5% PageView kế hoạch, cao hơn mức 0,31% của tháng 10/2026.

So với 2026 (ước cả năm: tổng 40,69M, Paid 7,92M, Non-Paid 32,77M), mục tiêu Non-Paid tăng 22,80M (+70%), tương đương bình quân khoảng 5,7% mỗi tháng từ T1 đến T12/2027.

Non-Paid được đặt theo tốc độ tăng trưởng, không theo tỷ trọng, vì Paid do BU quyết định và thay đổi theo từng tháng nên không thuộc cam kết của Web Platform. Bảng trên giả định Paid giữ nguyên 7,92M và tháng 12/2026 đạt 4,00M PageView (Phụ lục A). Mức tăng Non-Paid chỉ đạt khi có đầu tư và chiến lược rõ ràng từ cả hai bên: Web Platform triển khai nội dung, công cụ và tối ưu trang (mục 3.3); BU đầu tư, phối hợp và cung cấp dữ liệu (mục 3.4 và 3.5).

| Chỉ số | 2026 | Mục tiêu 2027 | Ghi chú |
| :--- | :---: | :---: | :--- |
| Lượt cài đặt mới mỗi tháng | 11.143 (T10) | 20.000 - 30.000 | |
| PageView từ AI mỗi tháng | 18.164 (T10); 25.340 (1-16/11) | 100.000 vào T12/2027 | Kênh AI Assistant trên GA4; ChatGPT chiếm khoảng 97% |
| Lưu lượng CIC và Tích lũy | 0,63M (T1-T10 thực tế) | 3,2 - 4,0M cả năm | Tương đương khoảng 0,3M PageView mỗi tháng |
| Cell Teams được hỗ trợ | 16 | 20 | Trong đó tự vận hành qua MoSpark CMS |
| Strategic Hubs đang hoạt động | 3 (Cinema, Vehicle, Financial) | 5 trở lên | |

**Rủi ro:**
- **Lưu lượng Non-Paid không có ngân sách:** để đạt 55,57M PageView Non-Paid, ba dự án có ngân sách chỉ đóng góp khoảng 6,1-8,3M PageView (giả định phần tăng này là Non-Paid). Phần còn lại, khoảng 14,5-16,7M PageView Non-Paid, nằm ngoài các dự án được cấp vốn và chưa có kế hoạch riêng. Phần tăng Non-Paid chủ yếu đến từ Organic và người dùng quay lại (Direct), cần chỉ số retention để kiểm chứng. Organic đang tăng 5,7% MoM, nên mức tăng Non-Paid đòi hỏi cải thiện rõ so với xu hướng tháng 10.
- **Paid do BU quyết định:** bảng giả định Paid giữ nguyên 7,92M. Nếu BU chạy thêm Paid, tổng PageView tăng nhưng mục tiêu Non-Paid không đổi.
- **AI Search:** tiếp tục làm giảm lượt nhấp vào bài viết kiến thức chung. Cần bù bằng công cụ tương tác và dữ liệu thời gian thực.

**Điều kiện từ BU:**
- Movies BU và Financial Services BU chia sẻ lịch phim, lộ trình sản phẩm và thay đổi chính sách trước 2-4 tuần.
- Financial Services BU cung cấp tỷ lệ chuyển đổi trên App (hồ sơ vay, tài khoản tích lũy) và đối soát qua Dashboard dùng chung.
- Movies BU thống nhất lộ trình thanh toán QR ngay trên Web trong 6 tháng đầu năm 2027, để giảm tỷ lệ bỏ dở trên 90%.

### 3.7. Điều kiện kỹ thuật, pháp lý và SEO kỹ thuật

Mỗi Hub chỉ Go-live khi đáp ứng các điều kiện sau:

| Nhóm | Yêu cầu | Ngưỡng nghiệm thu | Đơn vị phụ trách |
| :--- | :--- | :--- | :--- |
| Hạ tầng | Vận hành hạ tầng FPT Cloud ổn định, triển khai không gián đoạn | Uptime từ 99,9%; smoke test trước và sau mỗi lần triển khai | Web Platform Engineering |
| Hạ tầng | Đo lường Web-to-App đầy đủ: Identity Platform, OneLink, tracking GA4 và Umami | 100% liên kết mở App chuẩn hóa OneLink; số liệu đối soát hằng tháng | Web Platform Engineering |
| Kỹ thuật | Core Web Vitals đạt ngưỡng trước Go-live | LCP dưới 2,5 giây; INP dưới 200 ms; CLS dưới 0,1 | Web Platform Engineering |
| Kỹ thuật | Quality Gate tự động trước khi xuất bản trên MoSpark | Chấm điểm SEO/GEO, Schema và an toàn thương hiệu trước khi publish | Web Platform (MoSpark) |
| Kỹ thuật | Bảo mật và quản trị mã nguồn | Bản vá bảo mật hoàn tất; 69 dự án GitLab quản trị theo chuẩn ITC | Web Platform Engineering |
| Kỹ thuật | Giao diện theo chuẩn Mobase Design System | 100% trang dùng component Mobase, không hardcode màu và khoảng cách | Web Platform Engineering |
| Pháp lý | Thông tin giấy phép hoạt động, biểu phí và kênh khiếu nại công khai trên trang tài chính | Đủ trước Go-live của từng trang Financial | Financial Services BU, Legal |
| Pháp lý | Tác giả có tên (named author) cho nội dung tài chính thuộc nhóm YMYL | Theo chính sách; hiện đang chặn triển khai GEO/AEO cho nội dung tài chính | Legal, Content |
| Pháp lý | Duyệt pháp lý trang so sánh sản phẩm trước khi publish | Hoàn tất trước khi xuất bản; thời gian duyệt ghi trong SOW | Legal, BU liên quan |
| Pháp lý | Đăng nhập (SSO) trên Web và cơ chế gamification | Legal phê duyệt hoặc hoàn tất xin giấy phép trước khi triển khai | Legal, Web Platform |
| SEO kỹ thuật | Foundation Checklist là cổng bắt buộc trước khi publish | 100% trang đạt checklist; QA xác nhận trước Go-live | Out-App Traffic, Web Platform |
| SEO kỹ thuật | Quản trị URL theo 4 cấp: nofollow và loại khỏi sitemap, 308, 410, cập nhật nội dung | Mọi URL giá trị thấp có quyết định xử lý trong quý | Out-App Traffic |
| SEO kỹ thuật | Schema, sitemap và llms.txt | Schema JSON-LD và llms.txt trên các Hub chính; nộp sitemap sau mỗi lần ra mắt | Web Platform, Out-App Traffic |
| SEO kỹ thuật | Tỷ lệ index trang mới | Index rate từ 80% sau 30 ngày với template library | Out-App Traffic |

### 3.8. Định hướng 2027 theo sản phẩm

Năm 2027, Web tập trung tối ưu chuyển đổi qua thanh toán và tiếp cận người dùng chưa có App nhưng có nhu cầu, qua các dịch vụ trên Web, để tạo lượt cài đặt và MAU.

| Sản phẩm | Định hướng 2027 | KPI |
| :--- | :--- | :--- |
| Cinema Hub | Thanh toán quét mã QR trực tiếp trên Web, không bắt buộc tải App trong H1/2027 | Tỷ lệ hoàn tất giao dịch trên Web; tỷ lệ bỏ dở ở bước mua vé |
| BH thân vỏ (VCX) | Tối ưu trang chuyển đổi từ lead sang đơn | Tỷ lệ lead sang đơn từ 3,3% lên 7-10% |
| BH xe máy (XMBB) | Khôi phục lưu lượng tự nhiên và tăng thanh toán trực tiếp trên Web | Lưu lượng so với cùng kỳ; số đơn thanh toán trên Web |
| BHYT | Giữ luồng thanh toán trực tiếp trên Web | Tỷ lệ đơn chốt trên Web |
| Vé xe, eSIM du lịch, Sim chính chủ | Tiếp cận người dùng chưa có App nhưng có nhu cầu, dẫn vào luồng cài đặt và đăng ký | Lượt cài đặt và MAU từ nhóm dịch vụ này; mục tiêu đặt sau khi có số liệu nền |

### 3.9. Chỉ số cần cải thiện trong 2027

| Chỉ số | Hiện trạng | Đánh giá | Hành động cải thiện | Phụ trách |
| :--- | :---: | :--- | :--- | :--- |
| Tỷ lệ cài đặt sang đăng ký | 35,0% (T10) | Bước rớt lớn nhất, khoảng 65% người cài chưa đăng ký | Đưa bước đăng ký ngay sau khi cài đặt; đo tỷ lệ theo từng nguồn cài đặt | Web Platform, Out-App Traffic |
| Tăng trưởng Organic Search | +5,7% MoM (T10) | Thấp hơn tăng trưởng Non-Paid tổng (+13,5%) | Tăng nội dung có công cụ tương tác và Schema; theo dõi trích dẫn từ AI | Out-App Traffic |
| Tốc độ tăng Financial Hub | Cần tăng 3,7 lần để đạt 1M PageView mỗi tháng | Mục tiêu cuối 2026 khó đạt trong hai tháng còn lại | Đặt mốc theo quý và điều chỉnh mục tiêu nếu cần | Web Platform, Out-App Traffic |
| Lead sang đơn của VCX | 3,3% | Thấp hơn mục tiêu 7-10% | Tối ưu trang chuyển đổi và thử nghiệm A/B trên luồng báo giá | InsurTech BU, Web Platform |
| Lưu lượng web XMBB | Bằng 48% cả năm 2025 (-52%) | Giảm dù đã có 10/10 từ khóa mục tiêu trong top 10 | Làm rõ nguyên nhân trước khi đầu tư thêm | Out-App Traffic |
| Tỷ lệ mở App của CIC và Tín dụng | 2,9% | Thấp hơn Tích lũy và Đầu tư (4,0%) và mục tiêu 4,5% của Tầng 3 | Tối ưu nút mở App trên trang CIC; đợt 2 yêu cầu không thấp hơn mức 2026 | Web Platform, Financial Services BU |

### Thuật ngữ

- **PageView:** số lần một trang được tải và hiển thị.
- **Non-Paid / Paid:** lưu lượng không trả phí (Organic, Direct, Referral, AI) và lưu lượng từ quảng cáo trả phí.
- **Tỷ lệ mở App (W2A CTR):** số lượt mở App từ Web chia cho PageView Web.
- **Click to App:** lượt click có đường dẫn OneLink hợp lệ từ Web để mở hoặc cài đặt App (sự kiện click_to_app).
- **Install:** lượt cài đặt App.
- **Liên kết ngân hàng (Map Bank):** người dùng liên kết tài khoản ngân hàng với MoMo.
- **MAU:** số người dùng hoạt động trong tháng có giao dịch.
- **GMV:** tổng giá trị giao dịch, tính bằng đơn hàng nhân giá trị đơn trung bình (AoV).
- **SoV (Share of Voice):** Impression của MoMo trên Google Search chia cho lượt tìm kiếm của thị trường trong cùng nhóm.
- **GEO/AEO:** tối ưu nội dung để AI tìm kiếm trích dẫn và trả lời người dùng.

---

## PHỤ LỤC

### A. Lưu lượng 2026 theo quý

| Quý | Tổng PageView | Tỷ trọng Non-Paid | Ghi chú |
| :--- | :---: | :---: | :--- |
| Q1/2026 | 9,29M | 77,4% | T2 cao điểm Tết 3,47M |
| Q2/2026 | 9,38M | 80,0% | T4 cắt giảm quảng cáo |
| Q3/2026 | 10,59M | 77,9% | T9 cao nhất năm 3,95M |
| Q4/2026 (ước tính) | 11,43M | 86,0% | T10 3,60M; T11 ước 3,83M; T12 ước 4,00M |
| **Cả năm** | **40,69M** | **80,5%** | Non-Paid 32,77M (Organic 20,15M, Direct 7,46M, AI Traffic và Referral 5,16M); Paid 7,92M |

- Giá trị thay thế quảng cáo: 20,15M PageView Organic, nếu mua qua Paid SEM với giá thầu thấp nhất 2.000 đ/click, tương đương khoảng 25 tỷ đ (GA4 10 tháng 2026: Organic đạt 1,62 PageView trên mỗi phiên, tức khoảng 12,4 triệu phiên). Đây là lưu lượng Web tự sở hữu, không mất khi dừng chi tiêu.

### B. Quy mô thị trường tìm kiếm

- 214,4 triệu lượt tìm kiếm mỗi tháng ở 5 nhóm ngành (Google Keyword Planner, Semrush): Tài chính 122,97 triệu (giá vàng 73,59 triệu, ngân hàng và lãi suất 21,62 triệu, tỷ giá 9,47 triệu), Giao thông 35,63 triệu, Giải trí và Cinema 18,68 triệu, Tiện ích đời sống 15,91 triệu, Du lịch 6,50 triệu.
- Ngân sách 2027 tập trung vào CIC, vay và hành trình tích sản (khoảng 9,4 triệu lượt mỗi tháng) thay vì giá vàng và tỷ giá, vì đây là các Theme gắn trực tiếp với sản phẩm tài chính tạo doanh thu của MoMo.
