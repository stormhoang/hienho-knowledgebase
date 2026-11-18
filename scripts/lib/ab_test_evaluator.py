#!/usr/bin/env python3
"""
A/B TESTING & STATISTICAL SIGNIFICANCE CALCULATOR
Công cụ đánh giá độ tin cậy thống kê cho các thử nghiệm tối ưu CTR (Snippet) và CVR (OneLink W2A).

Tính năng:
1. Two-proportion Z-Test tính toán P-value và 95% Confidence Interval (Zero dependency, dùng math.erf).
2. Tính toán quy mô mẫu tối thiểu cần thiết (Minimum Sample Size Calculator - MDE).
3. Đưa ra khuyến nghị quyết định chuẩn Product Lead: Áp dụng Variant B, Giữ nguyên Variant A, hay Cần chạy thêm ngày.
"""

import sys
import math
import argparse
from tabulate import tabulate


def format_table(headers, rows):
    return tabulate(rows, headers=headers, tablefmt="github")


def normal_cdf(z: float) -> float:
    """Hàm phân phối tích lũy chuẩn tắc (Standard Normal CDF)."""
    return 0.5 * (1.0 + math.erf(z / math.sqrt(2.0)))


def evaluate_ab_test(name: str, metric_type: str, n_a: int, x_a: int, n_b: int, x_b: int, conf_level: float = 0.95):
    """
    n_a, n_b: Số lượng quan sát (Impressions hoặc Sessions)
    x_a, x_b: Số lượng thành công (Clicks hoặc OneLink Conversions)
    """
    if n_a <= 0 or n_b <= 0:
        return {"error": "Cỡ mẫu n_a và n_b phải lớn hơn 0."}

    p_a = x_a / n_a
    p_b = x_b / n_b

    # Pooled probability
    p_pool = (x_a + x_b) / (n_a + n_b)
    
    # Standard Error under Null Hypothesis
    if p_pool == 0 or p_pool == 1:
        return {"error": "Tỷ lệ chuyển đổi bằng 0 hoặc 100%, không đủ biến thiên để kiểm định."}

    se = math.sqrt(p_pool * (1.0 - p_pool) * (1.0 / n_a + 1.0 / n_b))
    if se == 0:
        return {"error": "Sai số chuẩn bằng 0."}

    z_score = (p_b - p_a) / se
    p_value = 2.0 * (1.0 - normal_cdf(abs(z_score)))

    # Relative Lift
    if p_a > 0:
        relative_lift = ((p_b - p_a) / p_a) * 100.0
    else:
        relative_lift = 0.0

    # 95% Confidence Interval for difference
    se_diff = math.sqrt((p_a * (1.0 - p_a) / n_a) + (p_b * (1.0 - p_b) / n_b))
    z_critical = 1.96  # for 95% CI
    ci_lower = ((p_b - p_a) - z_critical * se_diff) * 100.0
    ci_upper = ((p_b - p_a) + z_critical * se_diff) * 100.0

    # Decision Recommendation
    is_significant = p_value < (1.0 - conf_level)
    if is_significant:
        if relative_lift > 0:
            verdict = "CHIẾN THẮNG (WINNER): Áp dụng Variant B cho 100% người dùng ngay."
            status = "SIGNIFICANT_POSITIVE"
        else:
            verdict = "THẤT BẠI (LOSER): Variant B giảm hiệu suất. Giữ nguyên Variant A."
            status = "SIGNIFICANT_NEGATIVE"
    else:
        if n_a < 1000 or n_b < 1000:
            verdict = "CHƯA ĐỦ MẪU: Cần tiếp tục chạy thử nghiệm để tích lũy thêm dữ liệu."
            status = "UNDERPOWERED"
        else:
            verdict = "KHÔNG CÓ KHÁC BIỆT CÓ Ý NGHĨA THỐNG KÊ: Không có bằng chứng Variant B tốt hơn Variant A."
            status = "INCONCLUSIVE"

    return {
        "name": name,
        "metric_type": metric_type,
        "n_a": n_a,
        "x_a": x_a,
        "p_a": p_a * 100.0,
        "n_b": n_b,
        "x_b": x_b,
        "p_b": p_b * 100.0,
        "relative_lift": relative_lift,
        "z_score": z_score,
        "p_value": p_value,
        "ci_lower": ci_lower,
        "ci_upper": ci_upper,
        "verdict": verdict,
        "status": status
    }


def calculate_min_sample_size(baseline_rate: float, min_detectable_effect: float = 0.10, alpha: float = 0.05, power: float = 0.80) -> int:
    """
    Tính số lượng quan sát tối thiểu cần cho mỗi nhóm (Per Variant).
    baseline_rate: Tỷ lệ gốc (ví dụ: 0.03 cho 3% CVR)
    min_detectable_effect: Mức tăng tối thiểu muốn phát hiện (ví dụ: 0.10 cho 10% lift)
    """
    p = baseline_rate
    delta = p * min_detectable_effect
    z_alpha = 1.96  # alpha = 0.05 (two-tailed)
    z_beta = 0.84   # power = 0.80

    numerator = 2.0 * ((z_alpha + z_beta) ** 2) * p * (1.0 - p)
    denominator = delta ** 2
    if denominator == 0:
        return 0
    return int(math.ceil(numerator / denominator))


def print_ab_report(res):
    if "error" in res:
        print(f"[ERROR] {res['error']}")
        return

    print("=" * 80)
    print(f"KẾT QUẢ PHÂN TÍCH THỬ NGHIỆM A/B: {res['name'].upper()}")
    print("=" * 80)

    metric_unit = "CTR" if res["metric_type"].upper() == "CTR" else "W2A CVR"
    sample_unit = "Impressions" if res["metric_type"].upper() == "CTR" else "Sessions"
    success_unit = "Clicks" if res["metric_type"].upper() == "CTR" else "OneLink Clicks"

    data_table = [
        ["Phiên bản Kiểm thử", f"Mẫu ({sample_unit})", f"Chuyển đổi ({success_unit})", f"Tỷ lệ {metric_unit}"],
        ["Variant A (Control - Bản gốc)", f"{res['n_a']:,}", f"{res['x_a']:,}", f"{res['p_a']:.2f}%"],
        ["Variant B (Challenger - Thử nghiệm)", f"{res['n_b']:,}", f"{res['x_b']:,}", f"{res['p_b']:.2f}%"],
    ]
    print(format_table(data_table[0], data_table[1:]))

    print("\nChỉ số Thống kê Chuyên sâu:")
    stats_table = [
        ["Độ lệch tương đối (Relative Lift)", f"{res['relative_lift']:+.2f}%"],
        ["Khoảng tin cậy 95% (95% CI)", f"[{res['ci_lower']:+.2f}%, {res['ci_upper']:+.2f}%]"],
        ["Z-Score", f"{res['z_score']:.4f}"],
        ["P-Value", f"{res['p_value']:.4f} ({'P < 0.05' if res['p_value'] < 0.05 else 'P >= 0.05'})"],
        ["Kết luận Thực thi", res["verdict"]]
    ]
    print(format_table(["Chỉ số Kiểm định", "Giá trị tính toán"], stats_table))
    print("=" * 80)


def main():
    parser = argparse.ArgumentParser(description="A/B Testing Statistical Significance Calculator")
    parser.add_argument("--name", type=str, default="Thử nghiệm tối ưu", help="Tên bài kiểm thử")
    parser.add_argument("--type", type=str, choices=["ctr", "cvr"], default="ctr", help="Loại chỉ số đo lường (ctr hoặc cvr)")
    parser.add_argument("--na", type=int, default=50000, help="Cỡ mẫu Variant A (Impressions hoặc Sessions)")
    parser.add_argument("--xa", type=int, default=500, help="Số chuyển đổi Variant A (Clicks hoặc OneLink)")
    parser.add_argument("--nb", type=int, default=50000, help="Cỡ mẫu Variant B")
    parser.add_argument("--xb", type=int, default=650, help="Số chuyển đổi Variant B")
    parser.add_argument("--mde-calc", action="store_true", help="Chạy tính toán cỡ mẫu cần thiết")
    parser.add_argument("--baseline", type=float, default=0.02, help="Tỷ lệ cơ sở (ví dụ: 0.02 cho 2%% CVR)")
    parser.add_argument("--mde", type=float, default=0.15, help="Mức tăng tối thiểu muốn đo lường (ví dụ: 0.15 cho 15%% lift)")
    args = parser.parse_args()

    if args.mde_calc:
        n_needed = calculate_min_sample_size(args.baseline, args.mde)
        print("=" * 75)
        print("TÍNH TOÁN CỠ MẪU TỐI THIỂU CẦN THIẾT (SAMPLE SIZE CALCULATOR)")
        print("=" * 75)
        mde_table = [
            ["Tỷ lệ cơ sở ban đầu (Baseline)", f"{args.baseline * 100:.2f}%"],
            ["Mức nâng kỳ vọng tối thiểu (MDE)", f"{args.mde * 100:.1f}% lift"],
            ["Độ tin cậy (Confidence Level)", "95% (Alpha = 0.05)"],
            ["Lực thống kê (Statistical Power)", "80% (Beta = 0.20)"],
            ["Số lượng mẫu cần thiết mỗi Variant", f"{n_needed:,} lượt (Impressions/Sessions)"],
            ["Tổng số mẫu cả 2 nhóm (A + B)", f"{n_needed * 2:,} lượt"],
        ]
        print(format_table(["Tham số", "Giá trị tính toán"], mde_table))
        print("=" * 75)
    else:
        res = evaluate_ab_test(args.name, args.type, args.na, args.xa, args.nb, args.xb)
        print_ab_report(res)


if __name__ == "__main__":
    main()
