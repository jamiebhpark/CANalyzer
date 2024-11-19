import os
import sys
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from src.generate_report import generate_report


def generate_pdf_report(analysis_results, file_name="report.pdf"):
    """
    분석 결과를 PDF 파일로 저장.
    :param analysis_results: 분석 결과 (딕셔너리 형태)
    :param file_name: 저장할 파일 이름
    """
    try:
        c = canvas.Canvas(file_name, pagesize=letter)
        c.setFont("Helvetica", 12)
        c.drawString(100, 750, "CAN Analysis Report")
        c.drawString(100, 740, "=" * 30)

        y_position = 720
        for key, value in analysis_results.items():
            c.drawString(100, y_position, f"{key}: {value}")
            y_position -= 20

        c.save()
        print(f"PDF report saved as {file_name}")
    except Exception as e:
        print(f"Failed to save PDF report: {e}")


def generate_html_report(analysis_results, file_name="report.html"):
    """
    분석 결과를 HTML 파일로 저장.
    :param analysis_results: 분석 결과 (딕셔너리 형태)
    :param file_name: 저장할 파일 이름
    """
    try:
        with open(file_name, "w", encoding="utf-8") as file:
            file.write("<html><head><title>CAN Analysis Report</title></head><body>")
            file.write("<h1>CAN Analysis Report</h1>")
            file.write("<table border='1' style='border-collapse: collapse;'>")
            file.write("<tr><th>Metric</th><th>Value</th></tr>")
            for key, value in analysis_results.items():
                file.write(f"<tr><td>{key}</td><td>{value}</td></tr>")
            file.write("</table>")
            file.write("</body></html>")
        print(f"HTML report saved as {file_name}")
    except Exception as e:
        print(f"Failed to save HTML report: {e}")


if __name__ == "__main__":
    # 테스트 데이터
    sample_results = {
        "Total Messages": 100,
        "Unique CAN IDs": 5,
        "Average DLC": 7.2
    }
    # 텍스트 보고서 생성
    generate_report(sample_results)

    # PDF 보고서 생성
    generate_pdf_report(sample_results)

    # HTML 보고서 생성 테스트
    generate_html_report(sample_results, file_name="CAN_analysis_report.html")