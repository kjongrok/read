from io import BytesIO
from pathlib import Path

from pypdf import PdfReader, PdfWriter
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfgen import canvas


ROOT = Path(__file__).resolve().parents[1]
PDF_PATH = ROOT / "output" / "김종록_백엔드_AI응용개발자_이력서.pdf"
TEMP_PATH = PDF_PATH.with_name(f"{PDF_PATH.stem}_temp.pdf")

NAVY = "#13283F"
TEAL = "#159A9C"
GRAY = "#5C6670"
LIGHT_GRAY = "#D9E0E6"


def register_fonts():
    """PDF에 한글을 표시하기 위한 맑은 고딕 글꼴을 등록합니다.

    Returns:
        반환값은 없습니다.

    Side effects:
        ReportLab 전역 글꼴 레지스트리에 일반·굵은 글꼴을 추가합니다.

    Raises:
        Windows 글꼴 파일을 찾을 수 없으면 파일 시스템 예외가 발생합니다.
    """
    pdfmetrics.registerFont(TTFont("Malgun", r"C:\Windows\Fonts\malgun.ttf"))
    pdfmetrics.registerFont(TTFont("MalgunBold", r"C:\Windows\Fonts\malgunbd.ttf"))


def draw_entry_heading(pdf_canvas, title, meta, y_position):
    """프로젝트 제목과 기간·역할을 기존 이력서 형식으로 한 줄에 그립니다.

    Args:
        pdf_canvas: 내용을 그릴 ReportLab 캔버스입니다.
        title: 굵게 표시할 프로젝트 제목입니다.
        meta: 기간과 역할 등 보조 정보입니다.
        y_position: 문장을 배치할 PDF 세로 좌표입니다.

    Returns:
        반환값은 없습니다.

    Side effects:
        전달받은 PDF 캔버스에 제목과 보조 정보를 추가합니다.
    """
    pdf_canvas.setFont("MalgunBold", 9.75)
    pdf_canvas.setFillColor(NAVY)
    pdf_canvas.drawString(44.3, y_position, title)
    title_width = pdfmetrics.stringWidth(title, "MalgunBold", 9.75)
    pdf_canvas.setFont("Malgun", 8.4)
    pdf_canvas.setFillColor(GRAY)
    pdf_canvas.drawString(44.3 + title_width + 7, y_position + 0.4, f"|  {meta}")


def draw_body_line(pdf_canvas, text, y_position, color=NAVY, size=8.4):
    """프로젝트 설명이나 기술 정보를 지정한 위치에 한 줄로 그립니다.

    Args:
        pdf_canvas: 내용을 그릴 ReportLab 캔버스입니다.
        text: 표시할 본문 문자열입니다.
        y_position: 문장을 배치할 PDF 세로 좌표입니다.
        color: 본문 글자 색상입니다.
        size: 본문 글자 크기입니다.

    Returns:
        반환값은 없습니다.

    Side effects:
        전달받은 PDF 캔버스에 본문 문장을 추가합니다.
    """
    pdf_canvas.setFont("Malgun", size)
    pdf_canvas.setFillColor(color)
    pdf_canvas.drawString(48.5, y_position, text)


def draw_wrapped_text(pdf_canvas, text, y_position, bullet=False, color=NAVY, size=8.15, line_height=12):
    """본문을 페이지 폭에 맞춰 줄바꿈하고 다음 내용을 시작할 세로 좌표를 계산합니다.

    Args:
        pdf_canvas: 내용을 그릴 ReportLab 캔버스입니다.
        text: 표시할 본문 문자열입니다.
        y_position: 첫 줄을 배치할 PDF 세로 좌표입니다.
        bullet: 첫 줄 앞에 글머리표를 표시할지 여부입니다.
        color: 본문 글자 색상입니다.
        size: 본문 글자 크기입니다.
        line_height: 줄 사이의 세로 간격입니다.

    Returns:
        작성된 문단 아래에서 다음 내용을 시작할 세로 좌표를 반환합니다.

    Side effects:
        전달받은 PDF 캔버스에 줄바꿈된 본문을 추가합니다.
    """
    words = text.split()
    lines = []
    current_line = ""
    max_width = 493
    for word in words:
        candidate = f"{current_line} {word}".strip()
        if current_line and pdfmetrics.stringWidth(candidate, "Malgun", size) > max_width:
            lines.append(current_line)
            current_line = word
        else:
            current_line = candidate
    if current_line:
        lines.append(current_line)

    pdf_canvas.setFont("Malgun", size)
    pdf_canvas.setFillColor(color)
    for index, line in enumerate(lines):
        x_position = 48.5
        if bullet and index == 0:
            pdf_canvas.drawString(48.5, y_position, "•")
            x_position = 57
        elif bullet:
            x_position = 57
        pdf_canvas.drawString(x_position, y_position, line)
        y_position -= line_height
    return y_position


def draw_section_title(pdf_canvas, title, y_position, page_width):
    """이력서 섹션 제목과 하단 구분선을 지정한 위치에 그립니다.

    Args:
        pdf_canvas: 내용을 그릴 ReportLab 캔버스입니다.
        title: 표시할 섹션 제목입니다.
        y_position: 제목을 배치할 PDF 세로 좌표입니다.
        page_width: 구분선 길이를 계산할 페이지 너비입니다.

    Returns:
        반환값은 없습니다.

    Side effects:
        전달받은 PDF 캔버스에 제목과 구분선을 추가합니다.
    """
    pdf_canvas.setFont("MalgunBold", 11.25)
    pdf_canvas.setFillColor(NAVY)
    pdf_canvas.drawString(44.3, y_position, title)
    pdf_canvas.setStrokeColor(LIGHT_GRAY)
    pdf_canvas.setLineWidth(0.7)
    pdf_canvas.line(44.3, y_position - 9, page_width - 44.3, y_position - 9)


def build_clean_first_page(page_width, page_height):
    """수정된 역량·경력 문장을 포함한 이력서 첫 번째 페이지 전체를 생성합니다.

    Args:
        page_width: 원본 PDF 페이지 너비입니다.
        page_height: 원본 PDF 페이지 높이입니다.

    Returns:
        새 첫 번째 페이지 PDF를 담은 메모리 버퍼를 반환합니다.

    Side effects:
        메모리 버퍼에 프로필, 역량, 기술, 경력, 교육 내용을 기록합니다.
    """
    buffer = BytesIO()
    pdf_canvas = canvas.Canvas(buffer, pagesize=(page_width, page_height))

    pdf_canvas.setFont("MalgunBold", 25)
    pdf_canvas.setFillColor(NAVY)
    pdf_canvas.drawString(44.3, 786, "김종록")
    pdf_canvas.setFont("MalgunBold", 10.5)
    pdf_canvas.setFillColor(TEAL)
    pdf_canvas.drawString(44.3, 748, "BACKEND & AI APPLICATION DEVELOPER")
    pdf_canvas.setFont("Malgun", 8.7)
    pdf_canvas.setFillColor(GRAY)
    phone_text = "010-7742-1623"
    separator = "  |  "
    email_text = "xhxhahs2@gmail.com"
    location_text = "경기 하남시"
    contact_text = f"{phone_text}{separator}{email_text}{separator}{location_text}"
    pdf_canvas.drawString(44.3, 723, contact_text)
    phone_width = pdfmetrics.stringWidth(phone_text, "Malgun", 8.7)
    separator_width = pdfmetrics.stringWidth(separator, "Malgun", 8.7)
    email_width = pdfmetrics.stringWidth(email_text, "Malgun", 8.7)
    email_x = 44.3 + phone_width + separator_width
    pdf_canvas.linkURL("tel:+821077421623", (44.3, 720, 44.3 + phone_width, 732), relative=0, thickness=0)
    pdf_canvas.linkURL("mailto:xhxhahs2@gmail.com", (email_x, 720, email_x + email_width, 732), relative=0, thickness=0)
    pdf_canvas.setStrokeColor(TEAL)
    pdf_canvas.setLineWidth(2)
    pdf_canvas.line(44.3, 706, page_width - 44.3, 706)

    draw_section_title(pdf_canvas, "PROFILE", 684, page_width)
    profile_paragraphs = [
        "병원 전산 운영 3년 11개월 동안 여러 진료·행정부서의 장애에 대응하고 사용자 요청을 처리하며, 문제를 업무 흐름과 시스템 구조의 관점에서 파악하는 경험을 쌓았습니다.",
        "이후 Spring Boot 기반 Backend와 React 화면을 구현하고, 머신러닝·딥러닝 모델 개발과 LLM 에이전트·RAG 챗봇 구현을 경험했습니다. 5인 팀 PL로 참여한 BidMatch에서는 AI 기능을 Backend 규칙과 검증·대체 처리로 보완하고 AI 자동화 테스트 242건을 통과했습니다.",
        "운영 환경에 대한 이해를 바탕으로 AI 기능을 안정적인 Backend 서비스에 연결하고, 예외 상황에서도 사용자가 신뢰할 수 있는 결과를 제공하는 개발자로 성장하고 있습니다.",
    ]
    y_position = 656
    for profile_text in profile_paragraphs:
        y_position = draw_wrapped_text(pdf_canvas, profile_text, y_position, size=8.75, line_height=14)
        y_position -= 3

    link_items = [
        ("Portfolio", "https://kjongrok.github.io/"),
        ("GitHub", "https://github.com/kjongrok"),
        ("BidMatch Project", "https://github.com/aiHuman1Team"),
        ("BidMatch Service", "http://minsworkspace.ddns.net"),
    ]
    link_y = y_position - 1
    link_x = 44.3
    for index, (label, url) in enumerate(link_items):
        if index:
            separator = "  |  "
            pdf_canvas.setFont("Malgun", 8.7)
            pdf_canvas.setFillColor(GRAY)
            pdf_canvas.drawString(link_x, link_y, separator)
            link_x += pdfmetrics.stringWidth(separator, "Malgun", 8.7)
        pdf_canvas.setFont("MalgunBold", 8.7)
        pdf_canvas.setFillColor(TEAL)
        pdf_canvas.drawString(link_x, link_y, label)
        label_width = pdfmetrics.stringWidth(label, "MalgunBold", 8.7)
        pdf_canvas.linkURL(url, (link_x, link_y - 3, link_x + label_width, link_y + 9), relative=0, thickness=0)
        link_x += label_width

    core_title_y = link_y - 19
    draw_section_title(pdf_canvas, "CORE COMPETENCIES", core_title_y, page_width)
    competencies = [
        "Spring Boot 기반 인증·회원·기업정보·고객센터·알림 API와 React 사용자 흐름 구현",
        "정형 데이터 ML, 영상·시계열 DL 모델 개발과 LLM 에이전트·RAG 챗봇 구현",
        "BGE-M3 검색·Qwen 분류와 Spring 규칙 판정을 분리하고 검증·fallback 적용",
        "5인 팀 프로젝트 리더(PL)로 API 계약, 기능 범위, 테스트와 시연 자료를 조율",
    ]
    y_position = core_title_y - 27
    for competency in competencies:
        y_position = draw_wrapped_text(pdf_canvas, competency, y_position, bullet=True, size=8.45, line_height=14)

    skills_title_y = y_position - 4
    draw_section_title(pdf_canvas, "TECHNICAL SKILLS", skills_title_y, page_width)
    skill_rows = [
        ("Backend", "Java 17 · Spring Boot 3.5 · Spring Security · Spring Data JPA · MyBatis · SSE"),
        ("AI · ML/DL", "Python · FastAPI · scikit-learn · TensorFlow/Keras · PyTorch · YOLOv8 · RAG · BGE-M3 · Qwen/Ollama"),
        ("Frontend", "React 18 · Vite 5 · React Router · Axios · Streamlit"),
        ("Data · Infra", "PostgreSQL · pgvector · Redis · MariaDB · Supabase · Docker(실행·검증)"),
        ("Test · Collaboration", "JUnit 5 · pytest · Bruno · Git/GitHub · GitHub Actions · Jira · Slack"),
    ]
    row_top = skills_title_y - 22
    for label, skills in skill_rows:
        pdf_canvas.setFillColor("#EAF6F5")
        pdf_canvas.rect(51, row_top - 21, 86, 23, fill=1, stroke=0)
        pdf_canvas.setStrokeColor(LIGHT_GRAY)
        pdf_canvas.setLineWidth(0.5)
        pdf_canvas.line(51, row_top - 21, page_width - 52, row_top - 21)
        pdf_canvas.setFont("MalgunBold", 8.2)
        pdf_canvas.setFillColor(TEAL)
        pdf_canvas.drawString(57, row_top - 13, label)
        pdf_canvas.setFont("Malgun", 7.65)
        pdf_canvas.setFillColor(NAVY)
        pdf_canvas.drawString(142, row_top - 13, skills)
        row_top -= 23

    work_title_y = row_top - 9
    draw_section_title(pdf_canvas, "WORK EXPERIENCE", work_title_y, page_width)
    draw_entry_heading(pdf_canvas, "㈜시스게이트 · 한림대학교의료원(강동) 전산 운영", "2019.08 – 2023.06 · OA 운영 및 사용자 지원", work_title_y - 27)
    y_position = work_title_y - 52
    pdf_canvas.setFont("MalgunBold", 8.1)
    pdf_canvas.setFillColor(TEAL)
    pdf_canvas.drawString(48.5, y_position, "담당 업무")
    y_position -= 15
    for experience in [
        "병원 내 여러 진료·행정부서의 OA 요구사항 수집, 시스템 구성 검토와 도입 지원",
        "장애·사용자 요청 대응, 신규 시스템 교육 자료 제작과 사용자 교육 진행",
    ]:
        y_position = draw_wrapped_text(pdf_canvas, experience, y_position, bullet=True, size=8.15, line_height=13)
    y_position -= 1
    pdf_canvas.setFont("MalgunBold", 8.1)
    pdf_canvas.setFillColor(TEAL)
    pdf_canvas.drawString(48.5, y_position, "경험 및 직무 연결점")
    y_position -= 15
    for experience in [
        "반복 문의를 운영 매뉴얼·정책·Q&A 대응 체계로 정리하고 원격 OA 전환 지원",
        "사용자 업무와 영향 범위를 고려해 원인을 좁히는 경험을 개발의 예외 처리·운영 관점으로 확장",
    ]:
        y_position = draw_wrapped_text(pdf_canvas, experience, y_position, bullet=True, size=8.15, line_height=13)

    education_title_y = y_position - 4
    draw_section_title(pdf_canvas, "EDUCATION", education_title_y, page_width)
    draw_entry_heading(pdf_canvas, "휴먼AI교육센터 · 심화_인공지능(AI) 서비스 기반 웹 개발자 심화 프로젝트", "2026.06.11 – 2026.08.11", education_title_y - 27)
    draw_entry_heading(pdf_canvas, "KG IT BANK · 핀테크 서비스를 위한 풀스택 개발자 양성 과정", "2024.08.05 – 2025.02.13", education_title_y - 51)
    draw_entry_heading(pdf_canvas, "여주대학교 · 컴퓨터정보과", "2016.03 – 2020.02 · 졸업", education_title_y - 75)

    pdf_canvas.setFont("Malgun", 7.5)
    pdf_canvas.setFillColor(GRAY)
    pdf_canvas.drawRightString(page_width - 44.3, 25, "1")
    pdf_canvas.save()
    buffer.seek(0)
    return buffer


def build_clean_second_page(page_width, page_height):
    """검색 가능한 텍스트만 포함하도록 이력서 두 번째 페이지 전체를 새로 생성합니다.

    Args:
        page_width: 원본 PDF 페이지 너비입니다.
        page_height: 원본 PDF 페이지 높이입니다.

    Returns:
        새 두 번째 페이지 PDF를 담은 메모리 버퍼를 반환합니다.

    Side effects:
        메모리 버퍼에 프로젝트와 포트폴리오 내용을 기록합니다.
    """
    buffer = BytesIO()
    pdf_canvas = canvas.Canvas(buffer, pagesize=(page_width, page_height))

    draw_section_title(pdf_canvas, "AI EDUCATION HIGHLIGHTS", 800, page_width)
    y_position = 773
    for highlight in [
        "scikit-learn 기반 데이터 전처리·모델 비교와 불균형 데이터 평가",
        "YOLOv8·LSTM 기반 객체 탐지, 이상탐지와 시계열 예측 모델 개발",
        "LLM Function Calling·RAG 챗봇과 응답 검증·fallback 구현",
        "Spring Boot·FastAPI·React 기반 Backend·AI·사용자 화면 연동",
    ]:
        y_position = draw_wrapped_text(pdf_canvas, highlight, y_position, bullet=True, size=8.15, line_height=13)

    selected_title_y = y_position - 6
    pdf_canvas.setFont("MalgunBold", 11.25)
    pdf_canvas.setFillColor(NAVY)
    pdf_canvas.drawString(44.3, selected_title_y, "SELECTED PROJECTS")
    pdf_canvas.setStrokeColor(LIGHT_GRAY)
    pdf_canvas.setLineWidth(0.7)
    pdf_canvas.line(44.3, selected_title_y - 9, page_width - 44.3, selected_title_y - 9)

    y_position = selected_title_y - 28
    draw_entry_heading(pdf_canvas, "BidMatch · AI 기반 공공입찰 맞춤 추천·자가 자격 진단 서비스", "2026.07.09 – 2026.08.07 · 5인 팀 PL", y_position)
    y_position = draw_wrapped_text(pdf_canvas, "나라장터 공고와 기업정보를 연결해 맞춤 공고 추천, 근거 기반 자가 자격 진단, 알림과 고객센터를 제공하는 서비스", y_position - 18, color=GRAY)
    bidmatch_bullets = [
        "Java 17·Spring Boot로 일반/기업회원 인증, 기업정보·면허·실적, 고객센터와 SSE 알림 API 구현",
        "React 사용자 화면을 연동하고 Bruno 요청으로 Backend·AI API 계약과 예외 응답 검증",
        "FAQ RAG 챗봇에 역할별 검색, 낮은 유사도 차단, 다중 의도, LLM fallback과 민감정보 마스킹 적용",
        "BGE-M3 근거 검색과 Qwen 유형 분류 결과를 Spring 규칙 판정으로 재검증하는 자가 자격 진단 구조 설계",
        "병렬 개발 중 DB 마이그레이션(Flyway) 버전·체크섬·스키마 충돌을 기존 이력을 보존한 후속 마이그레이션으로 해결",
        "5개 저장소 118개 비병합 커밋 기여, AI 자동화 테스트 242건, Backend 테스트, 사용자·관리자 Frontend 빌드 통과",
    ]
    for bullet_text in bidmatch_bullets:
        y_position = draw_wrapped_text(pdf_canvas, bullet_text, y_position - 2, bullet=True)
    y_position = draw_wrapped_text(pdf_canvas, "기술: Spring Boot · FastAPI · React · PostgreSQL · Redis · BGE-M3 · Qwen/Ollama · RAG · PyMuPDF · Docker(실행·검증)", y_position - 2, color=TEAL, size=8.0)

    projects = [
        (
            "지능형 교통 관제 시스템",
            "2026.07.02 – 2026.07.07 · 개인",
            [
                "YOLOv8 차량 탐지 결과와 Supabase 로그 조회를 LLM Function Calling으로 연결",
                "날짜 환각과 도구 호출 오류를 시간 파서·DB 결과 검증·대체 모델 경로로 완화하고 Word 관제 일지 생성",
            ],
            "기술: Python · YOLOv8 · Supabase · LLM Function Calling · Streamlit · python-docx",
        ),
        (
            "CCTV 교통량 이상탐지·예측",
            "2026.06.25 – 2026.07.01 · 개인",
            [
                "YOLOv8 탐지, LSTM Autoencoder 이상탐지, ITS CCTV, Supabase 로그를 Streamlit 화면으로 통합",
                "입력 차원 불일치와 영상 지연을 reshape, 프레임 스킵, 표시 영상 리사이징으로 해결",
            ],
            "기술: Python · YOLOv8 · TensorFlow/Keras · LSTM Autoencoder · Supabase · Streamlit",
        ),
        (
            "항공편 지연 예측",
            "2026.06.18 – 2026.06.24 · 개인",
            [
                "약 25만 건 데이터를 전처리하고 XGBoost 등 모델을 비교해 불균형 데이터의 지연 Recall 중심으로 평가",
                "전처리·모델을 scikit-learn Pipeline으로 패키징해 Streamlit에 연결, 프로젝트 보고서 기준 Recall 65%·ROC-AUC 0.785 기록",
            ],
            "기술: Python · pandas · scikit-learn · XGBoost · Pipeline · Streamlit",
        ),
        (
            "맞춤 공고 자동 수집·메일 알림 프로토타입",
            "2026.06.11 – 2026.06.17 · 팀 PL",
            [
                "Flask·React로 OAuth/JWT 인증, Gmail 알림, Gemini 공고 요약, APScheduler 배치를 연결",
                "UTC/KST 발송 시간 차이를 Asia/Seoul 기준으로 보정하고 최종 Spring·FastAPI 프로젝트로 구조 확장",
            ],
            "기술: Flask · React · OAuth/JWT · Gmail SMTP · Gemini · APScheduler",
        ),
        (
            "Spike · Spring Boot 기반 금융 서비스",
            "2025.01 – 2025.02 · 팀 프로젝트",
            [
                "Spring Security와 BCrypt를 적용한 회원가입·로그인, 역할별 접근 제어와 마이페이지 구현",
                "관리자 사용자 CRUD·페이징과 보이스피싱 의심 계좌 신고·검토·상태 변경 흐름 구현",
            ],
            "기술: Java 17 · Spring Boot 2.7 · JSP · JPA · MyBatis · Oracle DB",
        ),
    ]
    for title, meta, bullets, technology in projects:
        y_position -= 7
        draw_entry_heading(pdf_canvas, title, meta, y_position)
        y_position -= 17
        for bullet_text in bullets:
            y_position = draw_wrapped_text(pdf_canvas, bullet_text, y_position, bullet=True)
        if technology:
            y_position = draw_wrapped_text(pdf_canvas, technology, y_position - 1, color=TEAL, size=8.0)

    pdf_canvas.setFont("Malgun", 7.5)
    pdf_canvas.setFillColor(GRAY)
    pdf_canvas.drawRightString(page_width - 44.3, 25, "2")
    pdf_canvas.save()
    buffer.seek(0)
    return buffer


def update_pdf():
    """기존 2페이지 PDF에 수정 내용을 병합하고 결과 파일을 안전하게 교체합니다.

    Returns:
        수정된 PDF 파일 경로를 반환합니다.

    Side effects:
        기존 PDF를 임시 파일을 거쳐 수정된 내용으로 덮어씁니다.

    Raises:
        원본 PDF가 없거나 읽기·쓰기·교체에 실패하면 관련 예외가 발생합니다.
    """
    register_fonts()
    reader = PdfReader(PDF_PATH)
    page = reader.pages[1]
    page_width = float(page.mediabox.width)
    page_height = float(page.mediabox.height)
    clean_first_page = PdfReader(build_clean_first_page(page_width, page_height)).pages[0]
    clean_second_page = PdfReader(build_clean_second_page(page_width, page_height)).pages[0]

    writer = PdfWriter()
    writer.add_page(clean_first_page)
    writer.add_page(clean_second_page)
    with TEMP_PATH.open("wb") as output_file:
        writer.write(output_file)
    TEMP_PATH.replace(PDF_PATH)
    return PDF_PATH


if __name__ == "__main__":
    print(update_pdf())
