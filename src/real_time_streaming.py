import csv
import time
from src.anomaly_detection import detect_anomalies
from src.can_parser import parse_can_log


def simulate_streaming(file_path, interval=1.0):
    """
    Simulates streaming by reading a CSV file line by line.
    :param file_path: Path to the CAN log file.
    :param interval: Time interval between each data row in seconds.
    """
    try:
        # Open the CSV file
        with open(file_path, "r") as file:
            reader = csv.DictReader(file)

            print("[INFO] Starting real-time CAN data stream simulation...")
            print("-" * 50)

            # Simulate streaming
            for row in reader:
                print(f"[INFO] New Data: {row}")

                # Process data for anomaly detection
                data_row = {
                    "Timestamp": float(row["Timestamp"]),
                    "CAN_ID": row["CAN_ID"],
                    "DLC": int(row["DLC"]),
                    "Data": row["Data"]
                }
                anomaly_result = detect_anomalies([data_row])

                # Check if an anomaly is detected
                if anomaly_result[0]["Anomaly"] == -1:
                    print(
                        f"[WARNING] Anomaly detected at Timestamp {data_row['Timestamp']}: CAN ID {data_row['CAN_ID']}")

                # Wait for the next interval
                time.sleep(interval)

    except FileNotFoundError:
        print(f"[ERROR] File not found: {file_path}")
    except Exception as e:
        print(f"[ERROR] An error occurred: {e}")


if __name__ == "__main__":
    # Path to the CAN log file
    file_path = "data/sample_can_log.csv"

    # Simulate streaming with a 1-second interval
    simulate_streaming(file_path, interval=1.0)
