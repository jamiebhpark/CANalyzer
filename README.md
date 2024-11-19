```markdown
# CANalyzer

## 프로젝트 설명
CANalyzer는 차량의 CAN 데이터를 분석하고 시각화하는 Python 기반 도구입니다.  
분석 결과를 PDF 보고서로 생성하여 저장할 수 있습니다.

## 주요 기능
1. CAN 로그 데이터 파싱
2. CAN 데이터 필터링 및 통계 분석
3. 데이터 시각화 (CAN 메시지 빈도)
4. PDF 보고서 생성

---

## 실행 방법

### 1. 필수 라이브러리 설치
아래 명령어를 실행하여 프로젝트에 필요한 라이브러리를 설치하세요:
```bash
pip install -r requirements.txt
```

### 2. 샘플 데이터 생성
샘플 데이터를 생성하려면 아래 명령어를 실행하세요:
```bash
python src/create_sample_data.py
```

### 3. 프로그램 실행
메인 프로그램을 실행하여 CAN 데이터를 분석하고 보고서를 생성하세요:
```bash
python main.py
```

---

## 프로젝트 구조
```
CANalyzer/
│
├── data/                    # CAN 데이터 저장
│   └── sample_can_log.csv   # 샘플 CAN 로그 데이터
│
├── src/                     # 소스 코드
│   ├── __init__.py          # Python 패키지 초기화 파일
│   ├── can_parser.py        # CAN 데이터 파싱 모듈
│   ├── data_analysis.py     # CAN 데이터 분석 모듈
│   ├── data_visualization.py # 데이터 시각화 모듈
│   ├── report_generator.py  # 보고서 생성 모듈
│   └── create_sample_data.py # 샘플 데이터 생성 모듈
│
├── main.py                  # 메인 실행 파일
├── requirements.txt         # 필요한 라이브러리 목록
└── README.md                # 프로젝트 설명서
```

---

## 요구사항
- Python 3.8 이상
- 주요 라이브러리:
  - pandas
  - matplotlib
  - reportlab
  - python-can

---

## 주요 모듈 설명

### 1. `can_parser.py`
- **기능**: CAN 로그 데이터를 CSV 파일에서 읽어 Python 데이터프레임으로 변환합니다.
- **사용법**:
  ```python
  from src.can_parser import parse_can_log

  file_path = "data/sample_can_log.csv"
  data = parse_can_log(file_path)
  print(data.head())
  ```

### 2. `data_analysis.py`
- **기능**: CAN 데이터 필터링 및 통계 분석.
- **주요 함수**:
  - `filter_by_can_id`: 특정 CAN ID에 해당하는 데이터를 필터링합니다.
  - `calculate_message_frequency`: 각 CAN ID의 메시지 발생 빈도를 계산합니다.
  - `calculate_statistics`: 총 메시지 수, 고유 CAN ID 수, DLC 평균을 계산합니다.

### 3. `data_visualization.py`
- **기능**: 데이터를 시각화하여 그래프를 생성합니다.
- **주요 함수**:
  - `plot_message_frequency`: CAN ID의 발생 빈도를 막대 그래프로 시각화합니다.

### 4. `report_generator.py`
- **기능**: 분석 결과를 보고서로 저장합니다.
- **주요 함수**:
  - `generate_report`: 텍스트 파일 보고서를 생성합니다.
  - `generate_pdf_report`: PDF 파일 보고서를 생성합니다.

### 5. `create_sample_data.py`
- **기능**: 샘플 CAN 데이터를 생성하여 `data/sample_can_log.csv` 파일로 저장합니다.

---

## 실행 예시

1. 샘플 데이터 생성:
   ```bash
   python src/create_sample_data.py
   ```

2. 메인 프로그램 실행:
   ```bash
   python main.py
   ```

3. 결과:
   - **PDF 보고서**: `CAN_analysis_report.pdf`가 프로젝트 폴더에 생성됩니다.
   - **시각화**: 메시지 빈도 그래프가 화면에 표시됩니다.

---

## 기여 방법
1. 프로젝트를 포크합니다.
2. 새로운 기능을 추가하거나 버그를 수정합니다.
3. Pull Request를 제출합니다.

---

## 라이선스
이 프로젝트는 [MIT License](LICENSE)에 따라 배포됩니다.