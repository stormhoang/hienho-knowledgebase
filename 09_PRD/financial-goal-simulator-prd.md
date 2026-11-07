# TÀI LIỆU ĐẶC TẢ KỸ THUẬT & GAME DESIGN DOCUMENT (GDD)
## DỰ ÁN: FINANCIAL GOAL SIMULATOR 2.0 (ROGUE-FINTECH JOURNEY)

* **Mã tài liệu:** `GDD-FINSIM-2.0` · `FIN-SIM-MOMO-2026`
* **Loại tài liệu:** Product Requirements Document (PRD) & Game Design Document (GDD)
* **Đối tượng sử dụng:** Frontend Engineer / AI Coding Assistant (Claude, Cursor, Copilot)
* **Ngôn ngữ & Nền tảng:** TypeScript, React / Next.js (App Router), Tailwind CSS, Framer Motion, Web Audio API
* **Trạng thái:** Active / Sẵn sàng triển khai kỹ thuật
* **Phân loại chiến lược:** Financial Hub Interactive Gamification & Contextual Web-to-App Bridge

---

## 1. TỔNG QUAN DỰ ÁN & MỤC TIÊU (PROJECT OVERVIEW & OBJECTIVES)

### 1.1. Bối cảnh & Khái niệm cốt lõi (Core Concept)
Financial Goal Simulator 2.0 (FIN-SIM-MOMO-2026) là một web game tương tác kết hợp giữa mô phỏng tài chính cá nhân (Financial Simulator) và cơ chế di chuyển theo bàn cờ phân nhánh (Roguelite Journey). 

Thay vì sử dụng các câu hỏi trắc nghiệm tĩnh nhàm chán, người dùng tự đặt ra một mục tiêu đời thực (ví dụ: Chuyến đi Đà Lạt 6 triệu cuối năm 2026 với số dư ban đầu 0 đồng) và bắt đầu hành trình vượt qua 12 lượt chơi (tương ứng 12 tháng) trên một bản đồ sinh thái tài chính. Trò chơi tích hợp:
* **Hệ thống cân bằng 3 tài nguyên sống còn:** Tiền tích lũy, Năng lượng tinh thần (Hạnh phúc) và Điểm tín nhiệm (Finance Score).
* **Mini-game tương tác cơ học:** Chém hóa đơn lãng phí (Slash Expenses), kéo thả phân bổ hũ tiền.
* **Tình huống đánh đổi chiến lược:** Cân bằng giữa tiết kiệm kỷ luật và ngưỡng áp lực tài chính dẫn đến chi tiêu bù đắp quá độ (Revenge Spending).
* **Giáo dục tri thức mộc mạc:** Chuyển hóa tư tưởng của các nhà kinh tế học lỗi lạc thành châm ngôn đường phố dễ hiểu.

### 1.2. Mục tiêu kinh doanh & Chuyển đổi (Business & Conversion Goals)
* **Thời gian giữ chân trên Kênh Web (Dwell time):** Đạt trung bình 90 - 150 giây/phiên.
* **Tỷ lệ hoàn thành hành trình (Completion Rate):** > 65% lượt truy cập chơi hết 12 tháng.
* **Chuyển đổi Web-to-App:** Dẫn người dùng vào App MoMo thông qua Deeplink/OneLink để kích hoạt tính năng **Tiết Kiệm Mục Tiêu / Túi Thần Tài / Điểm Tin Cậy** với dữ liệu mục tiêu được điền sẵn 100%.

---

## 2. KIẾN TRÚC DỮ LIỆU & STATE MANAGEMENT (DATA MODELS & ENGINE)

### 2.1. TypeScript Interface Definitions

```typescript
export type GoalCategory = 'travel' | 'wedding' | 'debt' | 'study' | 'emergency';

export interface UserGoal {
  category: GoalCategory;
  name: string; // Mặc định: "Chuyến đi Đà Lạt"
  targetAmount: number; // Mặc định: 6,000,000 VND
  deadlineMonths: number; // Mặc định: 12 tháng
  currentBalance: number; // Khởi điểm: 0 VND
}

export interface PlayerStats {
  savings: number; // Số tiền tích lũy thực tế
  sanity: number; // Năng lượng Hạnh phúc / Tinh thần (0 - 100). Khởi điểm: 70
  financeScore: number; // Điểm Tin Cậy (300 - 850). Khởi điểm: 600
  streakCount: number; // Chuỗi tháng duy trì kỷ luật
  burnoutTriggered: boolean; // Trạng thái rơi vào ngưỡng áp lực dẫn đến chi tiêu bù đắp
}

export type NodeType = 
  | 'income'       // Ô thu nhập / việc làm thêm
  | 'temptation'   // Ô cám dỗ mua sắm / ăn chơi
  | 'mystery'      // Ô sự kiện ngẫu nhiên (may mắn hoặc biến cố)
  | 'tactile_game' // Ô mini-game tương tác cơ học
  | 'boss';        // Ô trùm thử thách chặng cuối (Tháng 11)

export interface JourneyNode {
  month: number;
  type: NodeType;
  title: string;
  description: string;
  quote?: {
    author: string;
    text: string;
  };
}

export interface GameEngineState {
  goal: UserGoal;
  stats: PlayerStats;
  currentMonth: number; // 1 đến 12
  isGameOver: boolean;
  gameResult: 'success' | 'delayed' | 'failed' | null;
  historyLogs: Array<{
    month: number;
    actionTitle: string;
    savingsDelta: number;
    sanityDelta: number;
    scoreDelta: number;
  }>;
}
```

### 2.2. Quy tắc Logic & Công thức toán học (Core Rules & Math)

* **Định mức tích lũy chuẩn tháng:**
  $$\text{RequiredMonthly} = \left\lceil \frac{\text{TargetAmount} - \text{CurrentBalance}}{\text{DeadlineMonths}} \right\rceil$$
* **Quy tắc Ngưỡng Áp Lực & Chi Tiêu Bù Đắp Quá Độ (Burnout & Revenge Spending):**
  * Nếu chỉ số `sanity <= 20`: Kích hoạt trạng thái Báo động Căng thẳng.
  * Nếu chỉ số `sanity <= 0`: Kích hoạt ngay lập tức biến cố **"Chi tiêu bù đắp quá độ"**:
    $$\text{SavingsPenalty} = \text{savings} \times 0.35$$
    $$\text{sanity} = 50$$
    $$\text{financeScore} = \max(300, \text{financeScore} - 40)$$
  * *Ý nghĩa:* Dạy người dùng bài học tâm lý học hành vi: Ép bản thân nhịn ăn nhịn mặc cực đoan sẽ dẫn đến đổ vỡ tài chính nghiêm trọng hơn.
* **Quy tắc Chuỗi Kỷ Luật (Discipline Streak):**
  * Duy trì nạp đủ tiền trong 3 tháng liên tiếp mà `sanity >= 40`: Kích hoạt thưởng `+20 Finance Score` và cây tài chính nở hoa rực rỡ.
* **Độ trễ mục tiêu (Projected Delay):**
  * Kết thúc tháng 12, nếu `savings < targetAmount`:
    $$\text{DelayMonths} = \left\lceil \frac{\text{TargetAmount} - \text{savings}}{\text{RequiredMonthly}} \right\rceil$$

---

## 3. THIẾT KẾ BẢN ĐỒ 12 Ô HÀNH TRÌNH (THE 12-NODE JOURNEY)

Bản đồ được chia thành 12 bước chân thời gian. Mỗi bước có bối cảnh, 2 lựa chọn chiến lược đánh đổi hoặc 1 mini-game cơ học.

### Tháng 1: Khởi động dòng tiền (Income Node)
* **Bối cảnh:** Nhận tháng lương đầu tiên. Tiền về tài khoản 10 triệu đồng.
* **Lựa chọn A (Tích lũy trước):** Cất ngay 500.000 đ vào quỹ mục tiêu, còn lại đem chi trả sinh hoạt phí.
  * *Hệ quả:* `savings: +500.000 đ`, `sanity: -5`, `financeScore: +25`.
* **Lựa chọn B (Tự thưởng trước):** Đi ăn buffet hải sản chúc mừng tháng làm việc vất vả hết 400.000 đ, phần dư mới cất.
  * *Hệ quả:* `savings: +100.000 đ`, `sanity: +25`, `financeScore: -10`.
* **Châm ngôn kinh tế (Warren Buffett):**
  > *"Cụ Buffett dặn: Lương về thì cất một góc trước rồi tiêu chỗ còn lại. Đừng đợi tiêu xả láng cả tháng rồi mới gom tiền lẻ đi cất."*

---

### Tháng 2: Cơn sốt giảm giá chớp nhoáng (Temptation Node)
* **Bối cảnh:** Trang thương mại điện tử tung mã giảm giá 50% cho một món đồ công nghệ yêu thích từ 2 triệu còn 1 triệu đồng.
* **Lựa chọn A (Bỏ qua giảm giá):** Tắt màn hình, cất 500.000 đ vào quỹ mục tiêu.
  * *Hệ quả:* `savings: +500.000 đ`, `sanity: -10`, `financeScore: +20`.
* **Lựa chọn B (Chốt đơn giảm giá):** Mua ngay vì sợ mất mã giảm giá, rút 500.000 đ từ quỹ tiết kiệm bù vào.
  * *Hệ quả:* `savings: -500.000 đ`, `sanity: +30`, `financeScore: -25`.
* **Châm ngôn kinh tế (Morgan Housel):**
  > *"Bác Morgan Housel bảo: Mua đồ giảm giá không làm bạn giàu lên, nó chỉ chứng minh bạn vừa mất thêm 1 triệu trong ví. Giàu có là số tiền bạn giữ được trong tài khoản, không phải đống đồ hiệu treo trong tủ."*

---

### Tháng 3: Mini-Game "Chém Hóa Đơn Thừa" (Tactile Node 1)
* **Cơ chế chơi:** Màn hình xuất hiện hiệu ứng vuốt chém (Swipe to slash). Trong vòng 5 giây, các hóa đơn bay ngang màn hình:
  * Hóa đơn cần chém (Lãng phí): *Gói cước xem phim không dùng (70k), Cà phê thương hiệu cao cấp (80k), Mua đồ ăn vặt bốc đồng (50k)*.
  * Hóa đơn không được chém (Thiết yếu): *Tiền điện nước, Tiền internet làm việc, Tiền xăng xe*.
* **Cách tính điểm:**
  * Chém đúng 3 khoản lãng phí: Tiết kiệm thêm `+300.000 đ`, `financeScore: +30`.
  * Chém nhầm khoản thiết yếu: `sanity: -25`.

---

### Tháng 4: Đầu tư mạo hiểm hay Tích lũy bền vững (Mystery Node)
* **Bối cảnh:** Đồng nghiệp rủ góp 1.000.000 đ lướt sóng một dự án kinh doanh ngắn hạn, hứa hẹn lãi 50% sau 1 tháng hoặc có nguy cơ mất 50% vốn.
* **Lựa chọn A (Mạo hiểm - Bánh xe xác suất):**
  * Tỷ lệ 60% Thắng: `savings: +1.500.000 đ`, `sanity: +20`.
  * Tỷ lệ 40% Thua: `savings: -500.000 đ`, `sanity: -30`, `financeScore: -20`.
* **Lựa chọn B (Gửi Túi Thần Tài an toàn):** Nhận lãi suất tích lũy đều đặn mỗi ngày, chắc chắn và thanh khoản linh hoạt.
  * *Hệ quả:* `savings: +550.000 đ`, `sanity: +10`, `financeScore: +15`.
* **Châm ngôn kinh tế (Daniel Kahneman):**
  > *"Kahneman chứng minh rồi: Cảm giác đau đớn khi mất 500 nghìn lớn gấp đôi niềm vui khi nhặt được 500 nghìn. Đừng đánh cược mục tiêu chắc chắn lấy một giấc mơ bấp bênh."*

---

### Tháng 5: Đánh đổi sức khỏe lấy thu nhập (Dilemma Node)
* **Bối cảnh:** Bạn nhận được lời mời làm một dự án tự do (Freelance) ngoài giờ trị giá 2.000.000 đ, nhưng phải thức đêm liên tục 10 ngày.
* **Lựa chọn A (Cày cuốc kiếm thêm):** Nhận dự án, nạp toàn bộ thù lao vào quỹ Đà Lạt.
  * *Hệ quả:* `savings: +2.000.000 đ`, `sanity: -45` (Nguy cơ cận kề kiệt sức), `financeScore: +15`.
* **Lựa chọn B (Giữ gìn thể lực):** Từ chối dự án, duy trì mức tiết kiệm định kỳ tiêu chuẩn 500.000 đ.
  * *Hệ quả:* `savings: +500.000 đ`, `sanity: +15`, `financeScore: +10`.

---

### Tháng 6: Cột mốc nửa chặng đường (Milestone Node)
* **Bối cảnh:** Kiểm tra tiến độ Cây Tài Chính. Hệ thống tổng kết tài nguyên:
  * Nếu `savings >= 3.000.000 đ`: Cây ra hoa sum suê, thưởng `+20 Finance Score`.
  * Nếu `savings < 2.000.000 đ`: Cây còi cọc, kích hoạt cảnh báo trễ hạn.
* **Hành động:** Người dùng tương tác chạm vào cây để rung chuông nhận thưởng ngẫu nhiên (`sanity: +15` hoặc `savings: +100.000 đ`).

---

### Tháng 7: Thử thách chữ tín thanh toán (Debt & Due Date Node)
* **Bối cảnh:** Hạn thanh toán hóa đơn điện thoại và sao kê chi tiêu rơi vào ngày nghỉ cuối tuần, tài khoản đang kẹt tiền mặt.
* **Lựa chọn A (Thanh toán đúng hạn bằng giải pháp dự phòng):** Kích hoạt trích tiền tự động từ nguồn tiền dự phòng để thanh toán đúng ngày.
  * *Hệ quả:* `savings: +500.000 đ`, `sanity: -5`, `financeScore: +35`.
* **Lựa chọn B (Để sang tuần sau thanh toán bù):** Mặc kệ trễ hạn 3 ngày.
  * *Hệ quả:* `savings: +500.000 đ`, `financeScore: -50`, Cây bị sâu bọ tấn công.
* **Châm ngôn kinh tế (Adam Smith):**
  > *"Cụ Adam Smith dạy: Giữ chữ tín khi trả tiền đúng hẹn là chiếc chìa khóa vàng của tài chính. Trễ một ngày tiền nong, mất mười năm uy tín."*

---

### Tháng 8: Biến cố xe cộ bất ngờ (Crisis Node)
* **Bối cảnh:** Xe máy bị hỏng nhông xích và thủng lốp trên đường đi làm, chi phí sửa khẩn cấp mất 700.000 đ.
* **Lựa chọn A (Rút thẳng quỹ mục tiêu):** Lấy tiền Đà Lạt ra trả trực tiếp cho tiệm sửa xe.
  * *Hệ quả:* `savings: -700.000 đ`, `sanity: -20`, `financeScore: -10`.
* **Lựa chọn B (Dùng hạn mức tín dụng dự phòng miễn lãi):** Chi trả bằng Ví Trả Sau, dùng tiền lương tháng tới hoàn trả đúng hạn để giữ nguyên vẹn quỹ mục tiêu.
  * *Hệ quả:* `savings: +500.000 đ` (giữ nguyên), `sanity: -5`, `financeScore: +30`.
* **Châm ngôn kinh tế (Robert Kiyosaki):**
  > *"Bác Kiyosaki dặn: Người khôn ngoan không bao giờ lấy tiền tích lũy tương lai đi vá víu sự cố hiện tại. Hãy dùng công cụ tài chính thông minh để che chắn rủi ro."*

---

### Tháng 9: Mini-Game "Cân Bằng 3 Hũ Tiền" (Tactile Node 2)
* **Cơ chế chơi:** Kéo thả thanh trượt phân bổ nguồn thu nhập 10 triệu đồng vào 3 hũ:
  * Hũ 1: Chi phí thiết yếu (Chuẩn: 50%)
  * Hũ 2: Quỹ Mục Tiêu Đà Lạt (Chuẩn: 30%)
  * Hũ 3: Tự thưởng hưởng thụ (Chuẩn: 20%)
* **Đánh giá:** Nếu phân bổ sát tỷ lệ chuẩn trong vòng 5 giây: Nhận danh hiệu "Nhà Hoạch Định Chuẩn Mực", `sanity: +25`, `savings: +500.000 đ`, `financeScore: +25`.

---

### Tháng 10: Khoản thưởng bất ngờ cuối năm (Opportunity Node)
* **Bối cảnh:** Công ty bất ngờ thưởng hoàn thành sớm dự án một khoản 1.500.000 đ.
* **Lựa chọn A (Đập hộp tiêu sản):** Mua ngay chiếc tai nghe mới để nghe nhạc khi đi du lịch.
  * *Hệ quả:* `savings: +500.000 đ`, `sanity: +35`, `financeScore: 0`.
* **Lựa chọn B (Gia tăng tài sản):** Nạp toàn bộ 1.500.000 đ vào quỹ Đà Lạt để về đích sớm.
  * *Hệ quả:* `savings: +2.000.000 đ`, `sanity: +10`, `financeScore: +30`.

---

### Tháng 11: Trùm cuối cám dỗ chặng áp chót (Boss Battle Node)
* **Bối cảnh:** Nhóm bạn đi cùng rủ nâng cấp toàn bộ dịch vụ từ khách sạn 3 sao lên Resort 5 sao cao cấp với chi phí đội thêm 2.500.000 đ/người.
* **Lựa chọn A (Đu theo nhóm bạn):** Phá vỡ kế hoạch tài chính ban đầu, chấp nhận vay mượn thêm để ở resort sang chảnh.
  * *Hệ quả:* `savings: -2.000.000 đ`, `sanity: +20`, `financeScore: -40`. Kế hoạch bị dời lịch ít nhất 3 tháng.
* **Lựa chọn B (Giữ vững nguyên tắc chi tiêu):** Khéo léo từ chối nâng hạng, giữ đúng gói trải nghiệm 3 sao ấm cúng vừa vặn với túi tiền.
  * *Hệ quả:* `savings: +500.000 đ`, `sanity: +10`, `financeScore: +40`. Cây tài chính đơm quả chín rực rỡ.
* **Châm ngôn kinh tế (John Bogle):**
  > *"Bác John Bogle bảo rồi: Đừng chi tiền để gây ấn tượng với những người bạn thậm chí còn không thích. Hạnh phúc thật sự là chuyến đi trong tầm kiểm soát của túi tiền."*

---

### Tháng 12: Đích đến & Đóng cổng hành trình (Final Arrival Node)
* Tính toán tổng kết toàn bộ 3 chỉ số `savings`, `sanity`, `financeScore`.
* Chuyển người dùng sang màn hình Dashboard Chẩn Đoán.

---

## 4. BẢNG CHẨN ĐOÁN & PHÂN LOẠI TƯ DUY (POST-GAME DIAGNOSTIC)

Sau khi cán đích tháng 12, game cung cấp bản giám định tư duy tài chính cá nhân gồm 4 hồ sơ:

| Thang điểm Finance Score | Tỷ lệ tích lũy hoàn thành | Danh hiệu Persona | Bản chất tư duy | Lời khuyên trọng tâm |
| :--- | :--- | :--- | :--- | :--- |
| **750 - 850** | >= 100% | Bậc Thầy Cân Bằng Tài Chính | Quản trị dòng tiền xuất sắc, giữ được kỷ luật mà không bị kiệt sức. | Duy trì cơ chế trích tiền tự động để giải phóng tâm trí. |
| **650 - 749** | 80% - 99% | Chiến Binh Tích Lũy Bền Bỉ | Kỷ luật tốt nhưng còn lúng túng khi gặp các biến cố chi tiêu bất ngờ. | Cần bổ sung hạn mức dự phòng khẩn cấp để không phạm vào quỹ chính. |
| **500 - 649** | 50% - 79% | Tín Đồ Chi Tiêu Cảm Xúc | Thường xuyên bị bẫy giảm giá và tâm lý FOMO làm trễ hạn mục tiêu. | Cần công cụ đóng băng tiền tiết kiệm để tránh tự tay rút xài. |
| **Dưới 500** | < 50% | Báo Động Đỏ Cần Cứu Hộ | Dễ rơi vào vòng xoáy áp lực rồi chi tiêu bù đắp quá độ, điểm uy tín suy giảm. | Cần thiết lập lại từ những khoản tích lũy siêu nhỏ 10.000 đ/ngày. |

---

## 5. ĐẶC TẢ CHUYỂN ĐỔI WEB-TO-APP & PHỄU CHUYỂN ĐỔI (CTA & UTILITY)

### 5.1. Cấu trúc Deep-link chuyển đổi trọn vẹn tham số
Nút bấm hành động duy nhất tại trang kết quả: **"Kích Hoạt Kế Hoạch 6 Triệu Đà Lạt Tự Động Trên MoMo"**.

* **Format URL Deep-link:**
  ```text
  https://momo.vn/app/savings-goal?title=Chuyen_di_Da_Lat_2026&target=6000000&deadline=12&monthly_save=500000&score_tier=MASTER&utm_source=web_platform&utm_medium=game_muaquyt2&utm_campaign=finance_score_edu
  ```
* **Hành vi xử lý:**
  * *Trên Mobile Browser:* Gọi trực tiếp ứng dụng MoMo, mở thẳng vào màn hình tạo **Tiết Kiệm Mục Tiêu** hoặc **Túi Thần Tài**, tự động điền sẵn tên mục tiêu, số tiền 6.000.000 đ và chu kỳ trích tiền tự động hàng tháng.
  * *Trên Desktop Browser:* Hiển thị Pop-up mã QR động có logo MoMo ở giữa. Người dùng quét bằng App MoMo sẽ mở đúng màn hình trên ứng dụng.

### 5.2. Umami Tracking Event Schema (SSOT)

```typescript
// Gắn tracking vào các điểm mốc trong game
export const trackGameEvent = (eventName: string, data: Record<string, any>) => {
  if (typeof window !== 'undefined' && (window as any).umami) {
    (window as any).umami.track(eventName, data);
  }
};

// Danh mục sự kiện chuẩn
// 1. Khởi động: trackGameEvent('game_start', { goal_type: 'travel', target: 6000000 });
// 2. Quyết định từng tháng: trackGameEvent('game_turn_choice', { month: 2, choice: 'A', score: 620 });
// 3. Kích hoạt kiệt sức: trackGameEvent('game_burnout_triggered', { month: 5, savings_lost: 700000 });
// 4. Hoàn thành game: trackGameEvent('game_completed', { persona: 'MASTER', final_score: 780, total_savings: 6200000 });
// 5. Click chuyển đổi App: trackGameEvent('game_cta_app_click', { device: 'mobile', target_goal: 'Da_Lat' });
```

---

## 6. KHUNG PROMPT CHUYỂN GIAO CHO CLAUDE ĐỂ SINH CODE (MASTER PROMPT)

Sao chép toàn bộ nội dung trong khung dưới đây và dán trực tiếp vào Claude:

```markdown
Bạn là Tech Lead & Lead Frontend Engineer chuyên sâu về Next.js (App Router), React, Tailwind CSS, Framer Motion và Web Audio API.

Nhiệm vụ của bạn là lập trình hoàn chỉnh một Web Game tương tác chất lượng cao có tên "Financial Goal Simulator 2.0: Hành Trình Đà Lạt" dựa trên tài liệu đặc tả GDD-FINSIM-2.0 (FIN-SIM-MOMO-2026).

Yêu cầu kỹ thuật bắt buộc:
1. Kiến trúc State:
   - Sử dụng React Context hoặc Zustand quản lý 3 chỉ số cốt lõi: Tiền tích lũy (savings), Hạnh phúc (sanity 0-100), và Điểm tin cậy (financeScore 300-850).
   - Triển khai đúng logic "Ngưỡng áp lực & Chi tiêu bù đắp quá độ": Nếu sanity tụt về 0, kích hoạt màn hình cảnh báo đỏ, trừ 35% tiền tiết kiệm và trừ 40 điểm Finance Score.

2. Trải nghiệm Bản đồ 12 Tháng (Roguelite Board):
   - Thiết kế bản đồ hành trình gồm 12 Node trực quan (Node thu nhập, cám dỗ, mini-game, sự kiện bí ẩn, trùm cuối).
   - Mỗi tháng hiển thị hộp thoại quyết định với 2 lựa chọn có tính đánh đổi rõ ràng.
   - Sau mỗi quyết định, hiển thị popup 1 câu châm ngôn kinh tế học bình dân trong 3 giây (Warren Buffett, Morgan Housel, Daniel Kahneman...) trước khi nhân vật bước tiếp sang ô kế tiếp.

3. Tích hợp 1 Mini-Game cơ học (Tactile Mechanic):
   - Lập trình mini-game "Chém Hóa Đơn Thừa" ở Tháng 3: Người dùng vuốt màn hình để chém các khoản lãng phí bay qua trong 5 giây để gom tiền thưởng vào hũ.

4. Màn hình Dashboard Tổng Kết:
   - Hiển thị bản phân loại Persona dựa trên thang điểm cuối cùng.
   - Thống kê tỷ lệ hoàn thành mục tiêu, độ trễ thời gian (nếu có).
   - Nút CTA Web-to-App "Kích Hoạt Kế Hoạch 6 Triệu Đà Lạt Tự Động Trên MoMo" kèm bộ sinh link Deep-link URL đầy đủ tham số và hiển thị QR Code dự phòng cho thiết bị máy tính.
   - Tích hợp hàm tracking Umami chuẩn theo tài liệu.

5. Giao diện & Hiệu ứng:
   - Tối ưu tuyệt đối cho màn hình điện thoại di động (Mobile-first).
   - Hiệu ứng nhảy số tiền mượt mà (Ticker counter), rung lắc khi bị trừ điểm, âm thanh nảy đồng xu bằng Web Audio API không cần tải file ngoài.

Hãy viết code hoàn chỉnh, sạch, chia component module bài bản (GameContainer, BoardMap, StatBars, DecisionModal, SlashMiniGame, ResultDashboard), có TypeScript types đầy đủ và sẵn sàng chạy ngay.
```
