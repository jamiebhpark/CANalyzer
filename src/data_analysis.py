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
