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


def plot_time_series(df, file_name=None):
    """
    시간 범위에 따른 메시지 빈도 시각화 및 파일 저장.
    :param df: 데이터프레임
    :param file_name: 그래프를 저장할 파일 이름 (옵션)
    """
    # 타임 스탬프를 소수점 2자리로 그룹화
    df["Time Bin"] = df["Timestamp"].round(2)
    time_series = df["Time Bin"].value_counts().sort_index()

    # 그래프 그리기
    plt.figure(figsize=(10, 6))
    time_series.plot(kind="line", marker="o")
    plt.title("Message Frequency Over Time")
    plt.xlabel("Timestamp (seconds)")
    plt.ylabel("Frequency")
    plt.grid(True)
    plt.tight_layout()

    # 그래프 저장
    if file_name:
        plt.savefig(file_name)
        print(f"Time series plot saved as {file_name}")

    # 그래프 표시
    plt.show()
    plt.close()


def plot_anomalies(df):
    """
    이상 탐지 결과를 시각화합니다.
    :param df: 데이터프레임 (Anomaly 컬럼 포함)
    """
    normal_data = df[df["Anomaly"] == 1]
    anomalies = df[df["Anomaly"] == -1]

    plt.scatter(normal_data["Timestamp"], normal_data["DLC"], label="Normal", alpha=0.7)
    plt.scatter(anomalies["Timestamp"], anomalies["DLC"], label="Anomaly", color="red", alpha=0.7)
    plt.title("Anomaly Detection Results")
    plt.xlabel("Timestamp")
    plt.ylabel("DLC")
    plt.legend()
    plt.show()


def save_plot_message_frequency(freq_data, file_name="frequency_plot.png"):
    """
    메시지 빈도 그래프를 파일로 저장.
    :param freq_data: 메시지 빈도 데이터
    :param file_name: 저장할 파일 이름
    """
    freq_data.plot(kind="bar")
    plt.title("Message Frequency by CAN ID")
    plt.xlabel("CAN ID")
    plt.ylabel("Frequency")
    plt.tight_layout()
    plt.savefig(file_name)
    plt.close()
    print(f"Frequency plot saved as {file_name}")


def save_plot_anomalies(df, file_name="anomalies_plot.png"):
    """
    이상 탐지 결과를 그래프로 저장.
    :param df: 데이터프레임 (Anomaly 컬럼 포함)
    :param file_name: 저장할 파일 이름
    """
    normal_data = df[df["Anomaly"] == 1]
    anomalies = df[df["Anomaly"] == -1]

    plt.scatter(normal_data["Timestamp"], normal_data["DLC"], label="Normal", alpha=0.7)
    plt.scatter(anomalies["Timestamp"], anomalies["DLC"], label="Anomaly", color="red", alpha=0.7)
    plt.title("Anomaly Detection Results")
    plt.xlabel("Timestamp")
    plt.ylabel("DLC")
    plt.legend()
    plt.tight_layout()
    plt.savefig(file_name)
    plt.close()
    print(f"Anomalies plot saved as {file_name}")


def plot_time_intervals(data, file_name=None):
    """
    메시지 간 시간 간격 분석 및 시각화.
    :param data: CAN 로그 데이터프레임
    :param file_name: 저장할 파일 이름 (옵션)
    """
    intervals = data["Timestamp"].diff().dropna()
    plt.figure(figsize=(10, 6))
    plt.hist(intervals, bins=50, alpha=0.7, color='blue')
    plt.title("Message Time Intervals")
    plt.xlabel("Time Interval (seconds)")
    plt.ylabel("Frequency")
    plt.grid(True)
    plt.tight_layout()

    if file_name:
        plt.savefig(file_name)
        print(f"Time interval plot saved as {file_name}")
    plt.show()
    plt.close()


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
