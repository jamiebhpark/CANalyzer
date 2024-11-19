import pandas as pd


def parse_can_log(file_path):
    """
    CAN 로그 데이터를 읽어서 DataFrame으로 반환.
    파일 경로를 입력으로 받아 CSV 데이터를 읽고 컬럼을 정리함.
    """
    try:
        # CSV 파일 읽기
        df = pd.read_csv(file_path)
        # 컬럼 이름 설정
        df.columns = ["Timestamp", "CAN_ID", "DLC", "Data"]
        return df
    except Exception as e:
        print(f"파일 읽기 실패: {e}")
        return None


# 테스트 실행
if __name__ == "__main__":
    file_path = "data/sample_can_log.csv"
    data = parse_can_log(file_path)
    if data is not None:
        print(data.head())
