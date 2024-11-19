import argparse
from src.can_parser import parse_can_log
from src.data_analysis import calculate_message_frequency, calculate_statistics, filter_by_time_range
from src.data_visualization import plot_message_frequency, plot_time_series, plot_anomalies
from src.report_generator import generate_pdf_report, generate_report, generate_html_report
from src.anomaly_detection import detect_anomalies


def main():
    # 명령줄 인자 설정
    parser = argparse.ArgumentParser(description="CANalyzer: Analyze CAN logs.")
    parser.add_argument("--file", help="Path to the CAN log file", required=True)
    parser.add_argument("--start-time", type=float, help="Start time for filtering", default=0.0)
    parser.add_argument("--end-time", type=float, help="End time for filtering", default=float("inf"))
    parser.add_argument("--report-type", choices=["pdf", "txt", "html"], help="Report type to generate", default="pdf")
    args = parser.parse_args()

    # 1. CAN 로그 데이터 읽기
    data = parse_can_log(args.file)
    if data is None:
        print("Failed to load CAN log data.")
        return

    # 2. 데이터 분석
    stats = calculate_statistics(data)
    freq_data = calculate_message_frequency(data)

    # 3. 분석 결과 출력
    print("Analysis Results:")
    for key, value in stats.items():
        print(f"{key}: {value}")

    # 4. 데이터 시각화 (전체 데이터 기준)
    plot_message_frequency(freq_data)

    # 5. 시간 기반 데이터 필터링
    filtered_data = filter_by_time_range(data, args.start_time, args.end_time)
    print(f"Filtered Data from {args.start_time} to {args.end_time}:")
    print(filtered_data)

    # 6. 시간 기반 시각화
    plot_time_series(filtered_data)

    # 7. 보고서 생성
    if args.report_type == "pdf":
        generate_pdf_report(stats, file_name="CAN_analysis_report.pdf")
    elif args.report_type == "txt":
        generate_report(stats, file_name="CAN_analysis_report.txt")
    elif args.report_type == "html":
        generate_html_report(stats, file_name="CAN_analysis_report.html")
    print(f"Report generated as {args.report_type.upper()}")

    # 8. 이상 탐지 실행
    detected_data = detect_anomalies(data)
    print("Anomalies Detected:")
    print(detected_data[detected_data["Anomaly"] == -1])  # 이상치 출력

    # 9. 이상 탐지 결과 시각화
    plot_anomalies(detected_data)


if __name__ == "__main__":
    main()
