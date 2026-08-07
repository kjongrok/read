# BidMatch 전체 작업내역

## 1. 프로젝트 개요

BidMatch는 나라장터 공고를 수집·정규화하고 기업정보와 관심조건을 이용해 적합한 공고를 추천하는 공공입찰 지원 서비스입니다. 공고 검색, 기업 인증, AI 매칭, 자가 자격 진단, 관심조건, 일정·알림, 고객센터와 관리자 운영 기능을 하나의 흐름으로 연결했습니다.

### 공식 역할

- 역할: Project Leader
- 공식 담당: 기업정보·인증·실적 관리, OCR 및 자가 자격 진단, 챗봇·알림·고객센터 개선
- 실제 기여 범위: Backend, User Frontend, AI, Admin Frontend, Bruno API 검증

## 2. 개인 기여 범위 구분

| 구분 | 의미 |
| --- | --- |
| 직접 구현 | 본인 커밋에서 핵심 Controller, Service, UI 또는 AI 모듈 생성이 확인됨 |
| 연동·개선 | 팀원이 구현한 기능을 Backend·Frontend와 연결하거나 운영·예외 처리를 개선함 |
| 팀 전체 기능 | 서비스에는 존재하지만 본인 단독 구현으로 주장하지 않아야 함 |

## 3. 인증·회원·보안

### 직접 구현

- 일반회원 회원가입 API와 입력 검증
- 기업회원 가입, 이메일 인증, 사업자등록정보 진위 확인 연동
- 로그인 사용자 세션 조회 및 로그인 상태 처리
- 비밀번호 재설정 메일 발송·인증·변경 흐름
- 기업회원 가입 이메일 찾기
- 내 정보 조회·수정
- 비밀번호 변경 및 동일 비밀번호 거부
- 회원 탈퇴 시 계정 상태 전이와 개인정보 비식별화
- 비밀번호 최종 변경 시각 저장
- 휴면 계정 상태 스키마 반영

### 개선 및 트러블슈팅

- 국세청 진위 확인 응답 계약과 실패 처리 보완
- 국세청 호출 진단 로그 추가
- 기업 재인증과 인증 메일 처리 개선
- 비밀번호 재설정 토큰 만료 검증
- 로그인 성공 응답의 실제 사용자 이름 반환
- 회원가입 IP 수집 로직과 개인정보처리방침 문구 제거
- 기존 사업자등록번호 UNIQUE 제약과 가입 정책의 충돌을 Flyway로 해소

### 주요 Backend API

- `/api/auth/signup`
- `/api/auth/company-signup`
- `/api/auth/email-verification/send`
- `/api/auth/email-verification/verify`
- `/api/auth/validate-business`
- `/api/auth/check-email`
- `/api/auth/password-reset/send`
- `/api/auth/password-reset/verify`
- `/api/auth/password-reset/confirm`
- `/api/auth/find-company-email`
- `/api/auth/me`
- `/api/user/profile`
- `/api/user/security`
- `/api/user/security/password`
- `/api/user/security/account`

## 4. 기업정보·기업 인증·면허

### 직접 구현

- 기업 프로필 조회·수정·인증 신청 API
- 기업정보 입력 및 주소·업태·업종·대표자 관리 화면
- 기업 인증 신청 시 사업자등록증 파일 저장
- 면허 카탈로그 조회 API
- 나라장터 기업 보유 면허 조회 Client 및 API
- 사용자 보유 면허의 출처와 상태 이력 관리
- 나라장터 조회 면허와 직접 등록 면허 통합 표시
- 기업 프로필 변경 후 공고 매칭과 자격 진단에서 사용할 데이터 구조 연결

### 면허 상태 모델

- 출처: 나라장터 조회 또는 사용자 직접 등록
- 상태: 활성, 나라장터에서 미확인, 사용자 제거
- 나라장터에서 사라진 면허만 비활성화하고 수동 등록 면허는 유지
- 미확인 면허를 사용자가 직접 등록 면허로 전환하거나 제거 가능
- 복수 면허 중 실제로 누락된 면허만 상태 변경

### 주요 Backend API

- `/api/user/company-profile`
- `/api/user/company-profile/application`
- `/api/user/company-profile/business-license`
- `/api/user/company-profile/registered-licenses`
- `/api/user/business-license-catalog`

## 5. 사업자등록증 OCR 연동

### 본인 기여

- Backend에서 AI OCR 서버를 호출하는 중계 API 구현
- OCR 요청·응답 계약과 예외 응답 연결
- 회원가입·기업 재인증 화면에 OCR 자동입력 연동
- OCR로 인식된 주소를 우편번호 검색 흐름과 연결
- OCR 요청과 결과의 별도 이력 테이블 및 저장 로직 구현
- OCR 내부 오류를 사용자용 오류와 구분
- 환경변수와 Bruno 요청 추가

### 기여 범위 주의

PaddleOCR·EasyOCR 엔진, 이미지 전처리 및 필드 추출 알고리즘의 핵심 구현은 팀 기여입니다. 본인은 OCR 엔진을 서비스의 회원가입·기업정보 흐름에 연결하고 API 계약, UI 자동입력, 이력 저장을 구현한 것으로 설명합니다.

### 주요 API

- `/api/auth/business-document/ocr`
- 관리자 증빙 OCR 재처리 API

## 6. 자사 수행실적 관리

### 직접 구현

- 실적 목록 조회, 등록, 수정, 삭제 API
- 계약명·발주처·계약금액·착수일·준공일·업무유형·설명 관리
- 사용자 프로필 화면의 실적 입력 및 목록 UI
- 직접 입력 데이터임을 안내하고 자격진단·매칭에 활용할 수 있도록 연결
- 준공일 기준 정렬 개선
- 날짜 연도를 네 자리 범위로 제한하는 Backend·Frontend 검증

### 주요 API

- `/api/business/performances`
- `/api/business/performances/{performanceId}`

## 7. 고객센터·공지·FAQ

### 직접 구현

- 비회원 고객센터 문의 등록
- 로그인 사용자 1:1 문의 등록·목록·상세 조회
- 문의 목록 페이징
- 문의 수정 및 접수 취소 상태
- 관리자 고객센터 문의 답변 및 상태 관리 개선
- 게시 공지사항 목록·상세·검색·페이징 API
- 고객센터 게시판형 UI와 문의 작성 화면
- 관리자 공지·FAQ 삭제 API 및 화면
- FAQ 답변의 링크와 강조 서식 표시 개선

### 주요 API

- `/api/support/public/inquiries`
- `/api/support/inquiries`
- `/api/support/inquiries/{inquiryId}`
- `/api/support/inquiries/{inquiryId}/cancel`
- `/api/support/notices`
- 관리자 문의·공지·FAQ 운영 API

## 8. 관심조건 관리

### 직접 구현

- 사용자별 관심조건 목록·등록·수정·삭제
- 활성·비활성 상태 변경
- 조건 소유권 검증과 예외 응답
- 관심조건 등록 시 매칭 작업과 연결
- 키워드 입력 검증 강화
- 프론트에서 복수 지역과 복수 공고 유형 선택 지원
- 매칭 진행 상태와 재매칭 요청 API 연동

### 기여 범위 주의

BGE-M3 기반 AI 매칭 알고리즘과 최종 추천 모델 전체를 단독 구현한 것은 아닙니다. 본인은 기업·관심조건 데이터를 관리하고 매칭 작업이 실행될 수 있도록 사용자 기능과 API를 구현한 것으로 설명합니다.

### 주요 API

- `/api/user/interest-conditions`
- `/api/user/interest-conditions/{conditionId}`
- `/api/user/interest-conditions/{conditionId}/active`
- `/api/user/interest-conditions/{conditionId}/matching-progress`
- `/api/user/interest-conditions/{conditionId}/rematch`

## 9. 알림 이력과 실시간 알림

### 직접 구현

- 사용자 알림 이력 목록·상세 조회
- 알림 단건 읽음 및 전체 읽음 처리
- 알림과 관련 공고 항목을 별도 구조로 관리
- SSE 기반 실시간 알림 구독 API
- 알림 변경 이벤트 발행과 사용자별 SSE 연결 관리
- SSE 예외 처리
- 사용자 화면의 실시간 갱신 및 알림 상세 화면
- 관리자 알림 전송·조회 화면 일부 개선

### 주요 API

- `/api/user/notifications/stream`
- `/api/user/notifications`
- `/api/user/notifications/{notificationId}`
- `/api/user/notifications/{notificationId}/read`
- `/api/user/notifications/read-all`
- `/api/admin/notifications`
- `/api/admin/notifications/send`

## 10. 이메일과 발송 이력

### 직접 구현·개선

- 회원가입 이메일 인증과 비밀번호 재설정 이메일 연동
- 발송 이력 테이블과 저장 Service
- 인증 메일 템플릿 개선
- 이메일 전송 성공·실패가 인증 흐름에 미치는 영향 검증
- 관리자 메일·알림 화면의 목록과 상태 표시 개선

### 기여 범위 주의

시간별 매칭 이메일 묶음 발송과 전체 운영 메일 시스템은 팀 기능입니다. 본인은 가입·인증·비밀번호 재설정 메일과 발송 이력, 일부 관리자 UI 개선을 중심으로 설명합니다.

## 11. FAQ RAG 챗봇

### 직접 구현

- FastAPI 기반 FAQ RAG 챗봇 서비스
- 승인 FAQ와 검토대기 FAQ 데이터 분리
- 역할별 접근 가능한 FAQ 검색
- BGE-M3 임베딩 기반 FAQ 검색
- 낮은 유사도·서비스 외 질문·짧고 모호한 질문의 안전 응답
- 단일 의도와 복합 의도 질문 분기
- 자주 발생한 오타와 영문 표현 정규화
- LLM 정상 응답 검증 및 승인 FAQ fallback
- 1차·보조 LLM 순차 fallback
- 챗봇 요청·응답 로그 저장
- 이메일, 전화번호, 사업자번호, 주민번호, 계좌번호, 비밀번호 등 민감정보 마스킹
- LangSmith 실행 추적과 추적 데이터 마스킹
- Backend 챗봇 중계 API와 사용자 상담 UI

### 데이터·검증 근거

- 승인 FAQ 데이터 최소 49건 검증
- 검색 평가 케이스 최소 68건 검증
- 권한·출처·검증일 메타데이터 확인
- AI 테스트에 챗봇 fallback, 다중 의도, 오타, 민감정보 마스킹 포함

### 주요 API

- AI 서버 챗봇 API
- Backend `/api/support/chat`

## 12. 자가 자격 진단

### 직접 구현

- 기업회원 상태, 입찰 마감, 지역, 면허를 비교하는 규칙 기반 기본 진단
- 준비도 점수와 충족·미충족·확인 필요 상태 계산
- 공고 첨부문서 다운로드 및 PDF·HWPX·DOCX·TXT 텍스트 추출
- 문서 청크화와 BGE-M3 임베딩 검색
- Qwen을 이용한 근거 ID·자격조건 유형 분류
- LLM 응답을 허용 ID와 유형으로 제한하고 비정상 응답 폐기
- 구조화 조건과 문서 근거의 지역·면허 충돌 재판정
- 면허 OR 조건과 ‘모두 등록’ 조건 구분
- 실적·인력·공동수급·인증·제출서류·사업자 상태의 원문 근거 제공
- 미지원 형식·파일 손상·용량 초과의 개별 실패 사유 제공
- 근거 문서 다운로드 링크
- 분석 요청의 비동기 상태 저장, 중복 요청 방지, 최대 재시도
- 문서 텍스트·청크·진단 결과 캐시
- 마감 공고의 파생 문서 데이터 정리 스케줄러
- LLM 실패 시 규칙 기반 기본 진단 유지
- 사용자 화면의 원형 준비도, 판정 카드, 분석 중 상태, 제외 파일 안내

### 주요 설정

- 파일 최대 크기: 20MB
- 문서 청크: 900자, 중첩 120자
- 첨부파일별 우선 청크: 최대 3개
- 유형별 검색 Top-K: 3개
- LLM 전달 근거: 최대 4개, 1,600자
- 문서 LLM 제한시간: 180초
- 분석 최대 시도: 4회
- 파생 문서 데이터 보관: 마감 후 3일

### 주요 API 및 DB

- `/api/user/bid-notices/{noticeId}/eligibility-diagnosis`
- `bid_notice_document_texts`
- `bid_notice_document_chunks`
- `bid_notice_document_diagnoses`
- Flyway V45, V46

## 13. 관리자 화면 기여

### 연동·개선

- 회원 관리 화면 정보 표시 개선
- 고객센터 문의·공지·FAQ 관리 화면 개선
- 메일·알림 목록 및 발송 상태 표시 개선
- FAQ 삭제와 답변 서식 기능
- 관리자 API URL 환경변수와 개발 프록시 설정

관리자 대시보드와 관리자 전체 운영 시스템의 주 구현자는 별도 팀원이므로 위 범위만 개인 기여로 사용합니다.

## 14. 데이터베이스와 Flyway

### 직접 추가·개선한 주요 영역

- 면허 카탈로그와 초기화 마이그레이션
- 자사 실적 사용자 관리 정책
- 비밀번호 변경 시각과 휴면 상태
- 레거시 컬럼 호환과 중복 컬럼 복구
- 이메일 발송 이력
- 관심조건 매칭 진행 상태
- 사업자번호 제약 조정
- 사용자 보유 면허와 상태 이력
- 챗봇 로그 명칭 정리와 OCR 로그
- 알림 상세 항목
- 자가 자격 진단 문서 텍스트·청크·결과·비동기 상태

### 트러블슈팅

- 팀 병렬 작업으로 발생한 Flyway V24 중복을 V31로 이동
- 면허 마이그레이션 V32 충돌을 V33으로 이동
- 기존 개발 DB 컬럼과 Entity 간 불일치를 보정하는 V8·V9 추가
- 이미 적용된 마이그레이션을 임의 수정하지 않고 후속 버전으로 보정

## 15. API 검증과 Bruno

- 인증·세션·기업 가입·국세청 검증 요청
- 기업 프로필·면허·실적 요청
- 관심조건 CRUD 요청
- 비회원·회원 고객센터 요청
- 공지사항 조회 요청
- OCR 중계 요청
- 챗봇 Backend·AI 요청
- 자가 자격 진단 요청
- 알림 목록·상세·읽음·SSE 요청
- 관리자 고객센터·알림·FAQ 삭제 요청

본인 비병합 Bruno 커밋 28건, 저장소 내 중복 제거 변경 파일 62개가 확인됐습니다.

## 16. 테스트 및 현재 상태

### 확인된 테스트 영역

- 회원가입·이메일 인증·사업자 진위 확인
- 비밀번호 재설정·변경·탈퇴
- 기업 프로필과 사용자 면허 상태 전이
- 자사 실적 날짜 검증
- 고객센터 문의·공지·관리자 작업
- 알림과 관리자 발송
- 관심조건 관리
- 규칙 기반 자격 판정과 문서 근거 병합
- 챗봇 검색·fallback·민감정보 마스킹·LangSmith
- 문서 추출·근거 필터·Qwen 응답 파싱·캐시·재시도

### 2026-08-07 실행 결과

- Backend Gradle 테스트 성공
- User Frontend production build 성공
- Admin Frontend production build 성공
- AI pytest 242건 성공, 경고 1건

## 17. 팀 전체 기능과 개인 기여를 구분할 항목

다음은 프로젝트 전체의 중요한 기능이지만 본인 단독 구현으로 표현하지 않습니다.

- 나라장터 신규·변경 공고 전체 수집 파이프라인
- BGE-M3 기반 전체 공고 매칭 알고리즘과 재학습
- 자연어 공고 검색과 BGE-Reranker 핵심 구현
- 공고 AI 요약 핵심 구현
- PaddleOCR·EasyOCR 엔진과 이미지 전처리 핵심 구현
- Jenkins·Docker Compose·Nginx 기반 CI/CD 및 운영 인프라 구축
- 관리자 대시보드 전체 구현

개인 기여를 설명할 때는 해당 기능과 연결된 API, UI, 데이터, 검증 또는 운영 개선 범위를 정확히 말합니다.
