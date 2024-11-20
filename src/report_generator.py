import os
import sys
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Image, Table, TableStyle
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib import colors

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from reportlab.platypus import KeepTogether


def generate_pdf_report(
        analysis_results,
        graph_files=None,
        anomalies=None,
        evaluation_report=None,
        time_interval_stats=None,
        file_name="report.pdf",
        report_type="basic"
):
    """
    통합 PDF 보고서를 생성합니다.
    """
    try:
        from reportlab.platypus import PageBreak

        doc = SimpleDocTemplate(
            file_name,
            pagesize=letter,
            rightMargin=50,
            leftMargin=50,
            topMargin=50,
            bottomMargin=50
        )
        styles = getSampleStyleSheet()
        story = [Paragraph("CAN Analysis Report", styles['Title']), Spacer(1, 20),
                 Paragraph("Analysis Results:", styles['Heading2'])]

        # 1. Analysis Results
        for key, value in analysis_results.items():
            story.append(Paragraph(f"{key}: {value}", styles['Normal']))
        story.append(Spacer(1, 20))

        # 2. Detected Anomalies
        if report_type in ["with_anomalies", "with_graphs"] and anomalies is not None:
            table_data = [["Timestamp", "CAN_ID", "DLC"]] + [
                [row["Timestamp"], row["CAN_ID"], row["DLC"]] for _, row in anomalies.iterrows()
            ]
            table = Table(table_data, colWidths=[150, 150, 150])
            table.setStyle(TableStyle([
                ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor("#d3d3d3")),
                ('TEXTCOLOR', (0, 0), (-1, 0), colors.black),
                ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
                ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
                ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
                ('GRID', (0, 0), (-1, -1), 0.5, colors.grey)
            ]))
            story.append(KeepTogether([Paragraph("Detected Anomalies:", styles['Heading2']), table]))
            story.append(Spacer(1, 20))

        # 3. Time Interval Statistics
        if time_interval_stats:
            story.append(Paragraph("Time Interval Statistics:", styles['Heading2']))
            for key, value in time_interval_stats.items():
                story.append(Paragraph(f"{key}: {value:.6f} seconds", styles['Normal']))
            story.append(Spacer(1, 20))

        # 4. Data Quality Evaluation
        if evaluation_report:
            story.append(Paragraph("Data Quality Evaluation:", styles['Heading2']))
            story.append(Paragraph(evaluation_report.replace("\n", "<br />"), styles['Normal']))
            story.append(Spacer(1, 20))

        # 5. Graphs
        if report_type in ["with_graphs", "with_anomalies"] and graph_files:
            graph_titles = ["Message Frequency by CAN ID", "Anomaly Detection Results", "Message Frequency Over Time",
                            "Message Time Intervals"]
            for title, graph_file in zip(graph_titles, graph_files):
                if os.path.exists(graph_file):
                    graph_group = KeepTogether([
                        Paragraph(title, styles['Heading3']),
                        Image(graph_file, width=400, height=200),
                        Spacer(1, 20)
                    ])
                    story.append(graph_group)
                else:
                    story.append(Paragraph(f"Graph file not found: {graph_file}", styles['Normal']))

        # PDF 생성
        doc.build(story)
        print(f"PDF report saved as {file_name}")
    except Exception as e:
        print(f"Failed to save PDF report: {e}")


def generate_html_report(
        analysis_results,
        graph_files=None,
        evaluation_report=None,
        time_interval_stats=None,  # 시간 간격 통계 추가
        anomalies=None,  # 이상 탐지 결과 추가
        file_name="report.html"
):
    """
    HTML 보고서를 생성합니다.
    """
    try:
        with open(file_name, "w", encoding="utf-8") as file:
            # HTML 시작
            file.write("<html><head><title>CAN Analysis Report</title></head><body>")
            file.write("<h1>CAN Analysis Report</h1>")

            # 1. Analysis Results
            file.write("<h2>Analysis Results:</h2>")
            file.write("<table border='1' style='border-collapse: collapse; width: 50%;'>")
            file.write("<tr><th>Metric</th><th>Value</th></tr>")
            for key, value in analysis_results.items():
                file.write(f"<tr><td>{key}</td><td>{value}</td></tr>")
            file.write("</table>")

            # 2. Detected Anomalies
            if anomalies is not None and not anomalies.empty:
                file.write("<h2>Detected Anomalies:</h2>")
                file.write("<table border='1' style='border-collapse: collapse; width: 80%;'>")
                file.write("<tr><th>Timestamp</th><th>CAN_ID</th><th>DLC</th></tr>")
                for _, row in anomalies.iterrows():
                    file.write(f"<tr><td>{row['Timestamp']}</td><td>{row['CAN_ID']}</td><td>{row['DLC']}</td></tr>")
                file.write("</table>")

            # 3. Time Interval Statistics
            if time_interval_stats:
                file.write("<h2>Time Interval Statistics:</h2>")
                file.write("<ul>")
                for key, value in time_interval_stats.items():
                    file.write(f"<li>{key}: {value:.6f} seconds</li>")
                file.write("</ul>")

            # 4. Data Quality Evaluation
            if evaluation_report:
                file.write("<h2>Data Quality Evaluation:</h2>")
                file.write("<pre>")
                file.write(evaluation_report)
                file.write("</pre>")

            # 5. Graphs
            if graph_files:
                file.write("<h2>Graphs:</h2>")
                for graph_file in graph_files:
                    if os.path.exists(graph_file):
                        file.write(f"<div><img src='{graph_file}' alt='Graph' style='width: 80%;'></div><br>")
                    else:
                        file.write(f"<p>Graph file not found: {graph_file}</p>")

            # HTML 종료
            file.write("</body></html>")

        print(f"HTML report saved as {file_name}")
    except Exception as e:
        print(f"Failed to save HTML report: {e}")

