# BidMatch 근거 목록

## 1. 개인 식별과 기간

- Git 작성자: `kjong`, `kjongrok`
- Git 메일: `xhxhahs2@gmail.com`, `xhxhahs2@naver.com`
- 확인된 기여 기간: 2026-07-15 ~ 2026-08-05
- 공식 역할: Project Leader
- 공식 담당: 기업정보·인증·실적, OCR·자가 자격 진단, 챗봇·알림·고객센터 개선

## 2. 저장소별 커밋 근거

### Backend - 42개 비병합 커밋

대표 커밋:

| 해시 | 내용 |
| --- | --- |
| `7b4831a` | 일반회원 회원가입 |
| `424c2bf` | 기업회원 가입·이메일 인증·국세청 검증 |
| `eb87e37` | 비밀번호 재설정 |
| `5534654` | 기업회원 이메일 찾기 |
| `ba34608` | 사용자 프로필 관리 |
| `6af9a6a` | 기업정보·면허 카탈로그 관리 |
| `e3e8b77` | 자사 실적 관리 |
| `16f8f86` | 비밀번호 변경·회원 탈퇴 |
| `710b078` | 회원 1:1 문의 |
| `d6ce86f` | 문의 페이징과 패키지 리팩터링 |
| `87b8052` | 관심조건 관리 |
| `05178bf` | AI 챗봇 중계 API |
| `105e108` | 인증·비밀번호 메일 이력 |
| `7e9a2fd` | 사업자등록증 OCR 중계 API |
| `d653d37` | 나라장터 면허 조회와 상태 이력 |
| `00f974f` | 공고 자격요건 기반 자가 진단 |
| `3424684` | 알림 이력과 SSE |
| `a932ed7` | 챗봇·OCR 로그 분리 |
| `c0c98c9` | 관리자·알림·고객센터 API 개선 |
| `116f53f` | 규칙 기반 기본 자격 확인 |
| `914bdfa` | 첨부문서 자가 자격 진단·비동기·정리 |

### User Frontend - 38개 비병합 커밋

대표 커밋:

| 해시 | 내용 |
| --- | --- |
| `c9436ed` | 회원가입 화면 |
| `5f7c313` | 비밀번호 재설정 화면 |
| `97b22aa` | 기업 이메일 찾기 |
| `de4a059` | 사용자 정보 화면 |
| `ae34fe6` | 기업정보 화면 |
| `5c98221` | 자사 실적 화면 |
| `7eac239` | 보안·비밀번호 화면 |
| `4afaf48` | 관심조건 화면 |
| `aec5aa1` | 고객센터 게시판형 UI |
| `0620b2e` | 챗봇 상담 UI |
| `f05dba6` | 기업 재인증·문서 미리보기·비밀번호 UX |
| `e09db78` | OCR 자동입력 |
| `2f01e58` | 나라장터 면허 상태 안내 |
| `ff0dd33` | OCR 주소와 우편번호 연동 |
| `1cba552` | 자가 자격 진단 결과·근거 UI |
| `1c3a6e3` | 알림 상세·실시간 갱신 UI |
| `055b4e5` | 고객센터와 알림 UX 개선 |
| `7ce00a6` | 규칙 기반 기본 자격 확인 화면 |
| `b26dbb8` | 최종 자가 자격 진단 UI 개선 |

### AI - 8개 비병합 커밋

| 해시 | 내용 |
| --- | --- |
| `0a7283d` | FAQ 기반 RAG 챗봇 |
| `654567b` | 챗봇 로그와 민감정보 마스킹 |
| `01a7dee` | 초기 첨부문서·자격요건 분석 |
| `15e4778` | 챗봇 로그 테이블명 정리 |
| `537bb40` | 불안정했던 초기 문서 분석 기능 제거 |
| `c1b37e2` | FAQ 검색·fallback·LangSmith 개선 |
| `3f6d85a` | 최종 첨부문서 자가 자격 분석 |

`95e6160`은 OCR 연동 환경변수 문서화입니다.

### Admin Frontend - 2개 비병합 커밋

| 해시 | 내용 |
| --- | --- |
| `6b21079` | 회원·고객센터·알림 관리 개선 |
| `7d6ed04` | FAQ 삭제와 답변 서식 개선 |

### Bruno - 28개 비병합 커밋

인증·기업정보·면허·실적·관심조건·고객센터·OCR·챗봇·알림 SSE·자가 자격 진단과 관리자 API 요청 파일이 확인됐습니다.

## 3. 현재 코드 근거

### Backend 주요 패키지

- `com.bidmatch.auth`: 가입, 기업 인증, 이메일, 국세청, 비밀번호 재설정, OCR Client
- `controller.user.profile`: 사용자 프로필
- `controller.user.security`: 비밀번호 변경·탈퇴
- `controller.user.businessprofile`: 기업정보·면허
- `controller.business`: 자사 실적
- `controller.support`, `service.support`: 고객센터·공지
- `controller.user.notification`: 알림 이력·SSE
- `support.chatbot`: 챗봇 중계
- `controller.user.eligibility`, `service.bid.EligibilityDiagnosisService`: 자가 자격 진단
- `controller.admin`: 회원·증빙·알림·고객센터 운영 API

### AI 주요 모듈

- `app/chatbot.py`: FAQ 검색, 권한, fallback, 다중 의도
- `app/chatbot_log.py`: 로그와 민감정보 마스킹
- `app/chatbot_tracing.py`: LangSmith 추적
- `app/faq_dataset.py`: 승인·검토 FAQ 데이터
- `app/document_eligibility.py`: 문서 추출·검색·조건 분류·캐시·상태
- `app/llm_client.py`: Ollama LLM 호출·시간 제한

### Frontend 주요 화면

- `SignUp`, `Login`, `PasswordReset`, `FindCompanyEmail`
- `MyInfo`
- `InterestConditions`
- `PublicSupport`, `SupportCenter`
- `Notifications`, `NotificationDetail`
- `NoticeDetail`, `eligibilityApi`

## 4. DB·Flyway 근거

본인 기능과 직접 연결된 주요 마이그레이션:

- V1~V4: 면허 카탈로그 정리
- V5: 자사 실적 사용자 관리 정책
- V6: 비밀번호 변경 시각
- V7: 휴면 상태
- V8·V9: 레거시 컬럼 보정
- V14: 문의 취소 상태
- V17: 이메일 이력
- V24: 사업자번호 UNIQUE 제약 보정
- V31: 관심조건 매칭 진행
- V33: 사용자 보유 면허
- V36: 챗봇 로그명·OCR 로그
- R__create_notification_log_items: 사용자 알림 항목
- V38·V39: 초기 공고 문서·자격 분석
- V45·V46: 최종 문서 RAG·비동기 자가 자격 진단

## 5. 테스트 근거

### Backend

- 회원가입·이메일·로그인·비밀번호 재설정
- 사용자 보안·탈퇴
- 기업정보·나라장터 면허 상태 전이
- 실적 등록·수정 날짜 검증
- 관심조건
- 고객센터·공지·관리자 문의
- 알림·운영 API
- 기본 자격 진단과 문서 근거 병합
- 문서 RAG 데이터 정리

### AI

- 챗봇 역할 필터·유사도·모호한 질문·복합 의도·fallback
- FAQ 데이터 승인 상태와 평가셋 참조
- DB 로그와 LangSmith 민감정보 마스킹
- 미지원 문서 사유·내부 오류 숨김
- 일반 안내·평가·하도급 제재·보증 정산 문구 제외
- 실적·하도급·서약서 문장의 사용자용 정리
- 복수 면허 전체 등록 조건
- 일반 기준 첨부문서 제외

## 6. 2026-08-07 직접 실행 검증

| 대상 | 결과 |
| --- | --- |
| Backend `gradlew.bat test` | 성공, 16초 |
| User Frontend `npm run build` | 성공, 1,680 modules, 약 19.74초 |
| AI `pytest -q` | 242 passed, 1 warning, 166.14초 |
| Admin Frontend `npm run build` | 성공, 1,650 modules, 약 16.56초 |

### 남은 경고

- User Frontend JavaScript 번들 약 839kB로 Vite 500kB 경고
- AI Starlette TestClient의 기존 httpx 사용 중단 예정 경고

## 7. 문서 근거

- 공식 GitHub Profile README
  - 김종록 역할: Project Leader
  - 기업정보·인증·실적 관리
  - OCR 및 자가 자격 진단
  - 챗봇·알림·고객센터 개선
- 최종보고서 자가 자격 진단 섹션
  - 주 담당자 김종록, 부 담당자 모하영
  - BGE-M3 근거 검색, Qwen 유형 분류, Backend 판정
  - 문서 실패·지연·오탐·모호한 출력·조건 충돌·LLM 실패 대응

## 8. 검증에서 제외하거나 보수적으로 표현한 내용

- Git merge 커밋은 개인 구현 커밋 수에서 제외
- AI 매칭·OCR 엔진·CI/CD·관리자 전체 기능은 팀 기여로 분리
- 실제 측정하지 않은 정확도·속도 개선율은 제외
- 운영 사용자 수와 실제 입찰 성공 사례는 확인되지 않아 제외
- 커밋 수는 코드 품질이나 기여 난이도의 절대 지표로 사용하지 않음
