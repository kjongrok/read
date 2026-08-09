import bidmatchImage from '../assets/projects/bidmatch-ai-solution.png'
import bidmatchArchitecture from '../assets/projects/bidmatch-architecture.png'
import flaskDashboard from '../assets/projects/flask-bidmatch-dashboard.png'
import flaskPreview from '../assets/projects/bidmatch-flask-preview.mp4'
import flightMatrix from '../assets/projects/flight-confusion-matrix.png'

export const profile = {
  name: '김종록',
  role: 'Backend & AI Application Developer',
  summary: '사용자의 실제 업무 흐름을 이해하고, 백엔드의 안정성과 AI의 활용 가능성을 하나의 서비스로 연결합니다.',
  github: 'https://github.com/kjongrok',
}

export const impactMetrics = [
  { value: '5', label: '완성 프로젝트' },
  { value: '118', label: 'BidMatch 기여 커밋' },
  { value: '242', label: 'AI 자동 테스트 통과' },
  { value: 'PL', label: '5인 팀 프로젝트 리딩' },
]

export const skillGroups = [
  {
    label: 'Backend',
    skills: ['Java 17', 'Spring Boot', 'Spring Security', 'JPA', 'Flyway', 'Flask', 'FastAPI'],
  },
  {
    label: 'AI · Data',
    skills: ['BGE-M3', 'RAG', 'LLM', 'XGBoost', 'YOLOv8', 'LSTM', 'PostgreSQL', 'pgvector'],
  },
  {
    label: 'Frontend · Ops',
    skills: ['React', 'Vite', 'Streamlit', 'Redis', 'Docker', 'Bruno', 'GitHub'],
  },
]

export const projects = [
  {
    id: 'bidmatch-final',
    index: '01',
    featured: true,
    title: 'BidMatch',
    subtitle: 'AI 기반 공공입찰 맞춤 추천·자격진단 서비스',
    period: '2026.07.15 — 2026.08.05',
    role: 'Project Leader · Backend & AI Application',
    image: bidmatchImage,
    secondaryImage: bidmatchArchitecture,
    visual: 'image',
    tone: 'green',
    description: '나라장터 공고와 기업정보를 연결해 맞춤 추천, 근거 기반 자격진단, 알림과 고객센터를 제공하는 5인 팀 프로젝트입니다.',
    contributions: [
      '회원·기업 인증, 기업정보·면허·실적 관리 API와 React 화면 구현',
      'FAQ RAG 챗봇의 권한 필터, LLM fallback, 민감정보 마스킹 적용',
      'BGE-M3 검색·LLM 분류·Spring 규칙 판정을 결합한 첨부문서 자격진단 구현',
      'REST 이력과 SSE를 결합한 사용자 실시간 알림 흐름 구현',
    ],
    challenge: '병렬 개발 중 발생한 Flyway 버전 충돌과 기존 DB 스키마 불일치를 적용 이력을 보존하는 후속 마이그레이션 방식으로 해결했습니다.',
    outcome: 'Backend 테스트, 사용자·관리자 프론트 빌드, AI pytest 242건을 최종 검증했습니다.',
    tags: ['Spring Boot', 'FastAPI', 'React', 'PostgreSQL', 'Redis', 'BGE-M3', 'RAG'],
    links: [
      { label: 'Backend', url: 'https://github.com/aiHuman1Team/back-end' },
      { label: 'AI', url: 'https://github.com/aiHuman1Team/ai' },
      { label: 'Frontend', url: 'https://github.com/aiHuman1Team/front-end' },
    ],
  },
  {
    id: 'traffic-agent',
    index: '02',
    title: 'Intelligent Traffic Agent',
    subtitle: 'Vision-to-Text 지능형 고속도로 관제',
    period: '2026.07.04 — 2026.07.07',
    role: 'AI Application Developer',
    visual: 'traffic',
    tone: 'blue',
    description: '실시간 CCTV 분석 결과와 과거 교통 데이터를 LLM이 직접 조회하고 자연어로 브리핑하는 관제 에이전트입니다.',
    contributions: [
      'YOLOv8 차량 탐지와 Centroid Tracking, 정차 차량 제외·ROI 계수 구현',
      'Supabase 교통 로그를 조회하는 LLM Function Calling 흐름 구현',
      'Groq Llama와 Ollama 대체 경로, 대화 문맥 유지 로직 구성',
      '관제 일지 생성 결과를 Word 문서로 변환해 다운로드 제공',
    ],
    challenge: '경량 LLM의 도구 호출 오류와 날짜 환각을 정규식 시간 파서, DB 결과 검증, 대형 모델 기본값으로 완화했습니다.',
    outcome: '영상 인식부터 DB 조회, 자연어 설명, 보고서 생성까지 이어지는 데이터 기반 AI 에이전트 흐름을 완성했습니다.',
    tags: ['YOLOv8', 'LSTM', 'Llama 3', 'Function Calling', 'Supabase', 'Streamlit'],
    links: [{ label: 'GitHub', url: 'https://github.com/kjongrok/LLM' }],
  },
  {
    id: 'traffic-anomaly',
    index: '03',
    title: 'Traffic Anomaly Detection',
    subtitle: 'CCTV 교통량 이상탐지·예측 대시보드',
    period: '2026.06.21 — 2026.07.01',
    role: 'Deep Learning Developer',
    visual: 'vision',
    tone: 'violet',
    description: '실시간 CCTV 영상에서 차량을 탐지하고 교통 특징을 분석해 이상 상태와 다음 시점 밀집도를 표시하는 프로젝트입니다.',
    contributions: [
      'YOLOv8 Nano·Small·Medium 속도와 탐지 결과 비교',
      'K-Means, MLP, LSTM Autoencoder 이상탐지 실험과 임계값 탐색',
      'ITS 실시간 CCTV와 저장 모델을 연결한 Streamlit 대시보드 구현',
      'Supabase 비동기 로그 적재와 영상 실패 복구 흐름 적용',
    ],
    challenge: 'LSTM 입력 차원 불일치와 영상 렌더링 지연을 입력 reshape, 프레임 스킵, 표시 영상 리사이징으로 해결했습니다.',
    outcome: '객체 탐지, 이상탐지, 시계열 예측, 클라우드 로그를 하나의 실행 화면으로 연결했습니다.',
    tags: ['TensorFlow', 'YOLOv8', 'LSTM Autoencoder', 'OpenCV', 'Supabase'],
    links: [{ label: 'GitHub', url: 'https://github.com/kjongrok/Deep_Learning' }],
  },
  {
    id: 'flight-delay',
    index: '04',
    title: 'Flight Delay Prediction',
    subtitle: '항공편 지연 예측 머신러닝',
    period: '2026.06.21 — 2026.06.24',
    role: 'Machine Learning Developer',
    image: flightMatrix,
    visual: 'image-contain',
    tone: 'orange',
    description: 'DACON 항공 운항 데이터를 활용해 지연 가능성을 예측하고 결과와 주요 영향 요인을 보여주는 Streamlit 프로젝트입니다.',
    contributions: [
      '약 25만 건의 라벨 데이터 전처리와 시간 파생변수 생성',
      'Logistic Regression, Random Forest, XGBoost 성능 비교',
      '불균형 데이터의 지연 탐지율을 높이기 위한 가중치 튜닝',
      '전처리와 모델을 단일 Pipeline으로 패키징해 웹앱에 연결',
    ],
    challenge: '높은 정확도와 낮은 지연 재현율이 함께 나타나는 Accuracy Paradox를 확인하고 Recall 중심으로 평가 기준을 전환했습니다.',
    outcome: '프로젝트 보고서 기준 지연 Recall 65%, ROC-AUC 0.785를 기록했습니다.',
    tags: ['XGBoost', 'Scikit-learn', 'Pandas', 'Streamlit', 'Feature Importance'],
    links: [{ label: 'GitHub', url: 'https://github.com/kjongrok/Machine_Learning' }],
  },
  {
    id: 'bidmatch-flask',
    index: '05',
    title: 'BidMatch — Flask Prototype',
    subtitle: '나라장터 맞춤 공고 자동 수집·메일 알림',
    period: '2026.06.14 — 2026.06.20',
    role: 'Project Leader · Full-stack Developer',
    image: flaskDashboard,
    video: flaskPreview,
    visual: 'image',
    tone: 'cyan',
    description: '나라장터 공고 수집부터 조건 매칭, 이메일 다이제스트와 AI 요약까지 연결한 BidMatch의 1차 프로토타입입니다.',
    contributions: [
      'Google·Kakao OAuth와 JWT 인증 흐름 구현',
      'Gmail SMTP 기반 이메일 알림과 비밀번호 재설정 연결',
      'Gemini API 기반 공고 3줄 요약과 모델 오류 대응',
      'Cloudtype 배포 환경의 DB·스케줄러·CORS 문제 해결',
    ],
    challenge: '스케줄러의 UTC/KST 차이로 메일이 다른 시각에 발송되는 문제를 Asia/Seoul 시간대 설정으로 해결했습니다.',
    outcome: '초기 풀스택 프로토타입 경험을 최종 Spring·FastAPI BidMatch의 서비스 구조로 확장했습니다.',
    tags: ['Flask', 'React', 'MariaDB', 'JWT', 'Gemini', 'APScheduler'],
    links: [
      { label: 'GitHub', url: 'https://github.com/kjongrok/BidMatch' },
      { label: 'Demo', url: 'https://youtu.be/Omh36JkK0x0' },
    ],
  },
]

export const journey = [
  { phase: '01', title: '서비스의 시작', text: 'Flask·React로 인증, 외부 API, 배치와 이메일을 연결하며 웹 서비스의 전체 흐름을 경험했습니다.' },
  { phase: '02', title: '데이터로 판단하기', text: '정형데이터 머신러닝과 영상·시계열 딥러닝을 거치며 데이터 전처리와 평가 기준의 중요성을 배웠습니다.' },
  { phase: '03', title: 'AI를 서비스로 연결하기', text: 'LLM 도구 호출과 RAG를 적용하고, 최종 BidMatch에서 Spring·FastAPI·DB 경계를 갖춘 서비스로 발전시켰습니다.' },
]
