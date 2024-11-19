import os
import sys

# 현재 파일의 상위 디렉토리를 sys.path에 추가
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from sklearn.ensemble import IsolationForest


def detect_anomalies(df, contamination=0.05):
    """
    Isolation Forest를 사용해 이상치를 탐지합니다.
    :param df: 데이터프레임 (CAN 로그 데이터)
    :param contamination: 이상치 비율 (0.05는 5%)
    :return: 이상치가 추가된 데이터프레임
    """
    # CAN 데이터에서 분석에 사용할 특징 선택
    features = df[["Timestamp", "DLC"]]  # 예: Timestamp와 DLC를 사용
    model = IsolationForest(contamination=contamination, random_state=42)
    df["Anomaly"] = model.fit_predict(features)

    # Anomaly 값이 -1인 경우 이상치
    return df


if __name__ == "__main__":
    from src.can_parser import parse_can_log

    # 샘플 데이터 로드
    file_path = "data/sample_can_log.csv"
    data = parse_can_log(file_path)

    # 이상치 탐지 실행
    detected_data = detect_anomalies(data)
    print("Anomaly Detection Results:")
    print(detected_data[detected_data["Anomaly"] == -1])  # 이상치만 출력
