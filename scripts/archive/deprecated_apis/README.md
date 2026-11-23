# THƯ MỤC LƯU TRỮ CÁC SCRIPT GỌI API NGOÀI (DEPRECATED APIS)

> **CẢNH BÁO QUAN TRỌNG:**  
> Toàn bộ các script trong thư mục này đã bị **VÔ HIỆU HÓA HOÀN TOÀN VÀ VĨNH VIỄN** theo yêu cầu của Hạ tầng MoMo.  
> Tuyệt đối KHÔNG chạy, không khôi phục, không kích hoạt lại các script này.

## Lý do lưu trữ:
1. Ngăn chặn việc phát sinh các yêu cầu mạng (Network Requests) hoặc quét dữ liệu tự động ra ngoài Google Analytics 4 (GA4 Data API) và Google Search Console (GSC API) gây kích hoạt cảnh báo an ninh từ Hạ tầng MoMo.
2. Hệ thống Web Platform chuyển sang vận hành thuần túy trên:
   - **Google Tag Manager (GTM):** Quản lý thẻ, trigger, biến và cấu hình sự kiện đo lường Web (`GTM-P9JDDJZ`).
   - **Local Analytical Data Mart:** Cơ sở dữ liệu SQLite cục bộ (`performance.sqlite`).
