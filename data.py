# 🏦 신한은행 면접 스터디 앱

2026 상반기 신한은행 채용 대비 면접 스터디 Streamlit 앱입니다.

## 📚 포함 내용

- 🏦 **핵심 은행업** — 수신·여신·외환·전자금융 전체 카드
- 📱 **디지털·플랫폼** — SOL앱·AI브랜치·BaaS·땡겨요·CBDC
- ⚡ **강점·SWOT** — 면접 차별화 포인트·핵심 수치 암기

## 🚀 배포 방법 (Streamlit Cloud)

### 1단계. GitHub에 올리기
```bash
git init
git add .
git commit -m "신한은행 면접 스터디 앱"
git branch -M main
git remote add origin https://github.com/[내 유저명]/shinhan-study.git
git push -u origin main
```

### 2단계. Streamlit Cloud 배포
1. https://share.streamlit.io 접속
2. GitHub 계정 연결
3. **New app** 클릭
4. Repository: `shinhan-study` 선택
5. Main file path: `app.py` 선택
6. **Deploy!** 클릭

### 3단계. 완료!
- 배포된 URL을 북마크해서 언제든 공부하세요
- 무료로 24시간 접속 가능합니다

## 🗂️ 파일 구조

```
shinhan_study/
├── app.py              # 메인 홈 화면
├── data.py             # 신한은행 전체 데이터
├── requirements.txt    # 패키지 목록
├── README.md
└── pages/
    ├── 1_🏦_핵심_은행업.py
    ├── 2_📱_디지털_플랫폼.py
    └── 3_⚡_강점_SWOT.py
```

## 💡 로컬 실행 방법

```bash
pip install streamlit
streamlit run app.py
```
