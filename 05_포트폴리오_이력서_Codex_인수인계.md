# 포트폴리오·이력서·BidMatch 작업 인수인계

최초 작성일: 2026-08-09

최종 갱신일: 2026-08-11
목적: 현재 PC를 사용하지 않게 되더라도 다른 Windows PC와 새 Codex 대화에서 포트폴리오, 이력서, 자기소개서와 BidMatch 프로젝트 작업을 그대로 이어가기 위한 기준 문서입니다.

## 1. 가장 먼저 확인할 내용

1. 이 저장소는 개인 경력 정리용 저장소입니다. 이력서에 전화번호와 이메일이 포함되므로 GitHub에서 **비공개 저장소인지 먼저 확인**합니다.
2. 이 문서를 끝까지 읽은 뒤 `00_읽어보기.md`부터 `04_BidMatch_근거목록.md`까지 확인합니다.
3. 강사 첨삭 원문은 `summary_김종록.txt`, 자기소개서 최신 원문은 `output/김종록_자기소개서_수정초안.md`입니다.
4. 이력서 문장을 바꿀 때 PDF나 DOCX를 직접 고치지 말고 `resume-tools/`의 생성 스크립트를 먼저 수정합니다.
5. 실제 수행 범위보다 크게 쓰지 않고, 확인하기 어려운 수치나 성과는 넣지 않습니다.

새 Codex 대화에서 사용할 시작 문장:

> `05_포트폴리오_이력서_Codex_인수인계.md`, `summary_김종록.txt`, `00_읽어보기.md`부터 `04_BidMatch_근거목록.md`까지 읽고 작업을 이어서 진행해 주세요. 강사 첨삭은 참고하되 실제 수행 범위, PL과 PM의 역할 구분, 과장 금지 기준과 현재 이력서 생성 방식을 유지해 주세요.

## 2. 저장소와 공개 주소

| 구분 | 주소 | 용도 |
| --- | --- | --- |
| 경력 정리 저장소 | `https://github.com/kjongrok/read.git` | 이 문서, 근거, 이력서·자기소개서, 포트폴리오 원본 백업 |
| 개인 포트폴리오 저장소 | `https://github.com/kjongrok/kjongrok.github.io.git` | GitHub Pages 배포용 |
| 개인 포트폴리오 | `https://kjongrok.github.io/` | 채용 담당자에게 전달할 공개 포트폴리오 |
| GitHub 프로필 | `https://github.com/kjongrok` | 개인 프로젝트와 프로필 README |
| BidMatch 조직 | `https://github.com/aiHuman1Team` | 최종 프로젝트 저장소 모음 |
| BidMatch 시연 영상 | `https://youtu.be/lD0j2pKL1PE` | 최종 프로젝트 시연 |

현재 `read` 저장소 브랜치:

- 작업 브랜치: `docs/bidmatch-career-notes`
- 원격 기본 브랜치도 현재 이 브랜치를 가리킵니다.
- 다른 PC에서 작업을 시작하기 전에 GitHub에서 최신 푸시 여부와 기본 브랜치를 다시 확인합니다.

## 3. 다른 PC에서 복제하는 순서

### 경력 정리 저장소

```powershell
git clone --branch docs/bidmatch-career-notes https://github.com/kjongrok/read.git
cd read
git status
```

브랜치를 `main`에 병합한 뒤라면 `--branch` 옵션 없이 복제하고 현재 브랜치를 확인합니다.

### GitHub Pages 포트폴리오

```powershell
git clone https://github.com/kjongrok/kjongrok.github.io.git
cd kjongrok.github.io
npm install
npm run dev
```

검증:

```powershell
npm run lint
npm run build
```

Node.js 20 이상을 권장합니다. `vite`를 찾지 못한다는 오류가 나오면 먼저 `npm install`을 실행합니다.

### 최종 BidMatch

필요한 저장소만 각각 복제합니다.

```powershell
git clone https://github.com/aiHuman1Team/front-end.git
git clone https://github.com/aiHuman1Team/back-end.git
git clone https://github.com/aiHuman1Team/ai.git
git clone https://github.com/aiHuman1Team/bruno.git
```

현재 자가 자격 진단 관련 개발 브랜치는 Frontend, Backend, AI 모두 `feature/eligibility-document-analysis`입니다. 원격에서 `main` 병합 여부를 확인한 뒤 적절한 브랜치를 사용합니다. Bruno는 `main`입니다.

## 4. 이력서와 자기소개서 기준 파일

`output/`의 주요 파일:

- `김종록_백엔드_AI응용개발자_이력서.docx`: 편집 가능한 이력서
- `김종록_백엔드_AI응용개발자_이력서.pdf`: 제출용 이력서, 2쪽
- `김종록_백엔드_AI응용개발자_이력서_자기소개서.docx`: 이력서·자기소개서 결합본
- `김종록_백엔드_AI응용개발자_이력서_자기소개서.pdf`: 제출용 결합본, 5쪽
- `김종록_자기소개서_수정초안.md`: 자기소개서 원문
- `김종록_잡코리아_입력용_문안.md`: 채용 사이트 입력용 문안

현재 이력서 구성:

1. 간략 소개
2. 간략 소개 바로 아래 클릭 링크: `Portfolio | GitHub | BidMatch Project | BidMatch Service`
3. 핵심 역량
4. 기술 스택
5. 병원 전산 경력의 담당 업무와 직무 연결점
6. 교육 이력과 AI 교육 핵심 내용
7. 대표 프로젝트와 프로젝트별 기술

강사 템플릿의 구조는 참고했지만, 6쪽 분량을 그대로 따라 하지 않고 신입 지원용 2쪽 이력서를 유지했습니다. 강사 첨삭 내용은 반영하되 실제 경험과 다른 제안은 그대로 사용하지 않습니다.

## 5. 이력서 재생성 환경과 명령

Windows, Python 3.12 기준입니다.

```powershell
cd read
py -3.12 -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
pip install python-docx pypdf reportlab
```

생성 스크립트:

- `resume-tools/build_resume.py`: 이력서 DOCX 생성
- `resume-tools/update_resume_pdf.py`: 이력서 PDF 생성
- `resume-tools/merge_resume_cover_letter.py`: 이력서와 자기소개서 결합본 생성

실행:

```powershell
python resume-tools/build_resume.py
python resume-tools/update_resume_pdf.py
python resume-tools/merge_resume_cover_letter.py `
  --resume-docx "output/김종록_백엔드_AI응용개발자_이력서.docx" `
  --resume-pdf "output/김종록_백엔드_AI응용개발자_이력서.pdf" `
  --cover-letter "output/김종록_자기소개서_수정초안.md" `
  --output-docx "output/김종록_백엔드_AI응용개발자_이력서_자기소개서.docx" `
  --output-pdf "output/김종록_백엔드_AI응용개발자_이력서_자기소개서.pdf"
```

스크립트는 저장소 이름이나 드라이브 위치에 의존하지 않고 `resume-tools/`의 상위 폴더를 기준으로 `output/`을 찾도록 수정했습니다. PDF는 Windows의 맑은 고딕 글꼴을 사용합니다. 다른 운영체제에서는 글꼴 경로를 수정해야 합니다.

재생성 후 반드시 확인할 항목:

- 이력서 2쪽, 결합본 5쪽 유지 여부
- 페이지 하단 잘림과 문단 밀림 여부
- 전화번호, 이메일, 경력·교육 기간
- Portfolio, GitHub, BidMatch 링크 클릭 여부
- 공개 서비스 주소의 접속 여부
- DOCX를 Word 또는 LibreOffice로 열었을 때 줄바꿈 차이

## 6. 자기소개서와 강사 첨삭 반영 기준

강사 첨삭 원문: `summary_김종록.txt`

현재 자기소개서 문항:

1. 병원 전산 경험에서 개발자로 전환한 동기
2. Flyway 충돌과 기존 DB 호환 문제 해결
3. AI 결과를 그대로 믿지 않고 검색·검증·fallback을 둔 구조
4. PL로서 진행 상태를 직접 확인하고 PM과 우선순위·역할을 조정한 경험
5. 꼼꼼함을 우선순위 판단으로 보완한 경험
6. 동료의 서로 다른 강점을 이해하며 협업 기준을 넓힌 경험

작성 원칙:

- 병원 전산 3년 11개월은 개발 경력이 아니라 운영·사용자 지원 경험입니다.
- 머신러닝·딥러닝에서는 모델 개발 경험을, LLM 프로젝트에서는 에이전트·RAG 챗봇 구현 경험을 구분합니다.
- `30개 이상 부서`, `300건 이상 요청`, `40회 이상 교육`처럼 근거를 바로 설명하기 어려운 수치는 사용하지 않습니다.
- Flyway는 모든 회사가 사용하는 보편 기술처럼 강조하지 않고 실제 문제 해결 사례 안에서만 설명합니다.
- 지원 회사가 정해지면 필요한 문항만 선택하고 500자, 700자, 1,000자 등 요구 글자 수에 맞춥니다.
- 지나치게 반듯한 모범답안보다 실제 판단, 시행착오와 아쉬움이 드러나는 문장을 선호합니다.

## 7. 사실관계와 과장 금지 기준

### 병원 전산

- 여러 진료·행정부서의 OA 요구사항과 장애·사용자 요청을 처리했습니다.
- 반복 문의를 매뉴얼, 정책과 Q&A 형태로 정리하고 사용자 교육을 진행했습니다.
- 코로나19 기간 전자결재·원격 OA 접근 체계 전환 과정에서 사용자 안내와 장애 대응을 담당했습니다.
- 개발 경력으로 표현하지 않습니다.

### BidMatch 역할

- 공식 팀 구성은 5명이며 사용자는 프로젝트 리더(PL), PM은 별도 인원입니다.
- 회원·기업 인증, 기업정보·면허·실적, 고객센터, SSE 알림 API와 관련 사용자 흐름을 구현했습니다.
- FAQ RAG 챗봇과 첨부문서 기반 자가 자격 진단을 Backend 규칙·검증·대체 처리와 연결했습니다.
- 관리자 전체 시스템이나 관리자 대시보드를 단독 구현한 것으로 쓰지 않습니다.
- 관리자 기여는 회원 정보 표시, 고객센터·FAQ 관리, 메일·알림 상태 표시와 일부 환경 설정 보완 범위입니다.
- AI 공고 매칭 전체와 OCR 핵심 엔진은 사용자의 단독 구현이 아닙니다.
- Jenkins, Docker Compose, Nginx 기반 CI/CD 전체를 사용자가 구축했다고 쓰지 않습니다.
- 242건은 챗봇만이 아니라 문서 분석 등을 포함한 전체 AI 자동화 테스트 수입니다.
- 실제 입찰 성공률, 운영 사용자 수와 자가 자격 진단 정확도는 확인되지 않았습니다.

### 자가 자격 진단

- BGE-M3가 첨부문서 근거를 검색하고 Qwen/Ollama가 조건 유형을 분류합니다.
- 최종 자격 판정은 Spring Boot가 기업정보와 구조화 조건을 비교해 수행합니다.
- LLM이 비정상 응답을 반환하거나 시간 초과가 발생해도 기본 진단을 유지합니다.
- 분석 제외 파일명, 제외 사유와 원문 다운로드 링크를 안내합니다.
- 다양한 실제 공고에 대한 반복 검증 시간은 제한적이었으므로 완벽한 자동 판정을 주장하지 않습니다.

## 8. BidMatch 자가 자격 진단 재개 시 필수 설정

실제 값은 각 저장소의 `.env.example`을 복사해 `.env`에만 입력하고 Git에 올리지 않습니다.

Backend와 AI에서 일치해야 하는 값:

```text
ELIGIBILITY_DOCUMENT_API_KEY=동일한-강한-문자열
```

주요 Backend 변수:

```text
AI_API_BASE_URL=http://localhost:8000
ELIGIBILITY_DOCUMENT_CONNECT_TIMEOUT_MS=5000
ELIGIBILITY_DOCUMENT_READ_TIMEOUT_MS=15000
DOCUMENT_RAG_RETENTION_DAYS=3
DOCUMENT_RAG_CLEANUP_CRON=0 20 3 * * *
```

주요 AI 변수:

```text
EMBEDDING_MODEL_NAME=BAAI/bge-m3
RERANKER_MODEL_NAME=BAAI/bge-reranker-v2-m3
LLM_PROVIDER=ollama
LLM_MODEL=qwen3:4b-instruct
ELIGIBILITY_DOCUMENT_API_KEY=Backend와-같은-값
DOCUMENT_LLM_TIMEOUT_SECONDS=180
DOCUMENT_ANALYSIS_MAX_ATTEMPTS=4
DOCUMENT_RAG_RETENTION_DAYS=3
```

로컬 AI 실행:

```powershell
cd ai
py -3.12 -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
Copy-Item .env.example .env
python run.py
```

Ollama에는 `qwen3:4b-instruct` 모델이 필요합니다. BGE-M3와 reranker는 첫 실행 시 다운로드될 수 있으므로 네트워크와 저장 공간을 확인합니다. Gemini 키는 자가 자격 진단의 필수값이 아닙니다. 외부 챗봇 LLM을 사용할 때만 별도 설정을 검토합니다.

## 9. GitHub Pages 포트폴리오

`read/portfolio-source/`는 포트폴리오 원본 백업입니다. 실제 공개 저장소는 `kjongrok.github.io`입니다.

현재 공개 내용:

1. BidMatch 최종 프로젝트
2. 지능형 교통 관제 시스템
3. CCTV 교통량 이상탐지·예측
4. 항공편 지연 예측
5. 맞춤 공고 자동 수집·메일 알림 프로토타입

프로젝트 데이터: `portfolio-source/src/data/portfolio.js`

보고서 PDF: `portfolio-source/public/reports/`
공개 URL: `https://kjongrok.github.io/`

수정 절차:

1. `read/portfolio-source` 또는 `kjongrok.github.io` 복제본에서 내용을 수정합니다.
2. `npm run lint`와 `npm run build`를 실행합니다.
3. 공개 저장소 `main` 브랜치에 푸시합니다.
4. GitHub Actions와 Pages 배포 성공 여부를 확인합니다.
5. 시크릿 창과 모바일 화면에서 외부 링크, 보고서와 YouTube 영상을 확인합니다.

두 저장소의 포트폴리오 소스가 달라지지 않도록 최종 수정본을 양쪽에 동기화합니다.

## 10. 개인 프로젝트 링크

- Flask BidMatch: `https://github.com/kjongrok/BidMatch`
- 머신러닝: `https://github.com/kjongrok/Machine_Learning`
- 딥러닝: `https://github.com/kjongrok/Deep_Learning`
- LLM: `https://github.com/kjongrok/LLM`
- 머신러닝 시연: `https://youtu.be/K5FKWHqEpRM`
- 딥러닝 시연: `https://youtu.be/33S2lS5M61c`
- LLM 시연: `https://youtu.be/dR177JPcxXM`

## 11. Git에 올리기 전 체크리스트

```powershell
git status
git diff --stat
git diff -- README.md 05_포트폴리오_이력서_Codex_인수인계.md
```

반드시 확인:

- `.env`, API 키, 비밀번호, 토큰과 운영 인증정보가 없는지
- 이력서의 전화번호와 이메일을 공개 저장소에 올리는 것이 맞는지
- `summary_김종록.txt`를 첨삭 근거로 함께 추적할지
- `node_modules`, `dist`, 가상환경, 로그와 임시 렌더 파일이 제외됐는지
- DOCX와 PDF가 최신 MD·생성 스크립트에서 다시 생성된 버전인지
- GitHub Pages 공개 저장소와 `portfolio-source`의 내용이 일치하는지

현재 `summary_김종록.txt`는 아직 추적되지 않은 파일일 수 있으므로 커밋 전에 `git status`로 확인합니다.

## 12. 현재 상태와 다음 우선순위

2026-08-11 기준:

- 강사 이력서 템플릿과 첨삭 원문을 다시 검토했습니다.
- 강사 첨삭을 무시하지 않되 실제 수행 범위와 다른 표현은 제외했습니다.
- 이력서는 2쪽, 자기소개서 결합본은 5쪽으로 생성했습니다.
- 간략 소개 아래 Portfolio, GitHub, BidMatch 프로젝트와 서비스 링크를 배치했습니다.
- 이력서 생성 스크립트의 `D:\read` 고정 경로 의존을 제거했습니다.
- PDF에서 페이지 잘림과 링크 배치를 확인했습니다.
- 현재 변경사항은 아직 커밋·푸시하지 않은 상태일 수 있습니다.

다음 우선순위:

1. 이 문서와 최신 이력서 산출물을 함께 커밋·푸시합니다.
2. 다른 PC에서 `read`와 `kjongrok.github.io`를 복제합니다.
3. Word에서 DOCX 2쪽 배치와 클릭 링크를 최종 확인합니다.
4. 지원 공고가 정해지면 범용 자기소개서에서 필요한 문항만 선택해 회사·직무에 맞춥니다.
5. 지원 전 공개 서비스와 모든 링크를 한 번 확인합니다.

## 13. 사용자 소통 기준

- 반드시 존댓말을 사용합니다.
- 수정 위치를 문항, 섹션과 파일명으로 구분해 짧게 설명합니다.
- 사용자가 하지 않은 일을 임의로 성과나 기여로 추가하지 않습니다.
- 불확실한 내용은 프로젝트 코드, 보고서와 Git 이력으로 다시 확인합니다.
- `성공적으로 이끌었습니다`, `역량을 발휘했습니다`처럼 근거 없는 모범답안 표현을 피합니다.
- 문서 전체를 매번 반복하기보다 바뀐 위치와 이유를 우선 안내합니다.
