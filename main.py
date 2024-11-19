from src.can_parser import parse_can_log
from src.data_analysis import calculate_message_frequency, calculate_statistics, filter_by_time_range
from src.data_visualization import plot_message_frequency, plot_time_series
from src.report_generator import generate_pdf_report


def main():
    # 1. CAN 로그 데이터 읽기
    file_path = "data/sample_can_log.csv"
    data = parse_can_log(file_path)
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

    # 4. 데이터 시각화
    plot_message_frequency(freq_data)

    # 5. PDF 보고서 생성
    generate_pdf_report(stats, file_name="CAN_analysis_report.pdf")

    # 시간 기반 데이터 필터링
    start_time, end_time = 0.001, 0.003
    filtered_data = filter_by_time_range(data, start_time, end_time)
    print(f"Filtered Data from {start_time} to {end_time}:")
    print(filtered_data)

    # 시간 기반 시각화
    plot_time_series(filtered_data)


if __name__ == "__main__":
    main()
