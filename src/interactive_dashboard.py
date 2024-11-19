import os
import sys
import dash
from dash import dcc, html
from dash.dependencies import Input, Output
import pandas as pd
from src.can_parser import parse_can_log
from src.data_analysis import filter_by_time_range

# 현재 파일의 상위 디렉토리를 sys.path에 추가
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

# 샘플 데이터 로드
file_path = "data/sample_can_log.csv"
data = parse_can_log(file_path)

# Dash 앱 초기화
app = dash.Dash(__name__)

# 앱 레이아웃 정의
app.layout = html.Div([
    html.H1("CANalyzer Interactive Dashboard", style={'textAlign': 'center'}),

    # CAN ID 선택 드롭다운
    html.Label("Select CAN ID:"),
    dcc.Dropdown(
        id='can-id-selector',
        options=[{'label': can_id, 'value': can_id} for can_id in data["CAN_ID"].unique()],
        placeholder="Select a CAN ID",
    ),

    # 시간 범위 슬라이더
    html.Label("Time Range (seconds):"),
    dcc.RangeSlider(
        id='time-slider',
        min=data["Timestamp"].min(),
        max=data["Timestamp"].max(),
        step=0.001,
        value=[data["Timestamp"].min(), data["Timestamp"].max()],
        marks={round(t, 3): str(round(t, 3)) for t in data["Timestamp"].unique()[:10]}  # 표시 제한
    ),

    # 그래프 출력
    dcc.Graph(id='time-series-graph'),
])


# 콜백 설정: 드롭다운과 슬라이더를 통해 그래프 업데이트
@app.callback(
    Output('time-series-graph', 'figure'),
    [Input('can-id-selector', 'value'),
     Input('time-slider', 'value')]
)
def update_graph(selected_can_id, time_range):
    # 시간 범위 필터링
    filtered_data = filter_by_time_range(data, time_range[0], time_range[1])
    # CAN ID 필터링
    if selected_can_id:
        filtered_data = filtered_data[filtered_data["CAN_ID"] == selected_can_id]

    # 빈도 계산
    time_series = filtered_data["Timestamp"].value_counts().sort_index()

    # 그래프 반환
    return {
        'data': [{'x': time_series.index, 'y': time_series.values, 'type': 'line', 'name': 'Frequency'}],
        'layout': {
            'title': f"Message Frequency for CAN ID {selected_can_id}" if selected_can_id else "Message Frequency"}
    }


# 앱 실행
if __name__ == '__main__':
    app.run_server(debug=True)
