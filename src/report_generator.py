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
