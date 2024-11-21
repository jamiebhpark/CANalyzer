### **`README.md`**

```markdown
# CANalyzer: CAN 데이터 분석 도구

**CANalyzer**는 CAN (Controller Area Network) 로그 데이터를 분석, 시각화, 보고할 수 있는 통합 도구입니다. 자동차 산업에서 활용할 수 있는 진단 및 분석 기술을 시뮬레이션하며, 실무에 적합한 기능을 갖춘 프로젝트입니다.

---

## **기능**

1. **CAN 데이터 분석**:
   - 총 메시지 수, 고유 CAN ID 수, 평균 DLC 등 주요 통계 계산.
   - 데이터 품질 평가를 통해 짧은 시간 간격 또는 잘못된 DLC 값 경고.

2. **데이터 시각화**:
   - CAN ID별 메시지 빈도 막대 그래프.
   - 시간 기반 메시지 빈도와 이상 탐지 결과 시각화.
   - 메시지 간 시간 간격 통계 및 시각화.

3. **진단 및 이상 탐지**:
   - Isolation Forest 기반 이상 탐지.
   - 데이터 품질 및 진단 결과 요약 제공.

4. **보고서 자동화**:
   - **PDF** 및 **HTML** 형식으로 보고서 생성:
     - 분석 결과, 진단 요약, 이상 탐지 결과, 그래프 포함.

5. **실시간 스트리밍 시뮬레이션**:
   - CAN 데이터 실시간 스트리밍 시뮬레이션.
   - 실시간 이상 탐지 및 경고 시스템.

6. **사용자 친화적 명령줄 인터페이스 (CLI)**:
   - 데이터 파일 및 보고서 형식을 명령줄에서 지정 가능.

---

## **설치 방법**

1. 레포지토리 클론:
   ```bash
   git clone https://github.com/yourusername/CANalyzer.git
   cd CANalyzer
   ```

2. 필요한 패키지 설치:
   ```bash
   pip install -r requirements.txt
   ```

3. 설치 확인:
   ```bash
   python main.py --help
   ```

---

## **사용법**

### **1. 데이터 분석 및 보고서 생성**
CAN 로그 데이터를 분석하고 보고서를 생성하려면:
```bash
python main.py --file data/sample_can_log.csv --report-type pdf
```

### **2. 실시간 스트리밍 시뮬레이션**
실시간 데이터 스트리밍과 이상 탐지를 시뮬레이션하려면:
```bash
python src/real_time_streaming.py
```

### **3. 보고서 형식**
- `--report-type pdf`: PDF 보고서 생성.
- `--report-type html`: HTML 보고서 생성.

---

## **프로젝트 구조**

```plaintext
CANalyzer/
│
├── data/                              # 샘플 데이터 파일
│   └── sample_can_log.csv
│
├── src/                               # 소스 코드
│   ├── anomaly_detection.py           # 이상 탐지 로직
│   ├── can_parser.py                  # CAN 로그 파일 파싱
│   ├── data_analysis.py               # 데이터 분석 함수
│   ├── data_visualization.py          # 데이터 시각화 함수
│   ├── report_generator.py            # PDF 및 HTML 보고서 생성
│   ├── real_time_streaming.py         # 실시간 스트리밍 시뮬레이션
│   └── __init__.py
│
├── main.py                            # 분석 및 보고서 생성 엔트리 포인트
├── README.md                          # 프로젝트 설명
├── requirements.txt                   # 의존성 파일
└── .venv/                             # Python 가상 환경 (선택 사항)
```

---

## **샘플 출력**

### **PDF 보고서**
- 분석 결과, 이상 탐지, 시간 간격 통계, 그래프 포함.
- 샘플 보고서: [CAN_analysis_report.pdf](sample_report.pdf)

### **HTML 보고서**
- 상호작용 가능한 테이블과 그래프 포함.

---

## **사용된 기술**

- **Python**: 주요 프로그래밍 언어.
- **Pandas**: 데이터 조작 및 분석.
- **Matplotlib**: 데이터 시각화.
- **ReportLab**: PDF 생성.
- **sklearn**: 머신러닝 기반 이상 탐지.

---

## **향후 개선점**

1. **고급 시각화**:
   - 히트맵과 상관 관계 그래프 추가.
2. **실시간 경고 시스템 강화**:
   - 이메일 또는 슬랙 알림 기능 추가.
3. **대규모 데이터 처리 지원**:
   - Spark 또는 Dask와의 통합으로 대규모 데이터 처리 성능 강화.

---

## **기여 방법**

기여를 환영합니다! 다음 단계를 따라주세요:
1. 레포지토리를 포크하세요.
2. 새 브랜치 생성 (`feature/your-feature`).
3. 변경 사항 커밋.
4. 풀 리퀘스트 제출.

---

## **문의**

질문이나 제안이 있다면 언제든 연락 주세요:

- 이름: 박종훈
- 이메일: jamiebhpark@gmail.com

---

**CANalyzer**: 자동차 산업을 위한 데이터 기반 진단의 미래를 만들어 갑니다.
