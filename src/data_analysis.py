import os
import sys

# 현재 파일의 상위 디렉토리를 경로에 추가
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from src.can_parser import parse_can_log  # 이제 경로 문제가 해결됨


def filter_by_can_id(df, can_id):
    """
    특정 CAN ID에 해당하는 데이터를 필터링.
    """
    return df[df["CAN_ID"] == can_id]


def calculate_message_frequency(df):
    """
    CAN 메시지 빈도를 계산하여 반환.
    """
    return df["CAN_ID"].value_counts()


def calculate_statistics(df):
    """
    주요 통계를 계산하여 반환.
    """
    statistics = {
        "Total Messages": len(df),
        "Unique CAN IDs": df["CAN_ID"].nunique(),
        "Average DLC": df["DLC"].mean(),
    }
    return statistics


def filter_by_time_range(df, start_time, end_time):
    """
    특정 시간 범위 내의 데이터를 필터링.
    :param df: 데이터프레임
    :param start_time: 시작 시간 (초)
    :param end_time: 종료 시간 (초)
    :return: 필터링된 데이터프레임
    """
    return df[(df["Timestamp"] >= start_time) & (df["Timestamp"] <= end_time)]


def evaluate_data_quality(data):
    """
    CAN 데이터의 품질 평가.
    :param data: CAN 로그 데이터프레임
    :return: 품질 평가 결과 문자열
    """
    try:
        # 평가 기준
        total_messages = len(data)
        unique_ids = len(data["CAN_ID"].unique())
        short_intervals = data["Timestamp"].diff().dropna().lt(0.01).sum()  # 0.01초 이하의 간격
        out_of_range_dlc = data["DLC"].gt(8).sum()  # DLC > 8

        # 결과 계산
        report = [f"Total Messages: {total_messages}", f"Unique CAN IDs: {unique_ids}",
                  f"Messages with short intervals (<0.01s): {short_intervals}",
                  f"Messages with out-of-range DLC (>8): {out_of_range_dlc}"]

        # 판단
        if short_intervals / total_messages > 0.1:
            report.append("Warning: High frequency of short intervals.")
        if out_of_range_dlc > 0:
            report.append("Warning: Out-of-range DLC values detected.")

        return "\n".join(report)

    except Exception as e:
        return f"Failed to evaluate data quality: {e}"


def calculate_time_interval_statistics(data):
    """
    메시지 간 시간 간격의 통계 계산.
    :param data: CAN 로그 데이터프레임
    :return: 시간 간격 통계 (딕셔너리)
    """
    intervals = data["Timestamp"].diff().dropna()
    stats = {
        "Min Interval": intervals.min(),
        "Max Interval": intervals.max(),
        "Mean Interval": intervals.mean(),
        "Std Interval": intervals.std()
    }
    return stats


def generate_diagnostics(data):
    """
    Generate diagnostic insights from CAN data.
    :param data: DataFrame of CAN log data.
    :return: Diagnostic results as a list of strings.
    """
    diagnostics = []

    # 1. 빈도 분석
    freq = data["CAN_ID"].value_counts()
    for can_id, count in freq.items():
        if count > 3:  # 임계값 설정
            diagnostics.append(f"CAN ID {can_id} appears {count} times, which is unusually high.")

    # 2. DLC 값 이상 탐지
    if (data["DLC"] < 2).any():
        diagnostics.append("Some DLC values are below 2, which might indicate data corruption.")

    # 3. 시간 간격 이상
    time_intervals = data["Timestamp"].diff().dropna()
    if time_intervals.max() > 0.2:  # 임계값 설정
        diagnostics.append("Large time gaps detected between messages, which could indicate a communication issue.")

    return diagnostics


# 테스트 실행
if __name__ == "__main__":
    import pandas as pd
    from src.can_parser import parse_can_log

    # 샘플 데이터 읽기
    file_path = "data/sample_can_log.csv"
    data = parse_can_log(file_path)

    # 특정 CAN ID 필터링
    filtered_data = filter_by_can_id(data, "0x123")
    print("Filtered Data for CAN ID 0x123:")
    print(filtered_data)

    # 메시지 빈도 계산
    message_frequency = calculate_message_frequency(data)
    print("Message Frequency:")
    print(message_frequency)

    # 주요 통계 계산
    stats = calculate_statistics(data)
    print("Statistics:")
    for key, value in stats.items():
        print(f"{key}: {value}")

    from src.can_parser import parse_can_log

    # 샘플 데이터 로드
    data = parse_can_log("data/sample_can_log.csv")

    # 특정 시간대 데이터 필터링
    filtered_data = filter_by_time_range(data, 0.001, 0.002)
    print("Filtered Data by Time Range (0.001 to 0.002):")
    print(filtered_data)
