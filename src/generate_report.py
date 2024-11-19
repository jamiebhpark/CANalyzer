def generate_report(analysis_results, file_name="report.txt"):
    """
    분석 결과를 텍스트 파일로 저장.
    :param analysis_results: 분석 결과 (딕셔너리 형태)
    :param file_name: 저장할 파일 이름
    """
    try:
        # 올바른 경로로 파일 저장
        with open(f"data/{file_name}", "w", encoding="utf-8") as file:
            file.write("CAN Analysis Report\n")
            file.write("=" * 30 + "\n")
            for key, value in analysis_results.items():
                file.write(f"{key}: {value}\n")
        print(f"Text report saved as {file_name}")
    except Exception as e:
        print(f"Failed to save text report: {e}")
