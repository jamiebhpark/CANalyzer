import argparse
from src.anomaly_detection import detect_anomalies
from src.can_parser import parse_can_log
from src.data_analysis import (
    calculate_message_frequency,
    calculate_statistics,
    filter_by_time_range,
    evaluate_data_quality,
    calculate_time_interval_statistics,
    generate_diagnostics  # 진단 함수 추가
)
from src.data_visualization import (
    plot_message_frequency,
    plot_time_series,
    plot_anomalies,
    save_plot_message_frequency,
    save_plot_anomalies,
    plot_time_intervals
)
from src.report_generator import generate_html_report, generate_pdf_report


def main():
    # 명령줄 인자 설정
    parser = argparse.ArgumentParser(description="CANalyzer: Analyze CAN logs.")
    parser.add_argument("--file", help="Path to the CAN log file", required=True)
    parser.add_argument("--start-time", type=float, help="Start time for filtering", default=0.0)
    parser.add_argument("--end-time", type=float, help="End time for filtering", default=float("inf"))
    parser.add_argument("--report-type", choices=["pdf", "html"], help="Report type to generate", default="pdf")
    parser.add_argument("--anomaly-detection", action="store_true", help="Enable anomaly detection")

    args = parser.parse_args()

    # 1. CAN 로그 데이터 읽기
    data = parse_can_log(args.file)
    if data is None:
        print("Failed to load CAN log data.")
        return

    # 2. 데이터 분석
    stats = calculate_statistics(data)
    freq_data = calculate_message_frequency(data)

    # 3. 데이터 품질 평가
    evaluation_report = evaluate_data_quality(data)
    print("Data Quality Evaluation:")
    print(evaluation_report)

    # 4. 시간 간격 통계 계산
    time_interval_stats = calculate_time_interval_statistics(data)
    print("Time Interval Statistics:")
    for key, value in time_interval_stats.items():
        print(f"{key}: {value:.6f} seconds")

    # 5. 진단 결과 생성
    diagnostics = generate_diagnostics(data)
    print("Diagnostics Summary:")
    for diagnostic in diagnostics:
        print(f"- {diagnostic}")

    # 6. 데이터 시각화 (전체 데이터 기준)
    plot_message_frequency(freq_data)

    # 7. 시간 기반 데이터 필터링
    filtered_data = filter_by_time_range(data, args.start_time, args.end_time)
    print(f"Filtered Data from {args.start_time} to {args.end_time}:")
    print(filtered_data)

    # 8. 시간 기반 시각화
    plot_time_series(filtered_data, file_name="message_frequency_over_time.png")

    # 9. 시간 간격 시각화 저장
    plot_time_intervals(data, file_name="time_interval_plot.png")

    # 10. 이상 탐지 실행
    detected_data = detect_anomalies(data)
    print("Anomalies Detected:")
    print(detected_data[detected_data["Anomaly"] == -1])  # 이상치 출력

    # 11. 이상 탐지 결과 시각화
    plot_anomalies(detected_data)

    # 12. 그래프 저장
    save_plot_message_frequency(freq_data, file_name="frequency_plot.png")
    save_plot_anomalies(detected_data, file_name="anomalies_plot.png")

    # 13. 보고서 생성
    if args.report_type == "pdf":
        # PDF 생성
        generate_pdf_report(
            analysis_results=stats,
            graph_files=[
                "frequency_plot.png",
                "anomalies_plot.png",
                "message_frequency_over_time.png",
                "time_interval_plot.png"
            ],
            anomalies=detected_data[detected_data["Anomaly"] == -1],
            evaluation_report=evaluation_report,
            time_interval_stats=time_interval_stats,
            diagnostics=diagnostics,  # 진단 결과 추가
            file_name="CAN_analysis_report.pdf",
            report_type="with_graphs"
        )
        print(f"Report generated as PDF: CAN_analysis_report.pdf")
    elif args.report_type == "html":
        # HTML 생성
        generate_html_report(
            analysis_results=stats,
            graph_files=[
                "frequency_plot.png",
                "anomalies_plot.png",
                "message_frequency_over_time.png",
                "time_interval_plot.png"
            ],
            evaluation_report=evaluation_report,
            time_interval_stats=time_interval_stats,
            anomalies=detected_data[detected_data["Anomaly"] == -1],
            diagnostics=diagnostics,  # 진단 결과 추가
            file_name="CAN_analysis_report.html"
        )
        print(f"Report generated as HTML: CAN_analysis_report.html")


if __name__ == "__main__":
    main()
