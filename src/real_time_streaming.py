import sys
import os
import csv
import time
import pandas as pd  # pandas 추가


# Add the parent directory to sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from src.anomaly_detection import detect_anomalies
from src.can_parser import parse_can_log


def simulate_streaming(file_path, interval=1.0):
    """
    Simulates streaming by reading a CSV file line by line.
    :param file_path: Path to the CAN log file.
    :param interval: Time interval between each data row in seconds.
    """
    try:
        with open(file_path, "r") as file:
            reader = csv.DictReader(file)

            print("[INFO] Starting real-time CAN data stream simulation...")
            print("-" * 50)

            for row in reader:
                print(f"[INFO] New Data: {row}")

                # Process data for anomaly detection
                data_row = {
                    "Timestamp": float(row["Timestamp"]),
                    "CAN_ID": row["CAN_ID"],
                    "DLC": int(row["DLC"]),
                    "Data": row["Data"]
                }

                # Convert the single row to a DataFrame
                df_row = pd.DataFrame([data_row])

                try:
                    # Anomaly detection
                    detected_data = detect_anomalies(df_row)
                    print(f"[DEBUG] Detected anomalies: {detected_data}")  # 디버깅 추가
                    anomaly_flag = detected_data.iloc[0]["Anomaly"]  # 첫 번째 행의 Anomaly 값 확인

                    if anomaly_flag == -1:
                        print(
                            f"[WARNING] Anomaly detected at Timestamp {data_row['Timestamp']}: CAN ID {data_row['CAN_ID']}"
                        )
                except Exception as e:
                    print(f"[ERROR] Anomaly detection failed: {e}")

                # Wait for the next interval
                time.sleep(interval)

    except FileNotFoundError:
        print(f"[ERROR] File not found: {file_path}")
    except Exception as e:
        print(f"[ERROR] An error occurred: {e}")


if __name__ == "__main__":
    # Path to the CAN log file
    file_path = os.path.join(os.path.dirname(__file__), "../data/sample_can_log.csv")

    # Simulate streaming with a 1-second interval
    simulate_streaming(file_path, interval=1.0)
