import os
import sys
from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.pdfgen import canvas
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Image

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from src.generate_report import generate_report


def generate_pdf_report(analysis_results, graph_files=None, file_name="report.pdf"):
    """
    분석 결과와 그래프를 포함한 PDF 파일로 저장.
    :param analysis_results: 분석 결과 (딕셔너리 형태)
    :param graph_files: 포함할 그래프 이미지 파일 리스트
    :param file_name: 저장할 파일 이름
    """
    try:
        # PDF 설정
        doc = SimpleDocTemplate(
            file_name,
            pagesize=letter,
            rightMargin=50,
            leftMargin=50,
            topMargin=50,
            bottomMargin=50
        )

        # 스타일 설정
        styles = getSampleStyleSheet()
        story = [Paragraph("CAN Analysis Report", styles['Title']), Spacer(1, 20),
                 Paragraph("Analysis Results:", styles['Heading2'])]

        # 제목 추가

        # 분석 결과 추가
        for key, value in analysis_results.items():
            story.append(Paragraph(f"{key}: {value}", styles['Normal']))
        story.append(Spacer(1, 20))

        # 그래프 추가
        if graph_files:
            story.append(Paragraph("Graphs:", styles['Heading2']))
            for graph_file in graph_files:
                story.append(Image(graph_file, width=400, height=200))
                story.append(Spacer(1, 20))

        # PDF 생성
        doc.build(story)
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


def generate_pdf_report_with_anomalies(analysis_results, anomalies, file_name="report_with_anomalies.pdf"):
    """
    이상 탐지 결과를 포함한 PDF 보고서를 생성합니다.
    """
    from reportlab.lib.pagesizes import letter
    from reportlab.pdfgen import canvas

    try:
        c = canvas.Canvas(file_name, pagesize=letter)
        c.setFont("Helvetica", 12)
        c.drawString(100, 750, "CAN Analysis Report with Anomalies")
        c.drawString(100, 740, "=" * 30)

        # 분석 결과 추가
        y_position = 720
        for key, value in analysis_results.items():
            c.drawString(100, y_position, f"{key}: {value}")
            y_position -= 20

        # 이상치 결과 추가
        c.drawString(100, y_position - 20, "Detected Anomalies:")
        for index, anomaly in anomalies.iterrows():
            y_position -= 20
            c.drawString(100, y_position,
                         f"Timestamp: {anomaly['Timestamp']}, CAN_ID: {anomaly['CAN_ID']}, DLC: {anomaly['DLC']}")

        c.save()
        print(f"PDF report with anomalies saved as {file_name}")
    except Exception as e:
        print(f"Failed to save PDF report with anomalies: {e}")


def generate_pdf_report_with_graphs(analysis_results, graph_files, anomalies, file_name="report_with_graphs.pdf"):
    """
    그래프와 이상 탐지 결과를 포함한 PDF 보고서를 생성합니다.
    :param analysis_results: 분석 결과 딕셔너리
    :param graph_files: 포함할 그래프 이미지 파일 리스트
    :param anomalies: 이상 탐지 결과 (DataFrame)
    :param file_name: PDF 파일 이름
    """
    try:
        c = canvas.Canvas(file_name, pagesize=letter)
        c.setFont("Helvetica", 12)
        c.drawString(100, 750, "CAN Analysis Report with Graphs")
        c.drawString(100, 740, "=" * 50)

        # 분석 결과 추가
        y_position = 720
        for key, value in analysis_results.items():
            c.drawString(100, y_position, f"{key}: {value}")
            y_position -= 20

        # 그래프 추가
        for graph_file in graph_files:
            y_position -= 40
            c.drawImage(graph_file, 100, y_position, width=400, height=200)
            y_position -= 220

        # 이상 탐지 결과 추가
        if not anomalies.empty:
            c.drawString(100, y_position - 20, "Detected Anomalies:")
            y_position -= 40
            for _, row in anomalies.iterrows():
                c.drawString(100, y_position,
                             f"Timestamp: {row['Timestamp']}, CAN_ID: {row['CAN_ID']}, DLC: {row['DLC']}")
                y_position -= 20

        c.save()
        print(f"PDF report with graphs saved as {file_name}")
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

    # HTML 보고서 생성 테스트
    generate_html_report(sample_results, file_name="CAN_analysis_report.html")
