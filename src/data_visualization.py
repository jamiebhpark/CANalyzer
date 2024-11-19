import os
import sys

import matplotlib.pyplot as plt

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))


def plot_message_frequency(freq_data):
    """
    CAN 메시지 빈도를 막대 그래프로 시각화.
    """
    freq_data.plot(kind="bar")
    plt.title("Message Frequency by CAN ID")
    plt.xlabel("CAN ID")
    plt.ylabel("Frequency")
    plt.show()


def plot_time_series(df):
    """
    시간 범위에 따른 메시지 빈도 시각화.
    :param df: 데이터프레임
    """
    # 타임 스탬프를 소수점 2자리로 그룹화
    df["Time Bin"] = df["Timestamp"].round(2)
    time_series = df["Time Bin"].value_counts().sort_index()

    # 그래프 그리기
    time_series.plot(kind="line", marker="o")
    plt.title("Message Frequency Over Time")
    plt.xlabel("Timestamp (seconds)")
    plt.ylabel("Frequency")
    plt.grid(True)
    plt.show()


# 테스트 실행
if __name__ == "__main__":
    from src.data_analysis import calculate_message_frequency
    from src.can_parser import parse_can_log

    # 샘플 데이터 읽기
    file_path = "data/sample_can_log.csv"
    data = parse_can_log(file_path)

    # 빈도 계산 및 시각화
    freq_data = calculate_message_frequency(data)
    plot_message_frequency(freq_data)

    from src.can_parser import parse_can_log

    # 데이터 로드
    data = parse_can_log("data/sample_can_log.csv")

    # 시간 기반 시각화
    plot_time_series(data)
