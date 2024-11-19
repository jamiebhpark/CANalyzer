import pandas as pd


def create_sample_data():
    # 샘플 데이터 정의
    sample_data = [
        {"Timestamp": 0.001, "CAN_ID": "0x123", "DLC": 8, "Data": "01 02 03 04 05 06 07 08"},
        {"Timestamp": 0.002, "CAN_ID": "0x124", "DLC": 4, "Data": "11 22 33 44"},
        {"Timestamp": 0.003, "CAN_ID": "0x123", "DLC": 8, "Data": "FF EE DD CC BB AA 99 88"},
    ]

    # DataFrame으로 변환
    df = pd.DataFrame(sample_data)

    # CSV 파일로 저장
    df.to_csv("data/sample_can_log.csv", index=False)
    print("샘플 데이터가 'data/sample_can_log.csv'에 저장되었습니다.")


# 실행
if __name__ == "__main__":
    create_sample_data()
