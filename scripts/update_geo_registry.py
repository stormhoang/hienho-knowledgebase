#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script cập nhật SSOT Geo Entity Registry trên Web Hubs (react-web-momo)
Đảm bảo 18 Archetypes nghiệp vụ thực tế và Hệ thống Dynamic Fallback theo Sector không bị lỗi shell interpolation.
"""
import os

CONTENT = r'''/**
 * GEO & ENTITY GAP INTELLIGENCE REGISTRY (SSOT)
 * Thư viện dữ liệu thực thể, cấu trúc Schema.org, đoạn trích Direct Answer (AI Answer Box)
 * và 3 Lỗ hổng thực thể (Entity Gaps: Chuyên môn, Bảo mật, Chi phí ẩn) cho Web Hubs.
 * Đã chuẩn hóa theo 18 Archetypes nghiệp vụ thực tế và Hệ thống Dynamic Fallback theo Sector.
 */

export interface SchemaField {
  field: string;
  desc: string;
}

export interface EntityGapPillar {
  title: string;
  summary: string;
  detail: string;
  actionable_angle: string;
}

export interface GeoEntityBlueprint {
  hub: string;
  theme: string;
  schema_type: string;
  schema_category: string;
  mandatory_fields: SchemaField[];
  direct_answer_text: string;
  word_count: number;
  sample_jsonld: Record<string, unknown>;
  pillars: {
    expertise: EntityGapPillar;
    trust: EntityGapPillar;
    high_intent: EntityGapPillar;
  };
  cta_text: string;
  deeplink: string;
  umami_event: string;
}

export const DOMAIN_ONTOLOGY_REGISTRY: Record<string, Omit<GeoEntityBlueprint, 'theme' | 'word_count'>> = {
  financial_savings: {
    hub: 'Financial Hub',
    schema_type: 'DepositAccount',
    schema_category: 'https://schema.org/DepositAccount',
    mandatory_fields: [
      { field: 'name', desc: 'Tên gói sản phẩm tiền gửi tiết kiệm.' },
      { field: 'provider', desc: 'Ngân hàng thương mại huy động được NHNN cấp phép (BankOrCreditUnion).' },
      { field: 'interestRate', desc: 'Lãi suất niêm yết theo kỳ hạn (%/năm).' },
      { field: 'amount', desc: 'Số tiền gửi tối thiểu mở sổ tiết kiệm.' },
      { field: 'feesAndCommissionsSpecification', desc: 'Quy định rút trước hạn và phương thức trả lãi.' },
    ],
    direct_answer_text:
      'Gửi tiết kiệm là hình thức tích lũy tài chính cho phép cá nhân gửi tiền nhàn rỗi vào các ngân hàng thương mại được Ngân hàng Nhà nước cấp phép nhằm sinh lời an toàn. Khoản tiền gửi được bảo hiểm theo luật định bởi BHTGVN (tối đa 125 triệu đồng), áp dụng đa dạng kỳ hạn từ 1 đến 36 tháng với lãi suất minh bạch và quản lý trực tuyến 24/7.',
    sample_jsonld: {
      '@context': 'https://schema.org',
      '@type': 'DepositAccount',
      name: 'Gửi Tiết Kiệm Ngân Hàng MoMo',
      provider: { '@type': 'BankOrCreditUnion', name: 'Hệ thống Ngân hàng Đối tác MoMo' },
      interestRate: 'Lãi suất cạnh tranh theo kỳ hạn',
      areaServed: 'VN',
    },
    pillars: {
      expertise: {
        title: 'Trần lãi suất Ngân hàng Nhà nước & Bảo hiểm tiền gửi 125 triệu',
        summary: 'Quy định pháp lý về bảo đảm an toàn vốn của người gửi tiền theo Luật Các TCTD.',
        detail:
          'Nội dung làm rõ: Tiền gửi tiết kiệm tại các ngân hàng liên kết được bảo hiểm bởi Bảo hiểm Tiền gửi Việt Nam (BHTGVN) với hạn mức chi trả tối đa 125 triệu đồng/người/tổ chức tín dụng. Lãi suất tiền gửi dưới 6 tháng tuân thủ trần do Thống đốc NHNN ban hành.',
        actionable_angle: 'Bảng đối chiếu trần lãi suất NHNN và chính sách chi trả bảo hiểm tiền gửi.',
      },
      trust: {
        title: 'Hợp đồng tiền gửi điện tử & Xác thực sinh trắc học eKYC',
        summary: 'Cơ chế định danh và cấp chứng nhận số có giá trị pháp lý tương đương sổ giấy.',
        detail:
          'Khách hàng mở sổ tiết kiệm online nhận hợp đồng điện tử có chữ ký số xác thực từ ngân hàng đối tác. Dữ liệu được đối soát với Cơ sở dữ liệu Quốc gia về dân cư qua chip CCCD, đảm bảo không thể mạo danh rút tiền.',
        actionable_angle: 'Quy trình 3 bước xác thực sinh trắc học bảo vệ sổ tiết kiệm online.',
      },
      high_intent: {
        title: 'Công cụ tính lãi & Bảng so sánh lãi suất nhóm Big 4 vs NHTM Cổ phần',
        summary: 'Bóc tách chênh lệch lợi nhuận giữa các phương thức nhận lãi cuối kỳ vs nhận trước.',
        detail:
          'Cung cấp công thức tính lãi thực nhận: Số tiền lãi = Tiền gửi × Lãi suất (%/năm) × Số ngày / 365. So sánh trực quan giữa các nhóm ngân hàng và hướng dẫn cách chia nhỏ sổ để tránh mất toàn bộ lãi khi cần rút gấp.',
        actionable_angle: 'Bảng mô phỏng tiền lãi nhận được theo các mức gửi 50tr, 100tr, 500tr.',
      },
    },
    cta_text: 'Mở Sổ Tiết Kiệm Ngân Hàng Online',
    deeplink: 'momo://savings',
    umami_event: 'web_savings_hub_btn_click',
  },

  financial_credit_paylater: {
    hub: 'Financial Hub',
    schema_type: 'FinancialProduct',
    schema_category: 'https://schema.org/LoanOrCredit',
    mandatory_fields: [
      { field: 'name', desc: 'Tên thương mại của sản phẩm ví trả sau.' },
      { field: 'provider', desc: 'Tổ chức tài chính / Ngân hàng đối tác bảo lãnh phát hành (Organization).' },
      { field: 'interestRate', desc: 'Lãi suất công bố trong hạn (0% trong chu kỳ miễn lãi).' },
      { field: 'feesAndCommissionsSpecification', desc: 'Đặc tả các loại phí: dịch vụ, duy trì, chậm trả.' },
      { field: 'areaServed', desc: 'Khu vực áp dụng (Mặc định: Việt Nam).' },
    ],
    direct_answer_text:
      'Ví trả sau là hình thức tín dụng tiêu dùng số cho phép người dùng thanh toán trước các giao dịch mua sắm và trả tiền vào cuối kỳ hoặc trả góp. Sản phẩm này hoạt động dựa trên lịch sử tín dụng cá nhân, tích hợp trực tiếp vào ví điện tử, giúp tối ưu hóa dòng tiền mà không cần thẻ tín dụng vật lý.',
    sample_jsonld: {
      '@context': 'https://schema.org',
      '@type': 'FinancialProduct',
      name: 'Ví Trả Sau MoMo',
      description: 'Sản phẩm tiêu dùng số mua trước trả sau miễn lãi lên đến 45 ngày.',
      provider: { '@type': 'BankOrCreditUnion', name: 'TPBank (Ngân hàng TMCP Tiên Phong)' },
      areaServed: 'VN',
    },
    pillars: {
      expertise: {
        title: 'Tác động đến Điểm Tín Dụng Quốc Gia (CIC)',
        summary: 'Phân tích cụ thể ảnh hưởng của các khoản chậm trả đến hồ sơ tín dụng tại CIC.',
        detail:
          'Chậm thanh toán ví trả sau từ 10 ngày trở lên sẽ bị xếp vào nhóm nợ cần chú ý (Nhóm 2) hoặc nợ xấu (Nhóm 3-5) trên hệ thống CIC, ảnh hưởng trực tiếp đến khả năng vay mua nhà, mua xe trong 3–5 năm tới.',
        actionable_angle: 'Bảng phân loại 5 nhóm nợ CIC và mốc thời gian báo cáo vi phạm của ví trả sau.',
      },
      trust: {
        title: 'Cơ chế định danh điện tử eKYC & Dữ liệu C06',
        summary: 'Cơ chế xác thực danh tính số kết hợp cơ sở dữ liệu quốc gia về dân cư.',
        detail:
          'Ứng dụng AI Face Matching đối soát khuôn mặt với chip CCCD và xác thực trực tiếp qua CSDL Quốc gia về dân cư, ngăn chặn tuyệt đối tình trạng mở ví giả mạo hoặc chiếm quyền sử dụng.',
        actionable_angle: 'Sơ đồ 3 bước xác thực sinh trắc học và mã hóa bảo mật chuẩn PCI-DSS Level 1.',
      },
      high_intent: {
        title: 'Minh bạch chi phí ẩn & Bảng phí phạt chậm trả',
        summary: 'Bóc tách chi tiết toàn bộ các loại phí phát sinh ngoài lãi suất công bố 0%.',
        detail:
          'Công khai chi tiết: Phí dịch vụ duy trì hàng tháng khi có phát sinh giao dịch, công thức tính phí chậm trả theo từng mốc ngày và mức phí chuyển đổi trả góp 3-6-12 tháng.',
        actionable_angle: 'Bảng biểu phí chi tiết so sánh giữa thanh toán đúng hạn vs chậm hạn.',
      },
    },
    cta_text: 'Kích Hoạt Ví Trả Sau Hạn Mức Đến 10 Triệu',
    deeplink: 'momo://paylater',
    umami_event: 'web_paylater_hub_btn_click',
  },

  financial_consumer_loan: {
    hub: 'Financial Hub',
    schema_type: 'LoanOrCredit',
    schema_category: 'https://schema.org/LoanOrCredit',
    mandatory_fields: [
      { field: 'name', desc: 'Tên gói vay tín chấp / tiêu dùng.' },
      { field: 'provider', desc: 'Ngân hàng hoặc công ty tài chính được cấp phép cấp vốn.' },
      { field: 'annualPercentageRate', desc: 'Lãi suất phần trăm hàng năm (APR) theo dư nợ giảm dần.' },
      { field: 'loanTerm', desc: 'Thời hạn vay tối thiểu và tối đa.' },
      { field: 'amount', desc: 'Hạn mức giải ngân tối đa.' },
    ],
    direct_answer_text:
      'Vay tiêu dùng trực tuyến là giải pháp cấp vốn tín chấp số hóa cho phép cá nhân tiếp cận khoản vay tiền mặt từ các tổ chức tín dụng được Ngân hàng Nhà nước cấp phép mà không cần thế chấp tài sản. Hồ sơ được duyệt tự động qua chấm điểm tín dụng eKYC và giải ngân tức thì trong vài phút.',
    sample_jsonld: {
      '@context': 'https://schema.org',
      '@type': 'LoanOrCredit',
      name: 'Vay Tiêu Dùng Tín Chấp MoMo',
      provider: { '@type': 'FinancialService', name: 'Đối tác tài chính cấp phép bởi NHNN' },
      areaServed: 'VN',
    },
    pillars: {
      expertise: {
        title: 'Quy định trần lãi suất theo Thông tư NHNN & Luật Dân sự',
        summary: 'Phân định rõ ràng giữa khoản vay hợp pháp với bẫy tín dụng đen.',
        detail:
          'Khoản vay tuân thủ quy định trần lãi suất của NHNN, hợp đồng hiển thị rõ lãi suất danh nghĩa và lãi suất thực tế theo dư nợ giảm dần, loại bỏ hoàn toàn các loại phí bất hợp pháp.',
        actionable_angle: 'Bảng đối chiếu 4 tiêu chí nhận diện đối tác cho vay hợp pháp vs app vay đen.',
      },
      trust: {
        title: 'Hợp đồng tín dụng điện tử & Tính pháp lý số',
        summary: 'Cơ chế ký kết hợp đồng số bằng OTP có giá trị pháp lý tương đương văn bản giấy.',
        detail:
          'Phân tích cơ sở pháp lý của hợp đồng tín dụng điện tử theo Luật Giao dịch điện tử. Khách hàng nhận bản sao hợp đồng qua email kèm mã tra cứu lưu trữ tại cổng thông tin tổ chức tín dụng.',
        actionable_angle: 'Quy trình thẩm định hồ sơ tự động không gọi điện làm phiền người thân.',
      },
      high_intent: {
        title: 'Phí tất toán trước hạn & Công thức tính lãi dư nợ giảm dần',
        summary: 'Minh bạch công thức tính tiền lãi hàng tháng và chi phí phạt khi trả nợ sớm.',
        detail:
          'Cung cấp bảng tính mô phỏng: So sánh số tiền phải trả giữa cách tính dư nợ gốc ban đầu vs dư nợ giảm dần, kèm tỷ lệ phí tất toán trước hạn (thường từ 1% đến 5% dư nợ còn lại).',
        actionable_angle: 'Bảng tính chi tiết kế hoạch trả góp mẫu cho khoản vay 20 triệu kỳ hạn 12 tháng.',
      },
    },
    cta_text: 'Đăng Ký Vay Tiêu Dùng Trực Tuyến',
    deeplink: 'momo://loan',
    umami_event: 'web_loan_hub_btn_click',
  },

  financial_gold_fx: {
    hub: 'Financial Hub',
    schema_type: 'FinancialProduct',
    schema_category: 'https://schema.org/FinancialProduct',
    mandatory_fields: [
      { field: 'name', desc: 'Tên loại vàng hoặc cặp ngoại tệ tra cứu.' },
      { field: 'provider', desc: 'Thương hiệu vàng / Ngân hàng niêm yết tỷ giá.' },
      { field: 'price', desc: 'Giá mua vào và giá bán ra thời gian thực.' },
    ],
    direct_answer_text:
      'Giá vàng và tỷ giá ngoại tệ trực tuyến là tiện ích cập nhật biến động giá vàng miếng SJC, nhẫn 9999, vàng 24K/18K và tỷ giá các đồng tiền chủ chốt (USD, EUR, JPY) theo thời gian thực từ các thương hiệu vàng lớn và hệ thống ngân hàng được cấp phép tại Việt Nam.',
    sample_jsonld: {
      '@context': 'https://schema.org',
      '@type': 'FinancialProduct',
      name: 'Tra Cứu Giá Vàng & Tỷ Giá Ngoại Tệ MoMo',
      provider: { '@type': 'Organization', name: 'SJC, DOJI, PNJ & Hệ thống Ngân hàng' },
      areaServed: 'VN',
    },
    pillars: {
      expertise: {
        title: 'Nghị định 24/CP & Cơ chế điều hành thị trường vàng của NHNN',
        summary: 'Quy định pháp lý về sản xuất, kinh doanh vàng miếng và phòng chống buôn lậu ngoại tệ.',
        detail:
          'Làm rõ quy chế quản lý thị trường vàng độc quyền SJC của Ngân hàng Nhà nước, sự khác biệt pháp lý giữa vàng miếng SJC có số seri và vàng nhẫn tròn trơn 9999 từ các doanh nghiệp tư nhân.',
        actionable_angle: 'Bảng so sánh tính pháp lý và độ thanh khoản giữa vàng miếng SJC vs vàng nhẫn 9999.',
      },
      trust: {
        title: 'Hóa đơn điện tử có mã cơ quan thuế & Giám định tuổi vàng',
        summary: 'Tiêu chuẩn bảo vệ quyền lợi người mua tránh vàng thiếu tuổi, thiếu trọng lượng.',
        detail:
          'Các đối tác niêm yết đều phát hành hóa đơn điện tử khởi tạo từ máy tính tiền kết nối với Tổng cục Thuế, giấy chứng nhận tuổi vàng chuẩn quốc tế đạt độ tinh khiết 99.99%.',
        actionable_angle: 'Quy chuẩn 3 dấu hiệu nhận biết vàng miếng thật và cách tra cứu hóa đơn điện tử.',
      },
      high_intent: {
        title: 'Chênh lệch giá mua - bán (Spread) & Biểu đồ quy đổi giá thế giới',
        summary: 'Phân tích khoảng cách chênh lệch giá để tối ưu hóa thời điểm mua tích trữ hoặc chốt lời.',
        detail:
          'Cung cấp công thức quy đổi giá vàng thế giới (Kitco) sang giá vàng trong nước theo tỷ giá USD ngân hàng, phân tích biên độ chênh lệch mua vào - bán ra của các tiệm vàng lớn.',
        actionable_angle: 'Công cụ tính nhanh giá trị quy đổi cây vàng sang tiền mặt theo giá hiện hành.',
      },
    },
    cta_text: 'Xem Biểu Đồ Giá Vàng & Tỷ Giá Hôm Nay',
    deeplink: 'momo://gold-fx',
    umami_event: 'web_gold_fx_hub_btn_click',
  },

  financial_credit_score: {
    hub: 'Financial Hub',
    schema_type: 'FinancialService',
    schema_category: 'https://schema.org/FinancialService',
    mandatory_fields: [
      { field: 'name', desc: 'Dịch vụ tra cứu điểm tín dụng cá nhân.' },
      { field: 'provider', desc: 'Trung tâm Thông tin Tín dụng Quốc gia Việt Nam (CIC).' },
    ],
    direct_answer_text:
      'Điểm tín dụng cá nhân là chỉ số đánh giá mức độ uy tín tài chính và lịch sử thanh toán nợ của cá nhân, được quản lý tập trung bởi Trung tâm Thông tin Tín dụng Quốc gia (CIC - NHNN). Điểm tín dụng quyết định khả năng xét duyệt hạn mức, mở thẻ và lãi suất vay vốn tại toàn bộ các tổ chức tín dụng.',
    sample_jsonld: {
      '@context': 'https://schema.org',
      '@type': 'FinancialService',
      name: 'Tra Cứu Điểm Tín Dụng & Check Nợ Xấu CIC',
      provider: { '@type': 'GovernmentOrganization', name: 'Trung tâm Thông tin Tín dụng Quốc gia (CIC)' },
      areaServed: 'VN',
    },
    pillars: {
      expertise: {
        title: 'Phân loại 5 nhóm nợ CIC & Thời hạn xóa lịch sử nợ xấu',
        summary: 'Căn cứ pháp lý xếp hạng rủi ro tín dụng theo quy định của Ngân hàng Nhà nước.',
        detail:
          'Phân tích rõ: Nhóm 1 (Đủ tiêu chuẩn), Nhóm 2 (Cần chú ý - quá hạn 10 đến 90 ngày), Nhóm 3-5 (Nợ xấu - quá hạn trên 90 ngày). Lịch sử nợ xấu nhóm 3-5 được lưu trữ tối thiểu 5 năm kể từ ngày tất toán nợ.',
        actionable_angle: 'Bảng mốc thời gian xóa vết nợ xấu tương ứng với từng nhóm nợ trên hệ thống CIC.',
      },
      trust: {
        title: 'Cơ chế bảo mật dữ liệu thông tin tín dụng cá nhân',
        summary: 'Quy trình xác thực chính chủ theo Nghị định 13/2023/NĐ-CP về bảo vệ dữ liệu cá nhân.',
        detail:
          'Chỉ chủ thể dữ liệu mới có quyền yêu cầu trích xuất báo cáo tín dụng cá nhân thông qua mã OTP xác thực và căn cước công dân gắn chip, bảo vệ tuyệt đối bí mật tài chính.',
        actionable_angle: 'Quy trình khiếu nại đính chính thông tin khi phát hiện bị ghi nhận nợ xấu oan.',
      },
      high_intent: {
        title: 'Bảng đối chiếu điểm tín dụng với hạn mức phê duyệt hồ sơ vay',
        summary: 'Khung điểm số giúp người dùng dự đoán tỷ lệ đậu hồ sơ vay hoặc mở thẻ tín dụng.',
        detail:
          'Khung điểm CIC từ 400 đến 750+ điểm phản ánh cấp độ rủi ro tín dụng. Điểm từ 650+ trở lên thuộc nhóm rủi ro thấp, được ngân hàng duyệt hạn mức tối đa với lãi suất ưu đãi nhất.',
        actionable_angle: 'Cẩm nang 4 bước cải thiện điểm tín dụng trong vòng 3-6 tháng.',
      },
    },
    cta_text: 'Kiểm Tra Điểm Tín Dụng & Nợ Xấu Ngay',
    deeplink: 'momo://credit-score',
    umami_event: 'web_credit_score_hub_btn_click',
  },

  insurtech_motor: {
    hub: 'Insurtech Hub',
    schema_type: 'InsuranceProduct',
    schema_category: 'https://schema.org/InsuranceProduct',
    mandatory_fields: [
      { field: 'name', desc: 'Tên gói bảo hiểm xe máy hoặc ô tô.' },
      { field: 'provider', desc: 'Doanh nghiệp bảo hiểm phi nhân thọ được Bộ Tài chính cấp phép.' },
      { field: 'feesAndCommissionsSpecification', desc: 'Biểu phí chuẩn theo Nghị định 67/2023/NĐ-CP.' },
    ],
    direct_answer_text:
      'Bảo hiểm bắt buộc trách nhiệm dân sự của chủ xe cơ giới là loại hình bảo hiểm theo luật định nhằm bồi thường thiệt hại về tính mạng, sức khỏe (tối đa 150 triệu đồng/người/vụ) và tài sản cho bên thứ ba do xe cơ giới gây ra. Giấy chứng nhận bảo hiểm điện tử có mã QR có giá trị pháp lý tương đương thẻ giấy.',
    sample_jsonld: {
      '@context': 'https://schema.org',
      '@type': 'InsuranceProduct',
      name: 'Bảo Hiểm Xe Máy & Ô Tô Bắt Buộc (TNDS)',
      provider: { '@type': 'InsuranceAgency', name: 'Bảo Việt, PTI, PVI, MIC' },
      areaServed: 'VN',
    },
    pillars: {
      expertise: {
        title: 'Căn cứ pháp lý Nghị định 67/2023/NĐ-CP & Mức bồi thường 150 triệu',
        summary: 'Quy định bắt buộc tham gia bảo hiểm TNDS và mức phạt khi không xuất trình.',
        detail:
          'Hạn mức bồi thường thiệt hại về sức khỏe, tính mạng là 150 triệu đồng/người/vụ. Thiệt hại tài sản là 50 triệu/vụ (xe máy) hoặc 100 triệu/vụ (ô tô). Mức phạt khi không có bảo hiểm là 100-200k (xe máy) và 400-600k (ô tô).',
        actionable_angle: 'Bảng đối chiếu mức phí chuẩn và khung bồi thường bảo hiểm TNDS bắt buộc.',
      },
      trust: {
        title: 'Giấy chứng nhận bảo hiểm điện tử tích hợp mã QR chuẩn Bộ Tài chính',
        summary: 'Cơ chế xuất trình giấy chứng nhận số hóa cho Cảnh sát Giao thông khi kiểm tra.',
        detail:
          'Giấy chứng nhận điện tử được lưu trữ trên ứng dụng ví điện tử kèm mã QR tra cứu trực tiếp dữ liệu từ Hiệp hội Bảo hiểm Việt Nam, hoàn toàn hợp lệ khi lực lượng chức năng kiểm tra.',
        actionable_angle: 'Hướng dẫn xuất trình giấy chứng nhận bảo hiểm điện tử trên điện thoại.',
      },
      high_intent: {
        title: 'Quy trình lập hồ sơ giám định hiện trường & Thời hạn giải quyết bồi thường',
        summary: 'Các bước cần làm khi xảy ra tai nạn để được doanh nghiệp bảo hiểm chi trả nhanh.',
        detail:
          'Hướng dẫn: Giữ nguyên hiện trường, gọi hotline bảo hiểm trong vòng 1 giờ, chụp ảnh góc rộng, phối hợp biên bản CSGT. Doanh nghiệp bảo hiểm có trách nhiệm tạm ứng bồi thường trong vòng 3 ngày làm việc.',
        actionable_angle: 'Checklist 5 tài liệu cần có trong hồ sơ yêu cầu bồi thường bảo hiểm xe.',
      },
    },
    cta_text: 'Mua Bảo Hiểm Xe Nhận Thẻ Điện Tử Ngay',
    deeplink: 'momo://motor-insurance',
    umami_event: 'web_motor_insurance_hub_btn_click',
  },

  insurtech_social_health: {
    hub: 'Insurtech Hub',
    schema_type: 'GovernmentService',
    schema_category: 'https://schema.org/GovernmentService',
    mandatory_fields: [
      { field: 'name', desc: 'Dịch vụ tra cứu và đóng bảo hiểm y tế / xã hội.' },
      { field: 'provider', desc: 'Bảo hiểm Xã hội Việt Nam (BHXH).' },
    ],
    direct_answer_text:
      'Bảo hiểm Y tế (BHYT) và Bảo hiểm Xã hội (BHXH) là các chính sách an sinh xã hội trụ cột do Nhà nước tổ chức, giúp người tham gia giảm gánh nặng chi phí khám chữa bệnh (chi trả đến 100% đúng tuyến) hoặc nhận trợ cấp thai sản, ốm đau, hưu trí. Hệ thống hỗ trợ gia hạn BHYT hộ gia đình và đóng BHXH tự nguyện online.',
    sample_jsonld: {
      '@context': 'https://schema.org',
      '@type': 'GovernmentService',
      name: 'Dịch Vụ Đóng & Gia Hạn BHYT / BHXH Trực Tuyến',
      provider: { '@type': 'GovernmentOrganization', name: 'Bảo hiểm Xã hội Việt Nam' },
      areaServed: 'VN',
    },
    pillars: {
      expertise: {
        title: 'Mức hưởng khám chữa bệnh đúng tuyến & Quyền lợi 5 năm liên tục',
        summary: 'Căn cứ Luật BHYT về tỷ lệ thanh toán viện phí và danh mục kỹ thuật cao.',
        detail:
          'Người tham gia BHYT được chi trả từ 80% đến 100% chi phí khám đúng tuyến. Khi tham gia 5 năm liên tục và có số tiền cùng chi trả trong năm lớn hơn 6 tháng lương cơ sở, người bệnh được quỹ BHYT chi trả 100% chi phí còn lại.',
        actionable_angle: 'Bảng đối chiếu mức hưởng BHYT đúng tuyến vs trái tuyến tại các tuyến bệnh viện.',
      },
      trust: {
        title: 'Tích hợp thẻ BHYT số trên VssID và VNeID mức độ 2',
        summary: 'Không cần mang thẻ BHYT giấy khi đi khám chữa bệnh tại các cơ sở y tế toàn quốc.',
        detail:
          'Hình ảnh thẻ BHYT trên ứng dụng VssID và tích hợp trên VNeID mức 2 có giá trị tương đương thẻ giấy tại 100% cơ sở khám chữa bệnh công lập và tư nhân có ký hợp đồng BHYT.',
        actionable_angle: 'Hướng dẫn 3 bước xuất trình thẻ BHYT điện tử trên ứng dụng VNeID.',
      },
      high_intent: {
        title: 'Mức đóng lũy tiến BHYT hộ gia đình & Cách tính tiền rút BHXH 1 lần',
        summary: 'Công thức tính số tiền đóng giảm trừ cho người thứ 2, 3, 4 trong gia đình.',
        detail:
          'Mức đóng BHYT hộ gia đình: Người thứ 1 đóng 100%, người thứ 2 đóng 70%, người thứ 3 đóng 60%, người thứ 4 đóng 50%, người thứ 5 trở đi đóng 40% mức của người thứ nhất. Công thức tính BHXH 1 lần dựa trên mức bình quân tiền lương đóng.',
        actionable_angle: 'Bảng tính tiền đóng BHYT hộ gia đình cho hộ 3, 4, 5 thành viên chuẩn 2026.',
      },
    },
    cta_text: 'Đóng Tiếp & Gia Hạn BHYT Hộ Gia Đình Online',
    deeplink: 'momo://bhyt',
    umami_event: 'web_bhyt_hub_btn_click',
  },

  vehicle_traffic_fines: {
    hub: 'Vehicle Hub',
    schema_type: 'GovernmentService',
    schema_category: 'https://schema.org/GovernmentService',
    mandatory_fields: [
      { field: 'name', desc: 'Dịch vụ tra cứu và nộp phạt vi phạm giao thông.' },
      { field: 'provider', desc: 'Cục Cảnh sát Giao thông (Bộ Công an).' },
      { field: 'serviceType', desc: 'Dịch vụ công trực tuyến / Tra cứu vi phạm hành chính.' },
    ],
    direct_answer_text:
      'Phạt nguội là hình thức xử phạt vi phạm hành chính trong lĩnh vực giao thông đường bộ được ghi nhận thông qua hệ thống camera giám sát tự động của Cục Cảnh sát Giao thông. Chủ phương tiện có thể tra cứu thông tin lỗi, địa điểm và hình ảnh vi phạm trực tuyến, từ đó chủ động nộp phạt trước khi bị cảnh báo đăng kiểm.',
    sample_jsonld: {
      '@context': 'https://schema.org',
      '@type': 'GovernmentService',
      name: 'Tra Cứu & Nộp Phạt Nguội Giao Thông MoMo',
      provider: { '@type': 'GovernmentOrganization', name: 'Cục Cảnh sát Giao thông (Bộ Công an)' },
      serviceType: 'Dịch vụ công trực tuyến',
      areaServed: 'VN',
    },
    pillars: {
      expertise: {
        title: 'Thời hạn xử phạt & Quy định tạm dừng đăng kiểm phương tiện',
        summary: 'Hệ quả pháp lý khi không chấp hành quyết định xử phạt nguội theo Nghị định 100/123.',
        detail:
          'Sau 20 ngày kể từ ngày gửi thông báo vi phạm, nếu chủ phương tiện không giải quyết, CSGT sẽ gửi cảnh báo lên hệ thống Cục Đăng kiểm. Phương tiện sẽ chỉ được cấp tem kiểm định tạm 15 ngày.',
        actionable_angle: 'Mốc thời gian 3 giai đoạn xử lý phạt nguội từ lúc vi phạm đến khi bị khóa đăng kiểm.',
      },
      trust: {
        title: 'Nguồn dữ liệu đối soát trực tiếp từ Cục CSGT',
        summary: 'Xác thực độ chuẩn xác của kết quả tra cứu dựa trên cổng dữ liệu csgt.vn.',
        detail:
          'Dữ liệu tra cứu được đồng bộ từ cơ sở dữ liệu xử lý vi phạm của Cục Cảnh sát Giao thông, đảm bảo tính chuẩn xác và loại trừ các website câu view giả mạo.',
        actionable_angle: 'Hướng dẫn kiểm tra mã quyết định xử phạt thật và đối chiếu số biên bản vi phạm.',
      },
      high_intent: {
        title: 'Quy trình nộp phạt online không cần đến cơ quan công an',
        summary: 'Hướng dẫn từng bước thanh toán tiền phạt trực tuyến và xóa cảnh báo đăng kiểm.',
        detail:
          'Hướng dẫn lấy mã số biên bản điện tử, thanh toán qua cổng Dịch vụ công Quốc gia hoặc ví điện tử, hệ thống tự động truyền dữ liệu giải tỏa cảnh báo sang Cục Đăng kiểm trong vòng 24-48 giờ.',
        actionable_angle: 'Sơ đồ 4 bước nộp phạt nguội tại nhà và cơ chế tự động xóa cảnh báo đăng kiểm.',
      },
    },
    cta_text: 'Tra Cứu Phạt Nguội Toàn Quốc Ngay',
    deeplink: 'momo://traffic-fine',
    umami_event: 'web_traffic_fine_lookup_btn_click',
  },

  vehicle_registration_plate: {
    hub: 'Vehicle Hub',
    schema_type: 'GovernmentService',
    schema_category: 'https://schema.org/GovernmentService',
    mandatory_fields: [
      { field: 'name', desc: 'Dịch vụ tra cứu biển số xe và hướng dẫn thủ tục sang tên.' },
      { field: 'provider', desc: 'Phòng Cảnh sát Giao thông (Bộ Công an).' },
    ],
    direct_answer_text:
      'Biển số định danh là biển số xe được cấp và quản lý theo mã định danh cá nhân của chủ phương tiện theo Thông tư 24/2023/TT-BCA. Chủ xe có thể tra cứu mã vùng biển số 63 tỉnh thành, tham gia đấu giá biển số đẹp trực tuyến và thực hiện thủ tục thu hồi, sang tên đổi chủ minh bạch.',
    sample_jsonld: {
      '@context': 'https://schema.org',
      '@type': 'GovernmentService',
      name: 'Tra Cứu Biển Số Xe & Hướng Dẫn Sang Tên Đổi Chủ',
      provider: { '@type': 'GovernmentOrganization', name: 'Phòng Cảnh sát Giao thông' },
      areaServed: 'VN',
    },
    pillars: {
      expertise: {
        title: 'Thông tư 24/2023/TT-BCA về cơ chế quản lý biển số định danh',
        summary: 'Nguyên tắc cấp biển theo chủ sở hữu và quy định giữ biển số 5 năm khi bán xe.',
        detail:
          'Khi chuyển nhượng, tặng cho xe, chủ xe bắt buộc phải giữ lại đăng ký, biển số nộp lại cho công an để làm thủ tục thu hồi. Cơ quan công an giữ lại biển số định danh trong kho 5 năm để cấp lại khi chủ xe mua xe mới.',
        actionable_angle: 'Sơ đồ quy trình 4 bước thu hồi biển số định danh và sang tên chính chủ.',
      },
      trust: {
        title: 'Cổng đấu giá biển số trực tuyến chính thức VPA (Bộ Công an)',
        summary: 'Quy chế đấu giá minh bạch, tiền đặt trước và hợp đồng xác nhận trúng đấu giá.',
        detail:
          'Toàn bộ các phiên đấu giá biển số đẹp đều diễn ra trên trang web của Công ty Đấu giá Hợp danh Việt Nam (vpa.com.vn) dưới sự giám sát trực tiếp của Bộ Công an, tiền cọc 40 triệu đồng được bảo toàn theo luật.',
        actionable_angle: 'Checklist điều kiện tham gia đấu giá và nhận biển số trúng đấu giá hợp lệ.',
      },
      high_intent: {
        title: 'Bảng lệ phí cấp biển theo khu vực & Chi phí thuế trước bạ khi sang tên',
        summary: 'Bóc tách chi phí ra biển số mới tại Hà Nội/TP.HCM (20 triệu) vs các tỉnh thành khác.',
        detail:
          'Cung cấp bảng biểu phí cấp mới biển số theo khu vực I, II, III; mức thuế trước bạ xe cũ (2%) và công thức tính khấu hao giá trị xe để tính đúng số tiền nộp tại Chi cục Thuế.',
        actionable_angle: 'Bảng tính tổng chi phí lăn bánh và sang tên đổi chủ xe máy, ô tô.',
      },
    },
    cta_text: 'Tra Cứu Biển Số Xe 63 Tỉnh Thành',
    deeplink: 'momo://vehicle-plate',
    umami_event: 'web_vehicle_plate_hub_btn_click',
  },

  cinema_movie: {
    hub: 'Cinema Hub',
    schema_type: 'Movie',
    schema_category: 'https://schema.org/Movie',
    mandatory_fields: [
      { field: 'name', desc: 'Tên phim chính xác theo giấy phép phát hành rạp.' },
      { field: 'duration', desc: 'Thời lượng phim chuẩn định dạng ISO 8601 (ví dụ: PT120M).' },
      { field: 'contentRating', desc: 'Phân loại độ tuổi chính thức (P, K, T13, T16, T18, C).' },
      { field: 'aggregateRating', desc: 'Điểm đánh giá từ khán giả và chuyên môn.' },
    ],
    direct_answer_text:
      'Lịch chiếu phim rạp là dịch vụ tổng hợp thời gian chiếu, sơ đồ ghế ngồi và giá vé theo thời gian thực của toàn bộ các cụm rạp trên toàn quốc (CGV, Lotte Cinema, Galaxy, BHD, Beta, Cinestar). Người xem có thể tra cứu suất chiếu gần nhất, so sánh giá vé và đặt vé online nhận mã QR vào thẳng phòng chiếu.',
    sample_jsonld: {
      '@context': 'https://schema.org',
      '@type': 'Movie',
      name: 'Lịch Chiếu Phim Rạp Toàn Quốc MoMo',
      description: 'Tổng hợp lịch chiếu, giá vé và đặt vé rạp CGV, Lotte, Galaxy, BHD.',
      areaServed: 'VN',
    },
    pillars: {
      expertise: {
        title: 'Quy chuẩn phân loại độ tuổi điện ảnh quốc gia (Cục Điện Ảnh)',
        summary: 'Quy định kiểm soát độ tuổi và giấy tờ tùy thân bắt buộc khi vào phòng chiếu.',
        detail:
          'Phân tích 6 nhãn phân loại: P, K, T13, T16, T18, C theo Thông tư 05/2023/TT-BVHTTDL. Nhân viên rạp có quyền từ chối khán giả không xuất trình được CCCD/VNeID chứng minh đủ tuổi và không hoàn tiền vé.',
        actionable_angle: 'Bảng giải mã 6 nhãn độ tuổi và quy định giấy tờ hợp lệ vào phòng chiếu.',
      },
      trust: {
        title: 'Cơ chế giữ chỗ & Đồng bộ sơ đồ ghế thời gian thực (Live Seat Map)',
        summary: 'Hạ tầng kết nối API trực tiếp với hệ thống bán vé của từng cụm rạp.',
        detail:
          'Hệ thống tự động khóa ghế tức thì trong 5-10 phút khi người dùng chuyển sang bước thanh toán, ngăn chặn tuyệt đối tình trạng trùng ghế (double booking) giữa các kênh mua vé.',
        actionable_angle: 'Quy trình nhận vé điện tử Smart Ticket QR vào thẳng phòng chiếu không cần in vé giấy.',
      },
      high_intent: {
        title: 'Bảng phụ thu phòng chiếu đặc biệt & Chính sách hoàn hủy vé',
        summary: 'Bóc tách mức giá phụ thu định dạng IMAX, 4DX, ScreenX và ghế Sweetbox.',
        detail:
          'Liệt kê chi tiết: Phụ thu ngày Lễ/Tết, phụ thu suất chiếu cuối tuần, phụ thu định dạng âm thanh Dolby Atmos và chính sách đổi trả suất chiếu của từng chuỗi rạp lớn.',
        actionable_angle: 'Bảng đối chiếu giá vé tiêu chuẩn vs định dạng cao cấp tại Hà Nội và TP.HCM.',
      },
    },
    cta_text: 'Xem Lịch Chiếu & Đặt Vé Xem Phim Ngay',
    deeplink: 'momo://cinema',
    umami_event: 'web_cinema_hub_btn_click',
  },

  ota_travel_transit: {
    hub: 'OTA Hub',
    schema_type: 'TravelAction',
    schema_category: 'https://schema.org/TravelAction',
    mandatory_fields: [
      { field: 'name', desc: 'Tên dịch vụ vận chuyển hoặc hành trình du lịch.' },
      { field: 'provider', desc: 'Hãng hàng không, đường sắt hoặc đối tác lữ hành.' },
    ],
    direct_answer_text:
      'Vé máy bay, tàu hỏa và du lịch trực tuyến là nền tảng so sánh giá vé, tìm kiếm hành trình tối ưu và đặt chỗ lưu trú từ các đối tác hàng không (Vietnam Airlines, Vietjet, Bamboo) và Tổng công ty Đường sắt Việt Nam. Người dùng nhận mã đặt chỗ (PNR) tức thì với nhiều ưu đãi tích lũy dặm bay.',
    sample_jsonld: {
      '@context': 'https://schema.org',
      '@type': 'TravelAction',
      name: 'Đặt Vé Máy Bay & Du Lịch MoMo Travel',
      provider: { '@type': 'Organization', name: 'Vietnam Airlines, Vietjet Air, VNR' },
      areaServed: 'VN',
    },
    pillars: {
      expertise: {
        title: 'Quy định vé điện tử PNR & Điều kiện hoàn đổi vé theo từng hạng vé',
        summary: 'Tiêu chuẩn hàng không dân dụng và chính sách hành lý xách tay, ký gửi.',
        detail:
          'Làm rõ quy định về mã đặt chỗ (PNR), điều kiện đổi giờ bay, hoàn vé đối với hạng vé Phổ thông tiết kiệm vs Thương gia, cùng mức phí chênh lệch và thuế phí sân bay do Cục Hàng không quy định.',
        actionable_angle: 'Bảng tổng hợp quy định hành lý xách tay và phí đổi vé của 4 hãng hàng không nội địa.',
      },
      trust: {
        title: 'Kết nối API trực tiếp hệ thống bán vé của các hãng vận chuyển',
        summary: 'Xuất vé tức thì, đảm bảo mã đặt chỗ thật và đối soát thông tin chuyến bay 24/7.',
        detail:
          'Hệ thống kết nối trực tiếp với cổng phân phối vé chính thức (GDS), loại trừ hoàn toàn nguy cơ vé giả hoặc bị đại lý trung gian chiếm dụng mã chỗ.',
        actionable_angle: 'Hướng dẫn 3 bước kiểm tra mã vé PNR trực tiếp trên website của hãng bay.',
      },
      high_intent: {
        title: 'Kinh nghiệm săn vé máy bay giá rẻ & Bảng phụ thu dịch vụ bổ sung',
        summary: 'Thời điểm vàng đặt vé và cách tránh các khoản phụ thu chọn chỗ ngồi, suất ăn không cần thiết.',
        detail:
          'Phân tích biểu đồ biến động giá vé theo mùa vụ (Tết, hè, dịp lễ), hướng dẫn mẹo đặt vé trước 3-4 tuần và bảng bóc tách chi phí phụ thu để người dùng tiết kiệm tối đa chi phí đi lại.',
        actionable_angle: 'Lịch mùa vụ giá vé máy bay và cẩm nang săn vé 0 đồng trong năm.',
      },
    },
    cta_text: 'Săn Vé Máy Bay & Tàu Xe Giá Rẻ',
    deeplink: 'momo://travel',
    umami_event: 'web_travel_hub_btn_click',
  },

  telco_data_sim: {
    hub: 'Telco Hub',
    schema_type: 'Service',
    schema_category: 'https://schema.org/Service',
    mandatory_fields: [
      { field: 'name', desc: 'Tên gói cước 4G/5G hoặc dịch vụ nạp thẻ.' },
      { field: 'provider', desc: 'Nhà mạng viễn thông (Viettel, VinaPhone, MobiFone...).' },
    ],
    direct_answer_text:
      'Nạp tiền điện thoại và gói cước data 4G/5G là tiện ích viễn thông số cho phép người dùng nạp tiền trực tiếp vào tài khoản di động, đăng ký gói dung lượng tốc độ cao và mua eSIM du lịch quốc tế kết nối trực tiếp với các nhà mạng lớn tại Việt Nam, xử lý tự động 24/7 với chiết khấu cạnh tranh.',
    sample_jsonld: {
      '@context': 'https://schema.org',
      '@type': 'Service',
      name: 'Nạp Data 4G & Mua Thẻ Điện Thoại MoMo',
      provider: { '@type': 'Organization', name: 'Viettel, VinaPhone, MobiFone' },
      areaServed: 'VN',
    },
    pillars: {
      expertise: {
        title: 'Quy định chuẩn hóa thông tin thuê bao di động (Nghị định 49)',
        summary: 'Chính sách quản lý SIM chính chủ và phòng chống SIM rác của Bộ Thông tin & Truyền thông.',
        detail:
          'Thuê bao di động bắt buộc phải khớp đúng thông tin với CSDL Quốc gia về dân cư. Dịch vụ nạp tiền và gói cước hỗ trợ các SIM chính chủ duy trì hoạt động hai chiều và tích lũy điểm thưởng nhà mạng.',
        actionable_angle: 'Cú pháp kiểm tra thông tin thuê bao chính chủ TTTB gửi 1414 của các nhà mạng.',
      },
      trust: {
        title: 'Kết nối API trực tiếp cổng nạp nhà mạng viễn thông',
        summary: 'Cộng tiền và kích hoạt gói data tức thì trong vòng 3-10 giây với bảo mật tuyệt đối.',
        detail:
          'Giao dịch được xử lý qua kênh kết nối bảo mật trực tiếp với hạ tầng kỹ thuật của Viettel, VNPT, MobiFone, đảm bảo tiền và dung lượng data vào tài khoản ngay lập tức mà không sợ lộ mã thẻ.',
        actionable_angle: 'Quy trình đối soát tự động hoàn tiền trong 5 phút khi hệ thống nhà mạng nghẽn.',
      },
      high_intent: {
        title: 'Bảng đối chiếu giá cước data theo ngày/tháng & Tỷ lệ chiết khấu nạp tiền',
        summary: 'So sánh chi phí giữa nạp tiền thông thường vs đăng ký gói cước dung lượng trọn gói.',
        detail:
          'Phân tích chi tiết: Gói cước ngày 1-3GB/ngày thích hợp cho nhu cầu ngắn hạn; gói cước tháng 60-120GB/tháng tiết kiệm tới 60% chi phí. Bảng chiết khấu nạp tiền trực tiếp từ 3% đến 10%.',
        actionable_angle: 'Bảng ma trận chọn gói cước 4G/5G tối ưu theo nhu cầu lướt web, xem video, chơi game.',
      },
    },
    cta_text: 'Nạp Data 4G & Tiền Điện Thoại Chiết Khấu Cao',
    deeplink: 'momo://telco',
    umami_event: 'web_telco_hub_btn_click',
  },

  hospital_health: {
    hub: 'Hospital Hub',
    schema_type: 'MedicalWebPage',
    schema_category: 'https://schema.org/MedicalWebPage',
    mandatory_fields: [
      { field: 'name', desc: 'Dịch vụ đặt lịch khám bệnh trực tuyến.' },
      { field: 'provider', desc: 'Bệnh viện hoặc phòng khám đa khoa được cấp phép.' },
    ],
    direct_answer_text:
      'Đặt lịch khám bệnh trực tuyến là tiện ích y tế thông minh hỗ trợ người bệnh tra cứu chuyên khoa, chọn bác sĩ và đăng ký khung giờ khám trước tại các bệnh viện tuyến đầu, giúp nhận phiếu tiếp đón điện tử, rút ngắn 50-70% thời gian chờ đợi và tích hợp thanh toán viện phí không tiền mặt.',
    sample_jsonld: {
      '@context': 'https://schema.org',
      '@type': 'MedicalWebPage',
      name: 'Đặt Lịch Khám Bệnh & Bệnh Viện Trực Tuyến MoMo',
      provider: { '@type': 'MedicalOrganization', name: 'Mạng lưới Bệnh viện Tuyến đầu' },
      areaServed: 'VN',
    },
    pillars: {
      expertise: {
        title: 'Luật Khám bệnh, chữa bệnh & Tiêu chuẩn chuyển đổi số ngành y tế',
        summary: 'Quy chuẩn an toàn y tế và giá trị pháp lý của hồ sơ bệnh án điện tử.',
        detail:
          'Quy định về quyền của người bệnh trong việc lựa chọn chuyên khoa và bác sĩ điều trị. Nền tảng tuân thủ đề án bệnh viện thông minh, hỗ trợ liên thông kết quả xét nghiệm và đơn thuốc điện tử.',
        actionable_angle: 'Quy trình chuyển tuyến khám chữa bệnh và thủ tục tiếp đón bệnh nhân BHYT.',
      },
      trust: {
        title: 'Bảo mật hồ sơ sức khỏe cá nhân & Mã số tiếp đón ưu tiên',
        summary: 'Dữ liệu y tế được mã hóa đa tầng, kết nối trực tiếp với phần mềm quản lý bệnh viện (HIS).',
        detail:
          'Thông tin cá nhân và triệu chứng sức khỏe được mã hóa theo tiêu chuẩn HIPAA y khoa. Mã QR tiếp đón điện tử giúp bệnh nhân vào thẳng phòng khám không cần xếp hàng lấy số thứ tự tại sảnh.',
        actionable_angle: 'Sơ đồ luồng tiếp đón ưu tiên tại viện cho bệnh nhân đặt lịch trực tuyến.',
      },
      high_intent: {
        title: 'Bảng giá khám dịch vụ vs khám BHYT & Hướng dẫn thanh toán viện phí',
        summary: 'Bóc tách chi phí khám theo yêu cầu, chọn chuyên gia đầu ngành và thanh toán tạm ứng.',
        detail:
          'Bảng so sánh chi phí giữa khám thường, khám BHYT và khám dịch vụ VIP tại các bệnh viện công lập lớn. Hướng dẫn nộp tạm ứng và tất toán viện phí trực tuyến không cần xếp hàng tại quầy thu ngân.',
        actionable_angle: 'Cẩm nang chuẩn bị giấy tờ và lưu ý nhịn ăn sáng khi đi khám tổng quát.',
      },
    },
    cta_text: 'Đặt Lịch Khám Bệnh Trực Tuyến',
    deeplink: 'momo://hospital',
    umami_event: 'web_hospital_hub_btn_click',
  },

  student_education: {
    hub: 'Student Hub',
    schema_type: 'EducationalOccupationalCredential',
    schema_category: 'https://schema.org/Course',
    mandatory_fields: [
      { field: 'name', desc: 'Thông tin tuyển sinh, điểm chuẩn hoặc học phí trường đại học.' },
      { field: 'provider', desc: 'Trường Đại học / Cao đẳng được Bộ GD&ĐT cấp phép.' },
    ],
    direct_answer_text:
      'Cổng thông tin sinh viên và tuyển sinh đại học là chuyên trang tổng hợp điểm chuẩn xét tuyển, đề án tuyển sinh, biểu phí đào tạo và các gói học bổng, vay vốn sinh viên ưu đãi cho toàn bộ các trường đại học, cao đẳng trên cả nước, giúp học sinh và phụ huynh định hướng nghề nghiệp vững vàng.',
    sample_jsonld: {
      '@context': 'https://schema.org',
      '@type': 'EducationalOccupationalCredential',
      name: 'Tra Cứu Điểm Chuẩn & Tuyển Sinh Đại Học MoMo',
      provider: { '@type': 'EducationalOrganization', name: 'Bộ Giáo dục và Đào tạo & Hệ thống ĐH-CĐ' },
      areaServed: 'VN',
    },
    pillars: {
      expertise: {
        title: 'Quy chế tuyển sinh đại học quốc gia & Khung học phí Nghị định 97',
        summary: 'Căn cứ pháp lý về các phương thức xét tuyển và trần học phí trường công lập.',
        detail:
          'Quy chế tuyển sinh của Bộ GD&ĐT về xét tuyển thẳng, điểm thi tốt nghiệp THPT, học bạ và bài thi đánh giá năng lực ĐHQG. Khung học phí các khối ngành theo Nghị định 97/2023/NĐ-CP của Chính phủ.',
        actionable_angle: 'Bảng đối chiếu 4 phương thức xét tuyển đại học phổ biến và cách quy đổi điểm.',
      },
      trust: {
        title: 'Nguồn dữ liệu đề án tuyển sinh chính thức từ các trường đại học',
        summary: 'Dữ liệu được trích xuất từ đề án tuyển sinh công khai đã đăng ký với Bộ GD&ĐT.',
        detail:
          'Toàn bộ thông tin chỉ tiêu, tổ hợp môn xét tuyển và mức học phí từng kỳ được cập nhật trực tiếp từ văn bản công bố chính thức của Hội đồng tuyển sinh các trường, loại bỏ tin đồn thất thiệt.',
        actionable_angle: 'Checklist các mốc thời gian đăng ký nguyện vọng và nộp lệ phí tuyển sinh quốc gia.',
      },
      high_intent: {
        title: 'Bảng đối chiếu điểm chuẩn 3 năm & Gói tín dụng vay vốn sinh viên',
        summary: 'Dự đoán biến động điểm chuẩn ngành hot và hướng dẫn vay vốn học tập lãi suất thấp.',
        detail:
          'Thống kê xu hướng điểm chuẩn các khối ngành Công nghệ thông tin, Kinh tế, Y dược qua 3 năm gần nhất. Hướng dẫn hồ sơ vay vốn ưu đãi sinh viên qua Ngân hàng Chính sách Xã hội mức 4 triệu đồng/tháng.',
        actionable_angle: 'Bảng ma trận điểm chuẩn 3 năm và công cụ tính toán chi phí sinh hoạt sinh viên.',
      },
    },
    cta_text: 'Tra Cứu Điểm Chuẩn & Tuyển Sinh Đại Học',
    deeplink: 'momo://student',
    umami_event: 'web_student_hub_btn_click',
  },

  lottery_vietlott: {
    hub: 'Lottery Hub',
    schema_type: 'GovernmentService',
    schema_category: 'https://schema.org/GovernmentService',
    mandatory_fields: [
      { field: 'name', desc: 'Dịch vụ tra cứu kết quả xổ số kiến thiết và Vietlott.' },
      { field: 'provider', desc: 'Hội đồng Xổ số Kiến thiết 3 Miền & Công ty Vietlott.' },
    ],
    direct_answer_text:
      'Kết quả xổ số kiến thiết 3 miền và Vietlott trực tuyến là tiện ích tường thuật trực tiếp kết quả mở thưởng xổ số Miền Bắc, Miền Trung, Miền Nam và các kỳ quay thưởng Mega 6/45, Power 6/55 theo thời gian thực từ các hội đồng quay số chính thức, hỗ trợ dò vé nhanh và hướng dẫn thủ tục lĩnh thưởng bảo mật.',
    sample_jsonld: {
      '@context': 'https://schema.org',
      '@type': 'GovernmentService',
      name: 'Tra Cứu Kết Quả Xổ Số Kiến Thiết & Vietlott Trực Tuyến',
      provider: { '@type': 'Organization', name: 'Công ty Xổ số Kiến thiết & Vietlott' },
      areaServed: 'VN',
    },
    pillars: {
      expertise: {
        title: 'Quy chế giám sát quay số mở thưởng của Bộ Tài chính',
        summary: 'Căn cứ pháp lý về tính minh bạch của hội đồng giám sát và nghĩa vụ thuế TNCN.',
        detail:
          'Quá trình quay thưởng được giám sát nghiêm ngặt bởi Hội đồng Giám sát Xổ số gồm đại diện Sở Tài chính, Công an, Thanh tra Nhà nước. Khoản tiền trúng thưởng trên 10 triệu đồng chịu thuế TNCN 10%.',
        actionable_angle: 'Bảng tính số tiền thuế TNCN thực tế phải nộp tương ứng với các mức trúng thưởng.',
      },
      trust: {
        title: 'Tường thuật trực tiếp đồng bộ thời gian thực từ trường quay',
        summary: 'Kết quả số mở thưởng cập nhật từng giải song song với sóng truyền hình.',
        detail:
          'Dữ liệu số trúng thưởng được truyền trực tiếp từ trường quay của các công ty XSKT vào các khung giờ cố định: 16h15 (Miền Nam), 17h15 (Miền Trung), 18h15 (Miền Bắc) và 18h00 (Vietlott).',
        actionable_angle: 'Quy trình kiểm tra tính toàn vẹn của tờ vé số hợp lệ trước khi lĩnh thưởng.',
      },
      high_intent: {
        title: 'Quy trình lĩnh thưởng bảo mật & Danh sách đại lý chi trả chính thức',
        summary: 'Thời hạn 30 ngày lĩnh thưởng và các giấy tờ cần xuất trình để nhận tiền an toàn.',
        detail:
          'Vé trúng thưởng phải còn nguyên vẹn, không rách rời, không chắp vá, thời hạn lĩnh thưởng trong vòng 30 ngày. Hướng dẫn nhận tiền mặt hoặc chuyển khoản tại trụ sở công ty xổ số hoặc đại lý ủy quyền.',
        actionable_angle: 'Checklist 4 bước nhận thưởng giải đặc biệt và bảo mật danh tính người trúng.',
      },
    },
    cta_text: 'Dò Vé Số & Xem Kết Quả Mở Thưởng Ngay',
    deeplink: 'momo://lottery',
    umami_event: 'web_lottery_hub_btn_click',
  },
};

/**
 * Hàm phân giải Geo Blueprint thông minh theo Theme ID, Theme Name và Sector
 */
export function getGeoEntityBlueprint(themeId: string, themeName: string, sector?: string): GeoEntityBlueprint {
  const normId = themeId.toLowerCase().replace(/[^a-z0-9]/g, '');
  const normName = themeName.toLowerCase();
  const text = `${normId} ${normName}`;

  // 1. Phân giải theo Ontology Archetypes chuyên sâu
  if (text.includes('tietkiem') || text.includes('laisuat') || text.includes('tichluy') || text.includes('tiengui')) {
    const item = DOMAIN_ONTOLOGY_REGISTRY.financial_savings;
    return { ...item, theme: themeName, word_count: item.direct_answer_text.split(/\s+/).length };
  }
  if (text.includes('vitrasau') || text.includes('muatruoctrasau') || text.includes('paylater') || text.includes('tragop')) {
    const item = DOMAIN_ONTOLOGY_REGISTRY.financial_credit_paylater;
    return { ...item, theme: themeName, word_count: item.direct_answer_text.split(/\s+/).length };
  }
  if (text.includes('diemtindung') || text.includes('noxau') || text.includes('cic')) {
    const item = DOMAIN_ONTOLOGY_REGISTRY.financial_credit_score;
    return { ...item, theme: themeName, word_count: item.direct_answer_text.split(/\s+/).length };
  }
  if (text.includes('vay') || text.includes('tinchap') || text.includes('thechap') || text.includes('laivay') || text.includes('thauchi')) {
    const item = DOMAIN_ONTOLOGY_REGISTRY.financial_consumer_loan;
    return { ...item, theme: themeName, word_count: item.direct_answer_text.split(/\s+/).length };
  }
  if (text.includes('giavang') || text.includes('vang') || text.includes('tygia') || text.includes('ngoai te') || text.includes('doitien') || text.includes('kieuhoi')) {
    const item = DOMAIN_ONTOLOGY_REGISTRY.financial_gold_fx;
    return { ...item, theme: themeName, word_count: item.direct_answer_text.split(/\s+/).length };
  }
  if (text.includes('chungkhoan') || text.includes('cophieu') || text.includes('traiphieu') || text.includes('chungchiquy') || text.includes('quyetf') || text.includes('dautu')) {
    return {
      ...DOMAIN_ONTOLOGY_REGISTRY.financial_savings,
      schema_type: 'InvestmentOrDeposit',
      schema_category: 'https://schema.org/InvestmentOrDeposit',
      theme: themeName,
      direct_answer_text: `${themeName} là giải pháp đầu tư và tích lũy tài chính số được giám sát bởi Ủy ban Chứng khoán Nhà nước (UBCKNN), cho phép nhà đầu tư cá nhân giao dịch minh bạch, theo dõi giá trị tài sản ròng (NAV) và tối ưu hóa lợi nhuận danh mục với tính thanh khoản cao.`,
      word_count: 45,
    };
  }
  if (text.includes('thuetncn') || text.includes('masothue') || text.includes('tinhluong') || text.includes('thue')) {
    return {
      ...DOMAIN_ONTOLOGY_REGISTRY.financial_credit_score,
      schema_type: 'FinancialService',
      theme: themeName,
      direct_answer_text: `${themeName} là công cụ tính toán và đối soát nghĩa vụ thuế trực tuyến, hỗ trợ người nộp thuế xác định chính xác số thuế TNCN theo biểu thuế lũy tiến từng phần, áp dụng đầy đủ các mức giảm trừ gia cảnh và bảo hiểm bắt buộc theo đúng quy định của Bộ Tài chính.`,
      word_count: 48,
    };
  }
  if (text.includes('baohiemxemay') || text.includes('baohiemoto') || text.includes('tnds') || text.includes('thanvo')) {
    const item = DOMAIN_ONTOLOGY_REGISTRY.insurtech_motor;
    return { ...item, theme: themeName, word_count: item.direct_answer_text.split(/\s+/).length };
  }
  if (text.includes('bhyt') || text.includes('bhxh') || text.includes('baohiemnhantho') || text.includes('baohiemtainan') || text.includes('baohiemchayno')) {
    const item = DOMAIN_ONTOLOGY_REGISTRY.insurtech_social_health;
    return { ...item, theme: themeName, word_count: item.direct_answer_text.split(/\s+/).length };
  }
  if (text.includes('phatnguoi') || text.includes('loigiaothong') || text.includes('dangkiem') || text.includes('banglaixe')) {
    const item = DOMAIN_ONTOLOGY_REGISTRY.vehicle_traffic_fines;
    return { ...item, theme: themeName, word_count: item.direct_answer_text.split(/\s+/).length };
  }
  if (text.includes('bienso') || text.includes('sangten') || text.includes('truocba')) {
    const item = DOMAIN_ONTOLOGY_REGISTRY.vehicle_registration_plate;
    return { ...item, theme: themeName, word_count: item.direct_answer_text.split(/\s+/).length };
  }
  if (text.includes('gara') || text.includes('suaxe') || text.includes('baoduong') || text.includes('giaxang') || text.includes('giadau') || text.includes('tramsac') || text.includes('vetc') || text.includes('epass')) {
    const item = DOMAIN_ONTOLOGY_REGISTRY.vehicle_registration_plate;
    return {
      ...item,
      schema_type: 'AutomotiveBusiness',
      schema_category: 'https://schema.org/AutomotiveBusiness',
      theme: themeName,
      direct_answer_text: `${themeName} là tiện ích vận hành phương tiện giao thông trên Kênh Web MoMo, hỗ trợ tra cứu giá dịch vụ, mạng lưới trạm thu phí không dừng và garage cứu hộ đạt chuẩn kỹ thuật, giúp người điều khiển phương tiện an tâm di chuyển trên mọi cung đường.`,
      word_count: 46,
    };
  }
  if (text.includes('phim') || text.includes('cinema') || text.includes('lichchieu') || text.includes('vechieu') || text.includes('rap')) {
    const item = DOMAIN_ONTOLOGY_REGISTRY.cinema_movie;
    return { ...item, theme: themeName, word_count: item.direct_answer_text.split(/\s+/).length };
  }
  if (text.includes('vemaybay') || text.includes('vetau') || text.includes('vexe') || text.includes('dulich') || text.includes('resort') || text.includes('tour')) {
    const item = DOMAIN_ONTOLOGY_REGISTRY.ota_travel_transit;
    return { ...item, theme: themeName, word_count: item.direct_answer_text.split(/\s+/).length };
  }
  if (text.includes('data4g') || text.includes('naptiendienthoai') || text.includes('sim') || text.includes('esim')) {
    const item = DOMAIN_ONTOLOGY_REGISTRY.telco_data_sim;
    return { ...item, theme: themeName, word_count: item.direct_answer_text.split(/\s+/).length };
  }
  if (text.includes('benhvien') || text.includes('kham') || text.includes('calo') || text.includes('bmi')) {
    const item = DOMAIN_ONTOLOGY_REGISTRY.hospital_health;
    return { ...item, theme: themeName, word_count: item.direct_answer_text.split(/\s+/).length };
  }
  if (text.includes('daihoc') || text.includes('caodang') || text.includes('diemchuan') || text.includes('hocphi') || text.includes('sinhvien') || text.includes('tuyensinh')) {
    const item = DOMAIN_ONTOLOGY_REGISTRY.student_education;
    return { ...item, theme: themeName, word_count: item.direct_answer_text.split(/\s+/).length };
  }
  if (text.includes('xoso') || text.includes('vietlott') || text.includes('veso')) {
    const item = DOMAIN_ONTOLOGY_REGISTRY.lottery_vietlott;
    return { ...item, theme: themeName, word_count: item.direct_answer_text.split(/\s+/).length };
  }

  // 2. Hệ thống Dynamic Fallback thông minh theo Sector
  const cleanHub = sector ? `${sector.charAt(0).toUpperCase() + sector.slice(1)} Hub` : 'Web Platform';
  const sec = (sector || '').toLowerCase();

  let schemaType = 'Article';
  let schemaCat = 'https://schema.org/Article';
  let pExpertise = {
    title: `Quy chuẩn chuyên môn & Cơ sở pháp lý của ${themeName}`,
    summary: 'Làm rõ các văn bản quy phạm pháp luật và tiêu chuẩn thẩm định nghiệp vụ.',
    detail: `Nội dung làm rõ các điều kiện pháp lý, quyền lợi và nghĩa vụ thực tế của người dùng khi sử dụng ${themeName} theo quy định pháp luật hiện hành.`,
    actionable_angle: 'Bảng điều kiện và tiêu chí thẩm định chuyên sâu.',
  };
  let pTrust = {
    title: `Cơ chế xác thực & Bảo vệ quyền lợi người dùng trong ${themeName}`,
    summary: 'Minh bạch hạ tầng công nghệ bảo vệ quyền lợi và dữ liệu cá nhân của người dùng.',
    detail: `Hệ thống tích hợp mã hóa đầu cuối, chứng chỉ an toàn thông tin và quy trình xác thực chính chủ minh bạch khi thao tác ${themeName}.`,
    actionable_angle: 'Quy trình xác minh bảo mật đa tầng và chính sách bảo vệ dữ liệu.',
  };
  let pHighIntent = {
    title: `Phân tích biểu phí & Bảng đối chiếu so sánh giải pháp ${themeName}`,
    summary: 'Cung cấp số liệu định lượng chi tiết giúp người dùng ra quyết định tức thì.',
    detail: `Cung cấp bảng số liệu định lượng, chi phí phát sinh và mốc thời gian xử lý thực tế thay vì diễn giải lý thuyết chung chung.`,
    actionable_angle: 'Bảng đối chiếu thông số thực tế giữa các phương án trên thị trường.',
  };

  if (sec.includes('financial')) {
    schemaType = 'FinancialProduct';
    schemaCat = 'https://schema.org/FinancialProduct';
    pExpertise = {
      title: `Quy định cấp phép của Ngân hàng Nhà nước & Căn cứ pháp lý của ${themeName}`,
      summary: 'Quy chuẩn an toàn vốn và điều kiện cung ứng dịch vụ tài chính theo quy định của NHNN.',
      detail: `Dịch vụ được vận hành bởi các tổ chức tín dụng được cấp phép chính thức, tuân thủ các quy định về trần lãi suất, hạn mức và bảo mật giao dịch thanh toán.`,
      actionable_angle: 'Bảng điều kiện cấp phép và danh mục văn bản pháp luật điều chỉnh.',
    };
  } else if (sec.includes('vehicle')) {
    schemaType = 'GovernmentService';
    schemaCat = 'https://schema.org/GovernmentService';
    pExpertise = {
      title: `Quy chuẩn an toàn giao thông & Căn cứ kiểm định phương tiện của ${themeName}`,
      summary: 'Tuân thủ các quy định quản lý phương tiện của Bộ Giao thông Vận tải và Cục CSGT.',
      detail: `Hướng dẫn tra cứu và đối soát dữ liệu trực tiếp với cơ sở dữ liệu phương tiện quốc gia, đảm bảo chuẩn xác về mặt pháp lý đường bộ.`,
      actionable_angle: 'Mốc thời gian và danh mục kiểm tra an toàn kỹ thuật phương tiện.',
    };
  } else if (sec.includes('insurtech')) {
    schemaType = 'InsuranceProduct';
    schemaCat = 'https://schema.org/InsuranceProduct';
    pExpertise = {
      title: `Quy định của Bộ Tài chính & Phạm vi bảo hiểm hợp pháp của ${themeName}`,
      summary: 'Làm rõ các điều khoản loại trừ bảo hiểm và hạn mức trách nhiệm bồi thường tối đa.',
      detail: `Quy định rõ ràng về quyền lợi được chi trả, hồ sơ yêu cầu bồi thường và thời hạn giải quyết quyền lợi theo Luật Kinh doanh Bảo hiểm.`,
      actionable_angle: 'Bảng đối chiếu quyền lợi bảo hiểm và danh mục các điểm loại trừ bồi thường.',
    };
  }

  const defaultAnswer = `${themeName} là giải pháp số hóa chuyên sâu thuộc lĩnh vực ${cleanHub} trên Kênh Web MoMo, hỗ trợ người dùng tra cứu thông tin chính xác, cập nhật dữ liệu thời gian thực và thực hiện giao dịch an toàn với sự liên kết của các đối tác đầu ngành được cấp phép.`;

  return {
    hub: cleanHub,
    theme: themeName,
    schema_type: schemaType,
    schema_category: schemaCat,
    mandatory_fields: [
      { field: 'name', desc: `Tên chính xác của tiện ích ${themeName}.` },
      { field: 'description', desc: 'Tóm tắt bản chất giá trị cung cấp.' },
      { field: 'provider', desc: 'Đơn vị phát hành hoặc đối tác thẩm quyền cung ứng dịch vụ.' },
      { field: 'areaServed', desc: 'Khu vực áp dụng (Mặc định: Toàn quốc / VN).' },
    ],
    direct_answer_text: defaultAnswer,
    word_count: defaultAnswer.split(/\s+/).length,
    sample_jsonld: {
      '@context': 'https://schema.org',
      '@type': schemaType,
      name: `${themeName} - MoMo Web Platform`,
      description: defaultAnswer,
      provider: { '@type': 'Organization', name: 'MoMo Web Platform', url: 'https://www.momo.vn' },
      areaServed: 'VN',
    },
    pillars: {
      expertise: pExpertise,
      trust: pTrust,
      high_intent: pHighIntent,
    },
    cta_text: `Trải Nghiệm Tiện Ích ${themeName} Trên MoMo`,
    deeplink: `momo://app-action?service=${themeId}`,
    umami_event: `web_${themeId.replace(/-/g, '_')}_btn_click`,
  };
}
'''

def main():
    target = "/Users/hienhv/HienHv/Klaus/Web-Idea/react-web-momo/lib/content-plan/geo-entity-registry.ts"
    with open(target, "w", encoding="utf-8") as f:
        f.write(CONTENT.strip() + "\n")
    print(f"Successfully written {len(CONTENT)} bytes to {target}")

if __name__ == "__main__":
    main()
