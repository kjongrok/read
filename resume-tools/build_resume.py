from pathlib import Path

from docx import Document
from docx.enum.section import WD_SECTION
from docx.enum.table import WD_CELL_VERTICAL_ALIGNMENT, WD_TABLE_ALIGNMENT
from docx.enum.text import WD_ALIGN_PARAGRAPH, WD_BREAK, WD_LINE_SPACING
from docx.oxml import OxmlElement
from docx.oxml.ns import qn
from docx.shared import Cm, Pt, RGBColor


ROOT = Path(__file__).resolve().parents[2]
OUTPUT_DIR = ROOT / "read" / "output"
OUTPUT_PATH = OUTPUT_DIR / "김종록_백엔드_AI응용개발자_이력서.docx"

NAVY = "13283F"
TEAL = "159A9C"
LIGHT_TEAL = "EAF6F5"
GRAY = "5C6670"
LIGHT_GRAY = "D9E0E6"
WHITE = "FFFFFF"


def set_cell_shading(cell, fill):
    """표 셀의 배경색을 지정합니다.

    Args:
        cell: 배경색을 적용할 python-docx 셀입니다.
        fill: 16진수 RGB 색상 문자열입니다.

    Returns:
        반환값은 없습니다.

    Side effects:
        셀 XML에 배경색 속성을 추가합니다.
    """
    tc_pr = cell._tc.get_or_add_tcPr()
    shd = tc_pr.find(qn("w:shd"))
    if shd is None:
        shd = OxmlElement("w:shd")
        tc_pr.append(shd)
    shd.set(qn("w:fill"), fill)


def set_cell_border(cell, **edges):
    """표 셀의 테두리 속성을 방향별로 설정합니다.

    Args:
        cell: 테두리를 적용할 python-docx 셀입니다.
        **edges: top, bottom, left, right 방향별 테두리 설정입니다.

    Returns:
        반환값은 없습니다.

    Side effects:
        셀 XML의 테두리 속성을 변경합니다.
    """
    tc_pr = cell._tc.get_or_add_tcPr()
    tc_borders = tc_pr.first_child_found_in("w:tcBorders")
    if tc_borders is None:
        tc_borders = OxmlElement("w:tcBorders")
        tc_pr.append(tc_borders)
    for edge_name, edge_data in edges.items():
        edge = tc_borders.find(qn(f"w:{edge_name}"))
        if edge is None:
            edge = OxmlElement(f"w:{edge_name}")
            tc_borders.append(edge)
        for key, value in edge_data.items():
            edge.set(qn(f"w:{key}"), str(value))


def set_repeat_table_header(row):
    """표의 첫 행이 다음 페이지에서도 제목 행으로 반복되도록 설정합니다.

    Args:
        row: 반복 대상으로 지정할 python-docx 행입니다.

    Returns:
        반환값은 없습니다.

    Side effects:
        행 XML에 반복 제목 속성을 추가합니다.
    """
    tr_pr = row._tr.get_or_add_trPr()
    tbl_header = OxmlElement("w:tblHeader")
    tbl_header.set(qn("w:val"), "true")
    tr_pr.append(tbl_header)


def set_cell_margins(cell, top=80, start=100, bottom=80, end=100):
    """표 셀 안쪽 여백을 트윕 단위로 설정합니다.

    Args:
        cell: 여백을 적용할 python-docx 셀입니다.
        top: 위쪽 여백입니다.
        start: 시작 방향 여백입니다.
        bottom: 아래쪽 여백입니다.
        end: 끝 방향 여백입니다.

    Returns:
        반환값은 없습니다.

    Side effects:
        셀 XML의 여백 속성을 변경합니다.
    """
    tc = cell._tc
    tc_pr = tc.get_or_add_tcPr()
    tc_mar = tc_pr.first_child_found_in("w:tcMar")
    if tc_mar is None:
        tc_mar = OxmlElement("w:tcMar")
        tc_pr.append(tc_mar)
    for margin_name, margin_value in {
        "top": top,
        "start": start,
        "bottom": bottom,
        "end": end,
    }.items():
        node = tc_mar.find(qn(f"w:{margin_name}"))
        if node is None:
            node = OxmlElement(f"w:{margin_name}")
            tc_mar.append(node)
        node.set(qn("w:w"), str(margin_value))
        node.set(qn("w:type"), "dxa")


def style_run(run, size=9.2, bold=False, color=NAVY, font="맑은 고딕"):
    """문서 전반에서 사용하는 글꼴과 색상을 런에 적용합니다.

    Args:
        run: 서식을 적용할 python-docx 런입니다.
        size: 글자 크기(pt)입니다.
        bold: 굵게 표시할지 여부입니다.
        color: 16진수 RGB 색상 문자열입니다.
        font: 적용할 글꼴 이름입니다.

    Returns:
        서식이 적용된 런을 반환합니다.

    Side effects:
        런의 글꼴, 크기, 굵기, 색상을 변경합니다.
    """
    run.font.name = font
    run._element.rPr.rFonts.set(qn("w:eastAsia"), font)
    run.font.size = Pt(size)
    run.font.bold = bold
    run.font.color.rgb = RGBColor.from_string(color)
    return run


def configure_document(document):
    """A4 이력서에 맞는 여백과 기본 스타일을 설정합니다.

    Args:
        document: 설정할 python-docx 문서입니다.

    Returns:
        반환값은 없습니다.

    Side effects:
        문서 섹션과 Normal 스타일을 변경합니다.
    """
    section = document.sections[0]
    section.page_width = Cm(21)
    section.page_height = Cm(29.7)
    section.top_margin = Cm(1.35)
    section.bottom_margin = Cm(1.25)
    section.left_margin = Cm(1.55)
    section.right_margin = Cm(1.55)
    section.header_distance = Cm(0.5)
    section.footer_distance = Cm(0.5)

    normal = document.styles["Normal"]
    normal.font.name = "맑은 고딕"
    normal._element.rPr.rFonts.set(qn("w:eastAsia"), "맑은 고딕")
    normal.font.size = Pt(9.2)
    normal.font.color.rgb = RGBColor.from_string(NAVY)
    normal.paragraph_format.space_after = Pt(2.4)
    normal.paragraph_format.line_spacing = 1.14


def add_header(document):
    """이름, 목표 직무, 연락처가 포함된 첫 페이지 헤더를 작성합니다.

    Args:
        document: 내용을 추가할 python-docx 문서입니다.

    Returns:
        반환값은 없습니다.

    Side effects:
        문서 첫 부분에 이름과 연락처 문단을 추가합니다.
    """
    name_paragraph = document.add_paragraph()
    name_paragraph.paragraph_format.space_after = Pt(0)
    style_run(name_paragraph.add_run("김종록"), size=25, bold=True, color=NAVY)

    role_paragraph = document.add_paragraph()
    role_paragraph.paragraph_format.space_before = Pt(0)
    role_paragraph.paragraph_format.space_after = Pt(5)
    style_run(role_paragraph.add_run("BACKEND & AI APPLICATION DEVELOPER"), size=10.5, bold=True, color=TEAL)

    contact = document.add_paragraph()
    contact.paragraph_format.space_after = Pt(7)
    contact.paragraph_format.line_spacing = 1.0
    style_run(contact.add_run("010-7742-1623  |  xhxhahs2@gmail.com  |  경기 하남시  |  "), size=8.7, color=GRAY)
    github_run = style_run(contact.add_run("github.com/kjongrok"), size=8.7, bold=True, color=TEAL)
    github_run.hyperlink = None

    rule = document.add_paragraph()
    rule.paragraph_format.space_after = Pt(6)
    p_pr = rule._p.get_or_add_pPr()
    p_bdr = OxmlElement("w:pBdr")
    bottom = OxmlElement("w:bottom")
    bottom.set(qn("w:val"), "single")
    bottom.set(qn("w:sz"), "16")
    bottom.set(qn("w:space"), "1")
    bottom.set(qn("w:color"), TEAL)
    p_bdr.append(bottom)
    p_pr.append(p_bdr)


def add_section_title(document, title):
    """구분선이 포함된 이력서 섹션 제목을 추가합니다.

    Args:
        document: 내용을 추가할 python-docx 문서입니다.
        title: 표시할 섹션 제목입니다.

    Returns:
        생성한 제목 문단을 반환합니다.

    Side effects:
        문서에 새 제목 문단을 추가합니다.
    """
    paragraph = document.add_paragraph()
    paragraph.paragraph_format.space_before = Pt(6)
    paragraph.paragraph_format.space_after = Pt(3.5)
    paragraph.paragraph_format.keep_with_next = True
    style_run(paragraph.add_run(title), size=11.3, bold=True, color=NAVY)
    p_pr = paragraph._p.get_or_add_pPr()
    p_bdr = OxmlElement("w:pBdr")
    bottom = OxmlElement("w:bottom")
    bottom.set(qn("w:val"), "single")
    bottom.set(qn("w:sz"), "7")
    bottom.set(qn("w:space"), "2")
    bottom.set(qn("w:color"), LIGHT_GRAY)
    p_bdr.append(bottom)
    p_pr.append(p_bdr)
    return paragraph


def add_body_paragraph(document, text, bold_prefix=None, color=NAVY, size=9.2, space_after=2.5):
    """일반 본문 문단을 추가하고 선택적으로 앞부분을 강조합니다.

    Args:
        document: 내용을 추가할 python-docx 문서입니다.
        text: 문단 전체 문자열입니다.
        bold_prefix: 굵게 표시할 시작 문자열입니다.
        color: 본문 글자 색상입니다.
        size: 글자 크기(pt)입니다.
        space_after: 문단 뒤 간격(pt)입니다.

    Returns:
        생성한 본문 문단을 반환합니다.

    Side effects:
        문서에 새 본문 문단을 추가합니다.
    """
    paragraph = document.add_paragraph()
    paragraph.paragraph_format.space_after = Pt(space_after)
    paragraph.paragraph_format.line_spacing = 1.13
    if bold_prefix and text.startswith(bold_prefix):
        style_run(paragraph.add_run(bold_prefix), size=size, bold=True, color=color)
        style_run(paragraph.add_run(text[len(bold_prefix):]), size=size, color=color)
    else:
        style_run(paragraph.add_run(text), size=size, color=color)
    return paragraph


def add_bullet(document, text, level=0, size=8.9, color=NAVY, compact=True):
    """성과 중심의 글머리표 문단을 추가합니다.

    Args:
        document: 내용을 추가할 python-docx 문서입니다.
        text: 표시할 글머리표 내용입니다.
        level: 들여쓰기 단계입니다.
        size: 글자 크기(pt)입니다.
        color: 글자 색상입니다.
        compact: 문단 간격을 좁게 유지할지 여부입니다.

    Returns:
        생성한 글머리표 문단을 반환합니다.

    Side effects:
        문서에 새 글머리표 문단을 추가합니다.
    """
    paragraph = document.add_paragraph(style="List Bullet")
    paragraph.paragraph_format.left_indent = Cm(0.45 + 0.35 * level)
    paragraph.paragraph_format.first_line_indent = Cm(-0.22)
    paragraph.paragraph_format.space_after = Pt(1.2 if compact else 2.6)
    paragraph.paragraph_format.line_spacing = 1.08
    paragraph.paragraph_format.keep_together = True
    style_run(paragraph.add_run(text), size=size, color=color)
    return paragraph


def add_skill_table(document):
    """기술을 역할별로 분류한 간결한 표를 추가합니다.

    Args:
        document: 내용을 추가할 python-docx 문서입니다.

    Returns:
        생성한 기술 표를 반환합니다.

    Side effects:
        문서에 2열 기술 분류 표를 추가합니다.
    """
    rows = [
        ("Backend", "Java 17 · Spring Boot 3.5 · Spring Security · Spring Data JPA · Flyway · SSE"),
        ("AI · Data", "Python 3.12 · FastAPI · RAG · BGE-M3 · LLM · PostgreSQL · pgvector · Redis"),
        ("Frontend · Test", "React 18 · Vite · Axios · JUnit 5 · pytest · Bruno · Git/GitHub"),
    ]
    table = document.add_table(rows=len(rows), cols=2)
    table.alignment = WD_TABLE_ALIGNMENT.CENTER
    table.autofit = False
    table.columns[0].width = Cm(3.0)
    table.columns[1].width = Cm(14.4)
    for index, (label, values) in enumerate(rows):
        left, right = table.rows[index].cells
        left.width = Cm(3.0)
        right.width = Cm(14.4)
        left.vertical_alignment = WD_CELL_VERTICAL_ALIGNMENT.CENTER
        right.vertical_alignment = WD_CELL_VERTICAL_ALIGNMENT.CENTER
        set_cell_shading(left, LIGHT_TEAL)
        for cell in (left, right):
            set_cell_margins(cell, top=60, bottom=60, start=100, end=100)
            set_cell_border(
                cell,
                bottom={"val": "single", "sz": "4", "color": LIGHT_GRAY},
            )
        left_p = left.paragraphs[0]
        left_p.paragraph_format.space_after = Pt(0)
        style_run(left_p.add_run(label), size=8.6, bold=True, color=TEAL)
        right_p = right.paragraphs[0]
        right_p.paragraph_format.space_after = Pt(0)
        style_run(right_p.add_run(values), size=8.5, color=NAVY)
    return table


def add_entry_heading(document, title, meta):
    """경력이나 프로젝트의 제목과 기간·역할 정보를 한 줄로 추가합니다.

    Args:
        document: 내용을 추가할 python-docx 문서입니다.
        title: 항목 제목입니다.
        meta: 기간과 역할 등 보조 정보입니다.

    Returns:
        생성한 제목 문단을 반환합니다.

    Side effects:
        문서에 새 항목 제목 문단을 추가합니다.
    """
    paragraph = document.add_paragraph()
    paragraph.paragraph_format.space_before = Pt(3.5)
    paragraph.paragraph_format.space_after = Pt(1.4)
    paragraph.paragraph_format.keep_with_next = True
    style_run(paragraph.add_run(title), size=10.0, bold=True, color=NAVY)
    style_run(paragraph.add_run(f"  |  {meta}"), size=8.4, color=GRAY)
    return paragraph


def add_page_number(section):
    """문서 바닥글 오른쪽에 현재 페이지 번호를 추가합니다.

    Args:
        section: 바닥글을 설정할 문서 섹션입니다.

    Returns:
        반환값은 없습니다.

    Side effects:
        섹션 바닥글에 PAGE 필드를 추가합니다.
    """
    footer = section.footer
    paragraph = footer.paragraphs[0]
    paragraph.alignment = WD_ALIGN_PARAGRAPH.RIGHT
    paragraph.paragraph_format.space_before = Pt(0)
    run = paragraph.add_run()
    begin = OxmlElement("w:fldChar")
    begin.set(qn("w:fldCharType"), "begin")
    instruction = OxmlElement("w:instrText")
    instruction.set(qn("xml:space"), "preserve")
    instruction.text = "PAGE"
    separate = OxmlElement("w:fldChar")
    separate.set(qn("w:fldCharType"), "separate")
    end = OxmlElement("w:fldChar")
    end.set(qn("w:fldCharType"), "end")
    run._r.extend([begin, instruction, separate, end])
    style_run(run, size=7.5, color=GRAY)


def build_resume():
    """검토된 경력과 프로젝트 사실을 바탕으로 2페이지 이력서를 생성합니다.

    Args:
        인자는 없습니다.

    Returns:
        생성된 DOCX 파일 경로를 반환합니다.

    Side effects:
        read/output 폴더에 기존 파일을 덮어써 DOCX 파일을 저장합니다.

    Raises:
        출력 폴더 생성이나 DOCX 저장에 실패하면 파일 시스템 예외가 발생합니다.
    """
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    document = Document()
    configure_document(document)
    add_header(document)

    add_section_title(document, "PROFILE")
    add_body_paragraph(
        document,
        "사용자의 실제 업무 흐름을 이해하고 백엔드의 안정성과 AI의 활용 가능성을 하나의 서비스로 연결하는 개발자입니다. "
        "병원 전산 운영 3년 11개월의 사용자 지원 경험을 바탕으로, Spring Boot API와 React 화면을 구현하고 "
        "FastAPI·RAG·LLM 기능을 서비스 경계 안에서 검증 가능한 형태로 연결했습니다.",
        size=9.25,
        space_after=3.5,
    )

    add_section_title(document, "CORE COMPETENCIES")
    add_bullet(document, "Spring Boot 기반 인증·회원·기업정보·고객센터·알림 API와 React 사용자 흐름 구현")
    add_bullet(document, "FastAPI·BGE-M3·LLM·Spring 규칙 판정을 분리한 근거 기반 RAG 기능 설계")
    add_bullet(document, "Flyway 충돌, 외부 API 장애, 비정상 AI 출력에 대한 검증, fallback과 상태 관리 적용")
    add_bullet(document, "5인 팀 Project Leader로 API 계약, 기능 범위, 테스트와 시연 자료를 조율")

    add_section_title(document, "TECHNICAL SKILLS")
    add_skill_table(document)

    add_section_title(document, "WORK EXPERIENCE")
    add_entry_heading(document, "㈜시스게이트 · 한림대학교의료원(강동) 전산 운영", "2019.08 – 2023.06 · OA 운영 및 사용자 지원")
    add_bullet(document, "30개 이상 부서의 OA 시스템 요구사항을 수집하고 하드웨어·소프트웨어 구성 검토와 도입 지원")
    add_bullet(document, "연간 300건 이상의 장애·사용자 요청을 처리하고 운영 매뉴얼, 정책, Q&A 대응 체계 정리")
    add_bullet(document, "신규 시스템 도입과 개편 과정에서 비IT 직군 대상 교육 자료를 제작하고 40회 이상 교육 진행")
    add_bullet(document, "코로나19 기간 전자결재·원격 OA 접근 체계 전환을 지원하며 중단 없는 업무 환경 유지")

    add_section_title(document, "EDUCATION")
    add_entry_heading(document, "KG IT BANK · 핀테크 서비스를 위한 풀스택 개발자 양성 과정", "2024.08 – 2025.02")
    add_body_paragraph(document, "Java, Spring Boot, SQL, JavaScript 기반 웹 서비스 설계와 팀 프로젝트 수행", size=8.8)
    add_entry_heading(document, "여주대학교 · 컴퓨터정보과", "2016.03 – 2020.02 · 졸업")

    document.add_page_break()

    add_section_title(document, "SELECTED PROJECTS")
    add_entry_heading(document, "BidMatch · AI 기반 공공입찰 맞춤 추천·자격진단 서비스", "2026.07.15 – 2026.08.05 · 5인 팀 PL")
    add_body_paragraph(
        document,
        "나라장터 공고와 기업정보를 연결해 맞춤 공고 추천, 근거 기반 자가 자격진단, 알림과 고객센터를 제공하는 서비스",
        size=8.9,
        color=GRAY,
        space_after=2.0,
    )
    add_bullet(document, "Java 17·Spring Boot로 일반/기업회원 인증, 기업정보·면허·실적, 고객센터와 SSE 알림 API 구현")
    add_bullet(document, "React 사용자 화면을 연동하고 Bruno 요청으로 Backend·AI API 계약과 예외 응답 검증")
    add_bullet(document, "FAQ RAG 챗봇에 역할별 검색, 낮은 유사도 차단, 다중 의도, LLM fallback과 민감정보 마스킹 적용")
    add_bullet(document, "BGE-M3 근거 검색, LLM 유형 분류, Spring 규칙 판정을 결합해 AI가 최종 자격 판정을 독점하지 않도록 설계")
    add_bullet(document, "병렬 개발 중 Flyway 버전·체크섬·레거시 스키마 충돌을 적용 이력을 보존하는 후속 마이그레이션으로 해결")
    add_bullet(document, "5개 저장소 118개 비병합 커밋 기여, AI pytest 242건 및 Backend·Frontend 최종 빌드/테스트 통과")
    add_body_paragraph(document, "기술: Spring Boot · FastAPI · React · PostgreSQL · Redis · BGE-M3 · RAG · LLM · Flyway", size=8.2, color=TEAL, space_after=2.0)

    add_entry_heading(document, "Intelligent Traffic Agent · Vision-to-Text 지능형 교통 관제", "2026.07.04 – 2026.07.07 · 개인")
    add_bullet(document, "YOLOv8 차량 탐지 결과와 Supabase 로그 조회를 LLM Function Calling으로 연결")
    add_bullet(document, "날짜 환각과 도구 호출 오류를 시간 파서·DB 결과 검증·대체 모델 경로로 완화하고 Word 관제 일지 생성")

    add_entry_heading(document, "Traffic Anomaly Detection · CCTV 교통량 이상탐지·예측", "2026.06.21 – 2026.07.01 · 개인")
    add_bullet(document, "YOLOv8 탐지, LSTM Autoencoder 이상탐지, ITS CCTV, Supabase 로그를 Streamlit 화면으로 통합")
    add_bullet(document, "입력 차원 불일치와 영상 지연을 reshape, 프레임 스킵, 표시 영상 리사이징으로 해결")

    add_entry_heading(document, "Flight Delay Prediction · 항공편 지연 예측", "2026.06.21 – 2026.06.24 · 개인")
    add_bullet(document, "약 25만 건 데이터를 전처리하고 XGBoost 등 모델을 비교해 불균형 데이터의 지연 Recall 중심으로 평가")
    add_bullet(document, "전처리·모델을 scikit-learn Pipeline으로 패키징해 Streamlit에 연결, Recall 65%·ROC-AUC 0.785 기록")

    add_entry_heading(document, "BidMatch Flask Prototype · 맞춤 공고 자동 수집·메일 알림", "2026.06.14 – 2026.06.20 · 팀 PL")
    add_bullet(document, "Flask·React로 OAuth/JWT 인증, Gmail 알림, Gemini 공고 요약, APScheduler 배치를 연결")
    add_bullet(document, "UTC/KST 발송 시간 차이를 Asia/Seoul 기준으로 보정하고 최종 Spring·FastAPI 프로젝트로 구조 확장")

    add_section_title(document, "PORTFOLIO")
    add_body_paragraph(document, "GitHub  https://github.com/kjongrok", bold_prefix="GitHub", size=8.8, space_after=0.8)
    add_body_paragraph(document, "BidMatch Backend  https://github.com/aiHuman1Team/back-end", bold_prefix="BidMatch Backend", size=8.6, space_after=0.8)
    add_body_paragraph(document, "BidMatch AI  https://github.com/aiHuman1Team/ai", bold_prefix="BidMatch AI", size=8.6, space_after=0.8)
    add_body_paragraph(document, "BidMatch Frontend  https://github.com/aiHuman1Team/front-end", bold_prefix="BidMatch Frontend", size=8.6, space_after=0.8)

    add_page_number(document.sections[0])
    document.save(OUTPUT_PATH)
    return OUTPUT_PATH


if __name__ == "__main__":
    print(build_resume())
