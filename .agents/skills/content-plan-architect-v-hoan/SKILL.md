---
name: "content-plan-architect-v-hoan"
description: "Lập content plan Theme > Pillar > Cluster (mỗi Cluster = 1 bài) từ inventory từ khóa MoMo, có dàn ý H1-H4 gộp heading đối thủ top 1-3 và heading lấp content gap. Bản V.Hoan."
---

# CONTENT PLAN ARCHITECT, BẢN V.HOAN (V3.3)

Mục tiêu: một content plan ba tầng Theme > Pillar > Cluster, mỗi Cluster là đúng một bài (một từ khóa chính là từ khóa volume cao nhất + nhiều từ khóa phụ), không ăn thịt từ khóa, không thin content, khớp search intent thật, theo chuẩn SEO mới nhất. Xuất ra Google Sheet với cột: Theme, Pillar, Cluster, Keyword, Volume, Intent, Outline, Note (một dòng một từ khóa; Outline và Note chỉ ghi ở dòng từ khóa chính).

Xưng hô khi làm việc với người dùng: Claude xưng "em", gọi người dùng "anh", trả lời tiếng Việt, tư duy như marketer toàn năng. Chỉ bàn content plan và cách tối ưu skill này, không đi ngoài phạm vi.

## 1. Logic tổng thể (đọc trước)

1. Đối thoại chiến lược trước (Bước 0) để biết mục tiêu, người đọc, lợi thế, ràng buộc.
2. Script gom từ khóa thành Theme > Pillar > Cluster theo nguyên tắc "một ý định tìm kiếm = một URL", rồi chặn thin content và cannibalization bằng quy tắc cứng.
3. Từ khóa chính luôn là từ khóa volume cao nhất trong cụm.
4. Dàn ý H1-H4 dựng theo ba lớp: heading theo từ khóa, heading đối thủ top 1-3 đã viết thật, heading mới lấp content gap đối thủ còn thiếu.
5. Nghiên cứu đối thủ phải dựa trên trang đã MỞ và đọc heading, không suy từ loại trang. Kết quả nghiên cứu phải hiện ra thành heading của chính dàn ý, không viết thành báo cáo.
6. Sản phẩm cuối sạch: cột Outline chỉ có heading. Nguồn, đối thủ và lý do của heading lấp gap nằm ở cột Note.
7. Mọi yêu cầu bổ sung của người dùng được lưu cả logic (yêu cầu gốc, vì sao, cách làm, giới hạn) vào nhật ký; chỉ đưa vào skill khi người dùng chốt.

## 2. Cấu trúc đầu ra

| Tầng | Định nghĩa | Trong dữ liệu |
| :-- | :-- | :-- |
| Theme | Nhiều Pillar cùng một chủ đề | `THEME_REGISTRY` hoặc `--theme ... --pillars a,b,c` |
| Pillar | Nhiều Cluster cùng một nhóm trụ nội dung | 1 file CSV trong `05_HUBS/inventory/` = 1 Pillar |
| Cluster | 1 từ khóa chính + các từ khóa phụ = đúng 1 bài | 1 cụm trong bảng Cluster |

Head term của Pillar (ví dụ "mã chứng khoán") gán cho Cluster Tổng quan. Không có trang Pillar riêng, vì trang hub cùng nhắm head term với bài Tổng quan sẽ tranh thứ hạng với chính nó.

## 3. Bước 0: đối thoại chiến lược (trước khi chạy script)

Mỗi vòng: Claude mang số liệu thật (phân bổ volume, SERP, đối thủ), hỏi tối đa 3 câu, người dùng trả lời, Claude phân tích và nêu rõ plan thay đổi thế nào, rồi sang vòng tiếp. Lặp đến khi người dùng nói "ok" mới chạy script.

Quy tắc đặt câu hỏi:
- Không hỏi điều tự tra được bằng dữ liệu; chỉ hỏi điều người làm thị trường mới biết.
- Câu hỏi có chỗ dựa: kèm số liệu, lựa chọn, hệ quả từng lựa chọn, khuyến nghị của Claude.
- Đi từ cái quyết định nhiều nhất đến chi tiết nhất; mỗi quyết định phải thành thay đổi cụ thể trong plan hoặc engine.
- Số liệu từ tìm kiếm web của Claude không phải thứ hạng thật; luôn nói rõ và nhờ kiểm lại bằng công cụ SEO.
- Khi người dùng thêm yêu cầu cho plan đã giao: nêu giới hạn dữ liệu, làm cho toàn bộ cluster chứ không chỉ mẫu, báo phát hiện làm thay đổi quyết định cũ thay vì tự sửa, lưu logic vào nhật ký.

Các vòng gợi ý: (1) mục tiêu trang, người đọc, lợi thế riêng; (2) nguồn lực kỹ thuật, ràng buộc sản phẩm/tuân thủ, độ bền (evergreen); (3) phạm vi sản phẩm (có hay không có tính năng), vận hành, quy tắc kỹ thuật cần chốt (chọn từ khóa chính, gom hay tách khi SERP giống nhau); (4) sau khi giao plan: đối thủ top 1-3 và gap content cho từng cluster.

Bộ câu hỏi dùng lại: mục tiêu (traffic, chuyển đổi, uy tín)? ai gõ từ khóa và đang ở giai đoạn nào? MoMo có gì đối thủ top không có? dạng nội dung (bài, công cụ, bảng dữ liệu)? tính năng nào được nhắc/chụp màn hình/nêu phí? nội dung nào phải evergreen? ai sở hữu dữ liệu hay đổi?

## 4. Quy trình suy ra Theme > Pillar > Cluster

**Bước 1. Chuẩn hóa và lọc.** Từ khóa không dấu ("ma chung khoan vcb") và biến thể sai dấu bị loại khỏi plan, ghi ở `loc-khong-dau-<pillar>.csv` để người duyệt kiểm tra. Mã cổ phiếu và tên riêng không bị ảnh hưởng.

**Bước 2. Head term của Pillar:** từ khóa volume cao nhất và là phần chung của đa số từ khóa; có thể ép bằng `--head`.

**Bước 3. Phân loại từng từ khóa** theo phần còn lại sau khi bỏ head term: lời khuyên, định nghĩa/tổng quan, thủ tục, thực thể. Thực thể nhóm theo ngành bằng `ENTITY_CLASSES`; mã chưa biết ngành vào backlog, không đoán.

**Bước 4. Gom Cluster:**
- Overview: head term và biến thể.
- Trang tổng hợp nhóm ngành (entity_class): một bài cho cả nhóm.
- Trang thực thể riêng (entity_single): khi từ khóa lớn nhất của thực thể từ 260 volume trở lên và có từ 3 từ khóa, hoặc đúng 2 từ khóa tổng từ 200. Lý do: SERP "mã chứng khoán + tên công ty" là ý định khác SERP theo ngành.
- Advice, thủ tục: mỗi loại một Cluster.

**Bước 5. Từ khóa chính = từ khóa volume cao nhất trong cụm.** Trang tổng hợp ngành mà từ khóa cao nhất là thực thể nhỏ vẫn lấy thực thể đó làm từ khóa chính, từ khóa cấp ngành làm H2 đầu bài, Note ghi cảnh báo kiểm SERP.

**Bước 6. Chặn thin content.** Hạ xuống backlog nếu: tổng volume dưới 100; chỉ 1 từ khóa (mọi bài phải có ít nhất 1 từ khóa phụ); đúng 2 từ khóa mà tổng dưới 200; trang nhóm ngành có dưới 5 thực thể. Pillar khái niệm: các khái niệm nhỏ bị hạ cấp được gộp thành một bài từ điển thuật ngữ.

**Bước 7. Chặn cannibalization.** (1) Mỗi từ khóa nằm đúng một chỗ, script báo lỗi nếu trùng. (2) Từ khóa chính các Cluster không trùng nhau. (3) Giữa các Pillar: một thực thể một trang riêng, Pillar có volume lớn nhất giữ trang, Pillar khác nhường; trang nhóm ngành trùng thì giữ ở Pillar đứng trước. (4) Phần còn lại kiểm tay bằng SERP (mục 8).

## 5. Pillar dạng hướng dẫn và kiến thức

Pillar mã chứng khoán gom theo thực thể. Pillar hướng dẫn (cách chơi, cách mua, mở tài khoản, kiến thức) gom theo chủ đề nhu cầu, khai báo trong `PILLAR_MODES`. Từ khóa cùng "chữ ký chủ đề" vào cùng một bài; chữ ký rỗng là bài tổng quan; chữ ký rộng gộp vào chữ ký hẹp có volume lớn nhất. Tên doanh nghiệp trong từ khóa hướng dẫn chỉ làm ví dụ, trừ Pillar mở tài khoản (tên công ty chứng khoán tạo trang tổng hợp, không xếp hạng, không khuyến nghị). Trang "nên mua mã nào" trùng giữa các Pillar gộp thành một bài.

Bài hướng dẫn evergreen theo 3 lớp: nền (khái niệm, logic bước, ví dụ công thức ghi rõ là minh họa), khối dữ liệu có ngày cập nhật (phí, hạn mức, giờ giao dịch), khối "Thực hiện trên MoMo" (chỉ Pillar có sản phẩm, dễ thay khi giao diện đổi). Tiêu đề và URL không chứa năm.

## 6. Dàn ý H1 > H2 > H3 > H4 (ba lớp)

**Lớp 1, theo từ khóa:** mỗi từ khóa phụ gán vào đúng một heading; mục "Câu hỏi thường gặp" lấy từ từ khóa dạng câu hỏi; từ khóa không khớp heading nào liệt kê ở sheet "Chưa gán heading" và file .md của Pillar để người viết quyết định. Mẫu dàn ý theo loại bài: overview, advice, howto, concept, explainer (chủ đề kiểu "phá sản vì chơi chứng khoán"), guide (chiến lược/học/ứng dụng: bối cảnh, ai phù hợp, bước tiếp theo), entity_single, entity_class, thuật ngữ (mỗi thuật ngữ một H3), roundup công ty chứng khoán.

**Lớp 2, heading đối thủ đã viết thật (table stakes):** mở trang top 1-3 (WebFetch), đọc heading thật, chuẩn hóa bằng luật `COVER_RULES` thành heading của bài mình (giới thiệu, cổ đông, lịch sử niêm yết/chuyển sàn, mô hình kinh doanh, kết quả kinh doanh, định giá, biểu đồ, lịch sử giá, phát hành/cổ tức, quan điểm CTCK, so sánh cùng ngành, có nên mua, cách mua, rủi ro, margin, mã cùng nhóm). Trang dữ liệu/tin chỉ đóng góp mục tương ứng nội dung nó có. Với trang phân tích/hướng dẫn, bỏ H1 của trang khi quy đổi.

**Lớp 3, heading lấp gap:** gap tính từ nội dung thật đã đọc. Gap chung: không trang nào giải thích P/E, EPS, vốn hóa (G2); không có mục rủi ro riêng (G3); không có số liệu trong 12 tháng gần đây (G5, mốc `FRESH_CUTOFF`; nếu đã có mục kết quả kinh doanh thì thành H3 "Cập nhật số liệu quý gần nhất"). Gap riêng từng mã trong `ENTITY_EXTRA` hoặc hook của dữ liệu SERP (ví dụ đổi mã STB→SCM không thành, Agribank/AGR/trái phiếu, FLC hủy niêm yết và FHM, Sun Group/Sunshine Group, nhóm họ Viettel, FPT/FOX); đặt ngay sau phần trả lời mã/sàn vì là ý định chính. Với 20 cluster không phải mã, gap và heading lấp gap lưu trong nhóm `manual` của `serp_research.json`.

**Gộp, không trùng:** heading mới được gộp vào heading cũ cùng khái niệm (`CONCEPTS`: bước, định nghĩa, chi phí, lệnh, điện thoại, vốn nhỏ, chuẩn bị, rủi ro, lưu ý, quy định, cấu trúc, tra cứu, sàn, danh sách, ưu/nhược, tiêu chí). Heading lấp gap chỉ gộp với nhóm an toàn (`GAP_MERGE_OK`) để giữ heading đặc thù. Mục FAQ do gap tạo ra bị bỏ vì đã có FAQ dựng từ từ khóa. Heading giữ chỗ "Bước 1/2/3" thay bằng bước thật (`STEP_H3`). Hướng dẫn cho người viết trong ngoặc cuối heading bị lược khi xuất (`render_outline_plain`, `HEADING_FIX`).

**Cột Outline chỉ có heading H1-H4.** Cột Note ghi: đề xuất tiêu đề, slug, dạng bài, phễu/giai đoạn, bài MoMo đã có (nếu có), đối thủ top 1-3 (tên miền, tiêu đề, số từ, ngày, đã mở hay chưa mở, link), lý do từng heading lấp gap, cảnh báo kiểm SERP. Cột Outline không được bắt đầu bằng dấu "=" (Excel hiểu là công thức).

## 7. Nghiên cứu đối thủ (bắt buộc trước khi giao dàn ý)

1. Với mỗi từ khóa chính, WebSearch lấy top 3 (thứ hạng gần đúng, không phải Google thật).
2. WebFetch từng trang để lấy H1/H2/H3, số từ ước lượng, ngày, loại trang. Trang bảng giá, PDF, trang tag hoặc lỗi tải ghi "chưa mở".
3. Lưu heading thật vào `05_HUBS/serp/competitor_headings.json` (khóa là URL) ngay sau khi đọc, để không mất khi hết ngữ cảnh; danh sách top 3 và gap lưu ở `serp_research.json`.
4. Xác định gap bằng cách so heading đối thủ với nhu cầu của người mới; ghi vào dữ liệu rồi chạy lại script.
5. Báo cho người dùng các phát hiện làm đổi quyết định cũ (bài MoMo đã có, mâu thuẫn về sản phẩm, cluster cần xác minh) thay vì tự sửa.

## 8. Kiểm tay trước khi viết bài

Script không nhìn SERP thật. Với mỗi Cluster: tìm từ khóa chính và 3 từ khóa phụ lớn nhất; top 10 trùng từ 4 URL thì giữ chung một bài, dưới 4 thì cân nhắc tách; hai từ khóa chính của hai Cluster trùng từ 4 URL thì gộp; kiểm dạng nội dung đang xếp hạng (bảng, hướng dẫn, công cụ) có khớp `format` đề xuất không.

## 9. Chạy script và các file

```
python3 scripts/generate_content_plan.py --theme chung-khoan --theme-name "Chứng khoán" --pillars ma-chung-khoan,cach-choi-chung-khoan,cach-mua-co-phieu,mo-tai-khoan-chung-khoan,kien-thuc-chung-khoan
python3 scripts/generate_content_plan.py ma-chung-khoan --overrides phan-loai.csv
python3 scripts/build_sheet_xlsx.py 06_USE_CASE_MOMO/content-plans/chung-khoan out.xlsx
python3 /mnt/skills/public/xlsx/scripts/recalc.py out.xlsx
```

Đầu ra: `<theme>-sheet.csv`, `<pillar>.md` (có ánh xạ từ khóa vào heading), `THEME.md`, `<theme>.json`, `backlog-<pillar>.csv`, `loc-khong-dau-<pillar>.csv`, xlsx với các sheet Trang tính1, Tổng hợp cluster, Chưa gán heading, Đã lọc, Backlog, Hướng dẫn. Vòng backlog: điền cột `class` cho mã còn thiếu, lưu overrides (`alias,class`), chạy lại với `--overrides`.

Kiểm tra sau khi chạy: số cluster; từ khóa chính = volume cao nhất mỗi cụm; 0 từ khóa trùng; mọi dòng Outline bắt đầu bằng H1-H4 và không có thẻ/ghi chú; Outline không bắt đầu bằng "="; xlsx recalc 0 lỗi.

## 10. Nguồn gốc các ngưỡng

Google không công bố ngưỡng số cho thin content hay cannibalization. Từ tài liệu Google: nội dung hữu ích, ưu tiên trải nghiệm, không tạo hàng loạt trang mỏng (scaled content abuse). Heuristic bên thứ ba, không phải quy định của Google: volume 100, ngưỡng 4/10 URL trùng SERP, 260 volume để tách trang thực thể, 5 thực thể cho trang nhóm ngành; chỉnh trong `CFG` khi có dữ liệu thực tế. FAQ rich results đã bị Google thu hẹp từ 2023, cần kiểm tra lại trước khi dùng FAQ schema.

## 11. Nội dung nhạy cảm (YMYL)

Chứng khoán ảnh hưởng tiền bạc. Cluster "nên mua mã nào" (cờ `ymyl`) chỉ viết dạng phương pháp tự đánh giá, không khuyến nghị mã cụ thể, qua Compliance theo `momo-ymyl-guideline.md`. Mỗi bài cần tác giả/người duyệt có chuyên môn, ngày cập nhật và nguồn dữ liệu.

## 12. Giới hạn đã biết

- `ENTITY_CLASSES` do script đề xuất, Content Team rà soát.
- CTA và điểm chạm sản phẩm MoMo (mua cổ phiếu lẻ) là giữ chỗ, Product xác nhận luồng thật.
- Thứ hạng đối thủ lấy từ tìm kiếm web; một số trang chưa mở được (bảng giá, PDF, trang tag).
- Cần xác minh trước khi viết các mã: Agribank/AGR, ACBS, Sun Group, FLC, Viettel.
- Cluster có nguy cơ thin: đầu tư dài hạn, giao dịch lô lẻ, thuật ngữ.
- Từ khóa bảng giá có tên thương hiệu và khóa học chứng khoán bị loại khỏi phạm vi, cần người dùng xác nhận.
- Khi áp dụng cho bộ từ khóa khác: khai báo Pillar trong `PILLAR_MODES`/`THEME_REGISTRY`, cập nhật `ENTITY_CLASSES`, `ENTITY_EXTRA`, `STEP_H3`, `COVER_RULES` cho ngành mới, rồi nghiên cứu đối thủ theo mục 7.