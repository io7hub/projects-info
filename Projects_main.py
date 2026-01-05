import streamlit as st
from streamlit.components.v1 import html
from pathlib import Path
import base64 # <-- 더 이상 사용하지 않아도 되지만, 기존 코드 구조 유지를 위해 남겨둠.
import os
# ======================================================
# 🚀 1. PDF 렌더링을 위한 라이브러리 추가
# (설치: pip install streamlit-pdf-viewer)
# ======================================================
try:
    from streamlit_pdf_viewer import pdf_viewer
except ImportError:
    st.error("streamlit_pdf_viewer 라이브러리가 설치되지 않았습니다. 'pip install streamlit-pdf-viewer'로 설치해주세요.")
    st.stop()


# ======================================================
# 기본 경로 설정
# ======================================================
BASE_DIR = Path(__file__).resolve().parent
IMG_DIR = BASE_DIR / "img"
HTML_DIR = BASE_DIR / "projects"


# ======================================================
# 유틸 함수
# ======================================================
def img_path(i):
    return IMG_DIR / f"p{i}.png"


def html_path(i):
    return HTML_DIR / f"p{str(i).zfill(2)}.html"


def pdf_path(i):
    return HTML_DIR / f"p{str(i).zfill(2)}.pdf"


def load_html(path: Path):
    try:
        return path.read_text(encoding="utf-8")
    except:
        return "<h3>❌ HTML 파일을 불러올 수 없습니다.</h3>"


# HTML 내부 이미지 경로 자동 복구
def render_html_with_fixed_img(html: str):
    # Windows/Linux 경로 호환성 확보
    html = html.replace("img/", str(IMG_DIR).replace("\\", "/") + "/")
    return html


# ❌ render_pdf_base64 함수는 제거 (streamlit_pdf_viewer 사용)

# ======================================================
# 📌 Streamlit 페이지 설정
# ======================================================
st.set_page_config(
    page_title="Kⁱ⁰⁷ · Portfolio_Projects",
    page_icon="🌎",
    layout="wide",
    initial_sidebar_state="collapsed")

if "selected" not in st.session_state:
    st.session_state.selected = None


st.balloons()

# ---------------------------------------------------------------
# 📌 3) 프로젝트 메타데이터 (직접 입력 방식)
# ---------------------------------------------------------------
projects = [
    {
        "id": 1,
        "title": "전략AI | AI-Ontology Converged BI",
        "desc": "전사 의사결정 자동화를 위한 온톨로지 기반 차세대 BI",
        "img": str(img_path(1)),
        "url": str(html_path(1)),
        "tags": ["Ontology", "AI_Agent", "Action_planner", "AI_Storyboard"]
    },
    {
        "id": 2,
        "title": "제조AI | 전동기 예지보전 통합 아키텍처",
        "desc": "3D Digital Twin - PdM_Edge_MLOps_Streamlit_Architecture",
        "img": str(img_path(2)),
        "url": str(html_path(2)),
        "tags": ["Ontology-Driven", "AI-Planner", "Strategy", "AI-Agent", "제조AI", "제조업", "생산경영", "플래너", "360610"]
    },
    {
        "id": 3,
        "title": "제조AI | AI Agent 기반 생산 전략 최적화",
        "desc": "기존 데이터 기반 진단(시간/할당/인력) 및 분석 시뮬레이션을 통한 최적화 모색",
        "img": str(img_path(3)),
        "url": str(html_path(3)),
        "tags": ["AI", "Agent", "KPI"]
    },
    {
        "id": 4,
        "title": "전략 AI | LATAM 맞춤형 IoT Master 플랫폼 구축",
        "desc": "Raspberry Pi 기반 IoT Edge & SCADA 구축",
        "img": str(img_path(4)),
        "url": str(html_path(4)),
        "tags": ["IoT", "Edge", "SCADA"]
    },
    {
        "id": 5,
        "title": "전략 AI | AI + 온톨로지 기반 전략 플래너",
        "desc": "AI + 온톨로지 기반 차세대 스마트 제조 솔루션_알루미늄 가공",
        "img": str(img_path(5)),
        "url": str(html_path(5)),
        "tags": ["SmartFarm", "IoT"]
    },
    {
        "id": 6,
        "title": "전략AI | Industrial IoT Master Architecture",
        "desc": "네트워크 불안정과 도입 비용을 극복하는 솔루션",
        "img": str(img_path(6)),
        "url": str(html_path(6)),
        "tags": ["IoT Master", "IoT Platform", "Edge-Cloud"]
    },
    {
        "id": 7,
        "title": "제조AI | 효율 분석 기반 생산성 혁신 전략",
        "desc": "DATA-DRIVEN MANUFACTURING PRODUCTIVITY IMPROVEMENT",
        "img": str(img_path(7)),
        "url": str(html_path(7)),
        "tags": ["KPIs", "Diagnosis", "Action_Plane", "LeadTime", "WIP", "OEE", "PPM", "Productivity", "Efficiency", "OTIF", "Dashboard", "IoT_Master", "DX"]
    },
    {
        "id": 8,
        "title": "제조AI | AI + 온톨로지 통합 분석 시스템",
        "desc": "AI-Agent + Ontology Engine + Rule Engine 통합 솔루션",
        "img": str(img_path(8)),
        "url": str(html_path(8)),
        "tags": ["", "Welding", "AXDX", "공정지능화", "로봇용접", "온톨로지", "ONTOLOGY", "ROBOT","AION01"]
    },
    {
        "id": 9,
        "title": "농산업AI | Kⁱ⁰⁷ Smart Farm AI Agent",
        "desc": "🍓 딸기 스마트팜 AI 전략 보고서",
        "img": str(img_path(9)),
        "url": str(html_path(9)),
        "tags": ["SmartFarm", "IoT", "실시간대시보드", "농가AI", "실행로드맵", "스마트팜전략"]
    },
    {
        "id": 10,
        "title": "전략AI | KADI 에콰도르 농기계 ODA 사업",
        "desc": "고산지대 농기계 도입 및 현지화 전략",
        "img": str(img_path(10)),
        "url": str(html_path(10)),
        "tags": ["ODA", "DX"]
    },
    {
        "id": 11,
        "title": "전략AI | 생산 ROI 분석 AGENT",
        "desc": "핵심 지표 분석을 통한 ROI 개선 시스템",
        "img": str(img_path(11)),
        "url": str(html_path(11)),
        "tags": ["IoT_Platform", "Streamlit_UI", "KPI", "Environment", "Policy", "Packaging", "Regulation", "Monitering", "법제정비", "경량_모니터링_플랫폼", "모니터링"]
    },
    {
        "id": 12,
        "title": "제조AI | LangChain 기반 Manufacturing AI Agent",
        "desc": "온톨로지 기반 제조 AI 분석 에이전트 개발",
        "img": str(img_path(12)),
        "url": str(html_path(12)),
        "tags": ["LangChain", "AI_Agent", "Ontology", "DX"]
    },
    {
        "id": 13,
        "title": "전략AI | Streamlit SQL Analyzer",
        "desc": "Query → KPI → Chart 자동화 엔진",
        "img": str(img_path(13)),
        "url": str(html_path(13)),
        "tags": ["AI", "Streamlit", "SQL", "BI", "KPI"]
    },
    {
        "id": 14,
        "title": "전략AI | Industrial Diagram Studio",
        "desc": "현장 중심 아키텍처 시각화 솔루션",
        "img": str(img_path(14)),
        "url": str(html_path(14)),
        "tags": ["KPI", "Streamlit", "Analytics", "Dashboard"]
    },
    {
        "id": 15,
        "title": "전략AI | Aluminum-Air Battery",
        "desc": "Al-Air 전지 시제품 생산 시스템 구축 사업제안",
        "img": str(img_path(15)),
        "url": str(html_path(15)),
        "tags": ["Al-Air_Battery", "Al_anode", "O₂_cathode", "Battery", "Research_Data", "Purity", "surface_treatment", "electrolyte", "cell_design", "typical_alloys", "high_purity_aluminum", "aluminum_alloys"]
    },
    {
        "id": 16,
        "title": "Kⁱᵒ⁷ 제조AI | 자동차부품 Smart Quality Planner",
        "desc": "AI 기반 자체 품질 관리 프레임워크 개발",
        "img": str(img_path(16)),
        "url": str(html_path(16)),
        "tags": ["AI-Driven", "AI-Planner", "Quality", "AI-Agent", "제조AI", "자동차부품", "품질", "플래너", "361317"]
    },
    {
        "id": 17,
        "title": "전략AI | Digital Twin Factory Viewer(3D)",
        "desc": "Node → Edge 3D 공정 시각화 엔진",
        "img": str(img_path(17)),
        "url": str(html_path(17)),
        "tags": ["DigitalTwin", "3D", "Visualization"]
    },
    {
        "id": 18,
        "title": "전략AI | 중남미 중소기업 DX 전략",
        "desc": "경량 IoT 플랫폼 기반의 현지 맞춤형 DX 솔루션 개발 및 전개 방안",
        "img": str(img_path(18)),
        "url": str(html_path(18)),
        "tags": ["디지털성숙도", "데이터분석", "알림&의사결정", "대응조치&이력조회", "폐쇄루프파이프라인", "Edge", "Cloud", "DigitalMaturity", "KPIsMonitering", "IoT", "Streamlit", "Google_Chat", "Trello", "LATAM", "FabrikMonitor", "QSI", "Eco-Sensor", "MES-Lite", "DX"]
    },
    {
        "id": 19,
        "title": "전략AI | DX Strategy for LATAM SMEs",
        "desc": "중남미 정부·기업 대상 DX 맞춤형 컨설팅 교육 프로그램",
        "img": str(img_path(19)),
        "url": str(html_path(19)),
        "tags": ["Technology_Blueprint", "Lightweight_IoT_Architecture", "DX Education", "LATAM", "IoT_Platform", "Light_MES", "IoT_Master", "Streamlit_UI"]
    },
    {
        "id": 20,
        "title": "전략AI | KPI Rule Engine Editor",
        "desc": "규칙 기반 KPI 진단 엔진 개발",
        "img": str(img_path(20)),
        "url": str(html_path(20)),
        "tags": ["Rule_Engine", "KPI", "Analysis", "Ontology", "DX"]
    },
    {
        "id": 21,
        "title": "제조AI | 품질 리스크 정량 분석",
        "desc": "FMEA와 AI 통합 기반의 Torque·Leak·Lock Force 분석 및 품질 예측",
        "img": str(img_path(21)),
        "url": str(html_path(21)),
        "tags": ["제조AI", "IoT", "DX", "KPI", "MES", "FMEA", "Quality", "Risk", "Action_Planner"]
    },
    {
        "id": 22,
        "title": "제조AI | Manufacturing.AI Storyboard",
        "desc": "AI-Driven Industrial Process Intelligence Framework",
        "img": str(img_path(22)),
        "url": str(html_path(22)),
        "tags": ["AI_Planner", "Quality", "MES", "IoT_Master", "DX"]
    },
    {
        "id": 23,
        "title": "전략AI | El Salvador SME DX Strategy",
        "desc": "A Lightweight, Modular, and Action-Oriented Pipeline for Digital Transformation",
        "img": str(img_path(23)),
        "url": str(html_path(23)),
        "tags": ["DMI", "Data&Analysis", "Alert&Discussion", "Action&Tracking", "Closed-Loop-Pipeline", "IoT", "DigitalMaturity", "LATAM", "ODA", "DX"]
    },
    {
        "id": 24,
        "title": "제조AI | 공정 지능화 AI-Agent — 유압설비편",
        "desc": "유압 장비 사용자 스토리보드 기반 AI-Agent 개발 · Ontology 엔진 고도화",
        "img": str(img_path(24)),
        "url": str(html_path(24)),
        "tags": ["IoT", "Edge", "Hydraulic", "DX_Planner"]
    },
    {
        "id": 25,
        "title": "전략AI | 온라인 플랫폼 분석 AI Agent",
        "desc": "플랫폼 지표 기반 성장전략 자동 분석 AI Agent 개발",
        "img": str(img_path(25)),
        "url": str(html_path(25)),
        "tags": ["Platform_data", "AI_Strategy_Planner", "BI", "Dashboard", "SQL"]
    },
    {
        "id": 26,
        "title": "전략AI | 데이터 기반 인사관리 시뮬레이터",
        "desc": "데이터 분석 기반의 액션 플랜 및 시뮬레이션 모델 개발",
        "img": str(img_path(26)),
        "url": str(html_path(26)),
        "tags": ["HR_Analytics", "KPI", "HR_Strategy", "BI", "Simulator"]
    },
    {
        "id": 27,
        "title": "전략AI | AI 기반 플랫폼 분석 및 성장 전략 보고서 생성",
        "desc": "플랫폼의 세부 분석, 플랫폼 성장 전략, 로드맵&액션플랜 AI Agent 개발",
        "img": str(img_path(27)),
        "url": str(html_path(27)),
        "tags": ["AI_Platform", "DataFrame", "DB", "SQL", "BI", "Visualization"]
    },
    {
        "id": 28,
        "title": "제조AI | 생산 효율 분석 및 로드맵 수립",
        "desc": "부서별 가용 시간 대비 효율 진단 및 개선 전략 AI Agent 개발",
        "img": str(img_path(28)),
        "url": str(html_path(28)),
        "tags": ["KPIs", "EPD", "EPR", "Visualization", "Productivity", "Efficiency", "Dashboard", "IoT_Master", "DX", "AI_Action_Planner", "Insight", "가용효율성", "보고효율성"]
    },
    {
        "id": 29,
        "title": "제조AI | AI 기반 HPDC 생산전략",
        "desc": "중남미 맞춤형 고압주조(HPDC) 생산현장 DX 전용 AI Agent 개발",
        "img": str(img_path(29)),
        "url": str(html_path(29)),
        "tags": ["HPDC", "Dinamic_Dashboard", "DX Strategy", "IoT", "AI_Action_Planner", "Insight", "LATAM", "고압주조", "생산전략", "중남미", "운영탄력성", "기술내재화", "동적시각화"]
    },
    {
        "id": 30,
        "title": "전략AI | LATAM 파트너 디지털 성숙도 분석",
        "desc": "7개 파트너 기업 DX 성숙도 진단 및 시장 분석",
        "img": str(img_path(30)),
        "url": str(html_path(30)),
        "tags": ["DMI", "Partners", "KeyInsights", "IoT", "SmartFactory", "DigitalMaturity", "LATAM", "ODA", "DX"]
    },
    {
        "id": 31,
        "title": "전략AI | LATAM 경영 전략 보고서",
        "desc": "Kⁱ⁰⁷ Manufacturing Intelligence Platform 기반 경영 전략 보고서",
        "img": str(img_path(31)),
        "url": str(html_path(31)),
        "tags": ["전략 AI", "하이브리드 인텔리전스", "AI", "Ontology", "LangChain", "Graphviz", "3D Simulator", "LATAM", "ODA", "DX"]
    },
    {
        "id": 32,
        "title": "제조AI | Su Día Cambiará Hoy",
        "desc": "Estrategias de Transformación Digital para Mejorar la Eficiencia y Productividad",
        "img": str(img_path(32)),
        "url": str(html_path(32)),
        "tags": ["제조 AI", "Desafíos enfrentados", "Tiempo Perdidos", "Errores en cálculo manuales", "Decisiones para mejoras", "IoT", "SmartFactory", "Manufacturing Intelligence", "LATAM", "Kⁱ⁰⁷ Platform", "DX"]
    },
    {
        "id": 33,
        "title": "전략AI | 생산 ROI 기준선 분석 AGENT",
        "desc": "보유 데이터 기반으로 AI 에이전트가 Baseline을 확립하고, 문제를 진단·시각화하여 ROI 중심의 실행 과제 우선순위를 제시하는 플랫폼",
        "img": str(img_path(33)),
        "url": str(html_path(33)),
        "tags": ["전략 AI", "수기 데이터", "기준선 분석", "IoT 연동", "실시간 시각화", "클라우드", "LATAM", "ODA", "DX"]
    },
    {
        "id": 34,
        "title": "제조AI | Fe-C 상태도 실무 활용 시스템",
        "desc": "Fe-C 상태도 기반 AI + Ontology + LangChain 통합 솔루션",
        "img": str(img_path(34)),
        "url": str(html_path(34)),
        "tags": ["제조 AI", "Kⁱ⁰⁷ Fe-C 상태도", "AI + Ontology", "LangChain Agent", "냉간 인발 튜브", "Heat Treatment", "열처리", "DX"]
    },
    {
        "id": 35,
        "title": "제조AI | 공정 분석 및 전략적 대안 시스템",
        "desc": "냉간인발 강관 제조공정 | 종합 검토 및 실행 계획",
        "img": str(img_path(35)),
        "url": str(html_path(35)),
        "tags": ["제조 AI", "냉간인발", "Sankey Diagram", "BYPASS 공정", "비파괴검사", "공정분석", "AI + 룰 엔진", "DX"]
    },
]
# ---------------------------------------------------------------
# 📌 4) 프로젝트 이미지 렌더링 (300x200 고정)
# ---------------------------------------------------------------
def render_project_image(path: str):
    f = Path(path)
    if not f.exists():
        return """
        <div style="width:300px;height:200px;border-radius:12px;
             background:#EEE;border:1px solid #CCC;
             display:flex;align-items:center;justify-content:center;">
            <span style="opacity:0.4;">No Image</span>
        </div>
        """

    b64 = base64.b64encode(f.read_bytes()).decode()
    return f"""
        <img src="data:image/png;base64,{b64}"
             style="width:300px;height:200px;object-fit:cover;
             border-radius:12px;border:1px solid #CCC;">
    """


# ---------------------------------------------------------------
# 📌 5) Global CSS (헤더 상단 여백 최소화 반영)
# ---------------------------------------------------------------
GLOBAL_CSS = """
<style>
/* 🚀 Streamlit 기본 여백 제거 (핵심 수정 부분) */
/* .stApp 클래스는 Streamlit 앱 전체를 감싸는 컨테이너입니다. */
/* header { display: none; } 은 상단 메뉴를 없앨 때 사용 가능 */
.stApp {
    padding-top: 0 !important;
}

/* Streamlit의 메인 컨테이너 (여백의 주범) */
.stApp > header {
    display: none; /* Streamlit의 기본 헤더 제거 */
}

/* Streamlit이 콘텐츠를 감싸는 main 태그의 상단 패딩 제거 */
.stApp > div:first-child > section {
    padding-top: -0 !important;
}

/* Streamlit이 페이지 콘텐츠를 감싸는 main 태그의 상단 패딩 제거 */
.main {
    padding-top: -0 !important; 
}


/* body는 Streamlit 컨테이너의 바깥이라 영향을 덜 줍니다. */
body {
    background-color: #F7F9FB;
}
/* 🚀 1. 폰트 적용 */
body, .stApp, p, h1, h2, h3, h4, .stText, .stMarkdown {
    font-family: 'Noto Sans KR', sans-serif !important; 
}
/* 헤더 스타일 */
.header-container {
    width: 100%;
    padding: 40px 10px;
    border-radius: 20px;
    background: linear-gradient(135deg, #005CFF, #00C06F);
    text-align: center;
    color: white;
    /* 기존 margin-bottom 유지 */
    margin-bottom: 1rem;
}

.header-title {
    color: white;
    font-size: 3rem;
    font-weight: bold;
    margin-bottom: 0.5rem;
}

.header-subtitle {
    color: rgba(255,255,255,0.9);
    font-size: 1.2rem;
    margin-bottom: 1rem;
}

.header-tags {
    display: flex;
    justify-content: center;
    gap: 1rem;
    flex-wrap: wrap;
    margin-top: 1rem;
}

.header-tag {
    background: rgba(255,255,255,0.2);
    padding: 0.5rem 1rem;
    border-radius: 20px;
    color: white;
    font-size: 0.9rem;
}

/* Project Cards */
.k_card {
    padding: 10px;
    border-radius: 16px;
    background: #FFFFFF;
    box-shadow: 0 0 6px rgba(0,0,0,0.07);
    margin-bottom: 18px;
    transition: 0.2s ease;
}
.k_card:hover {
    transform: translateY(-4px);
    box-shadow: 0 6px 18px rgba(0,0,0,0.12);
}

/* 이미지 고정 크기 */
.k_img {
    width: 100%;
    height: 200px;
    object-fit: cover;
    border-radius: 14px;
    background: #EEE;
}

</style>
"""
st.markdown(GLOBAL_CSS, unsafe_allow_html=True)


# ---------------------------------------------------------------
# 📌 6) Header
# ---------------------------------------------------------------
HEADER_HTML = """
<div class="header-container">
    <div class="header-title">🌎 Kinam Kim | Portfolio</div>
    <div class="header-subtitle">
        Kⁱ⁰⁷ 데이터로 현장을 읽고, 전략으로 연결하는 데이터 기반 가치 전환 전략가
    </div>
    <div class="header-tags">
        <span class="header-tag">AI Engineering</span>
        <span class="header-tag">IoT · Ontology</span>
        <span class="header-tag">AX Strategy</span>
        <span class="header-tag">Manufacturing Intelligence</span>
    </div>
</div>
"""
st.markdown(HEADER_HTML, unsafe_allow_html=True)


# ---------------------------------------------------------------
# 📌 7) SPA 상태 변수
# ---------------------------------------------------------------
if "selected" not in st.session_state:
    st.session_state.selected = None


# ======================================================
# 📌 8) 상세 페이지 — 항상 최상단에서 먼저 렌더링
# ======================================================
if st.session_state.selected is not None:

    proj = next((p for p in projects if p["id"] == st.session_state.selected), None)

    if proj:
        file_path = Path(proj["url"])

        # ----------------------------------------------------
        # 🚀 1행 3열 구조 (헤더)
        # ----------------------------------------------------
        col_button, col_title, col_desc = st.columns([0.15, 0.55, 0.3])
        
        # 1열: 돌아가기 버튼 
        with col_button:
            st.write("") 
            if st.button("⬅ Back to Portfolio", use_container_width=True):
                st.session_state.selected = None
                st.rerun()

        # 2열: 프로젝트 제목
        with col_title:
            st.markdown(f"## {proj['title']}")

        # 3열: 프로젝트 설명
        with col_desc:
            st.markdown(f"<div style='margin-top: 1.5rem;'>{proj['desc']}</div>", unsafe_allow_html=True)

#        st.markdown("---")
        # ----------------------------------------------------
    
        # 💡 [핵심 복구] HTML/PDF 상세 내용을 담는 컨테이너
        st.markdown("<div class='k_detail_box'>", unsafe_allow_html=True)
        
        # ----------------------------------------------------
        # 🚀 HTML 상세 페이지 렌더링 로직 (안정화)
        # ----------------------------------------------------
        def inject_before_close_tag(html: str, snippet: str) -> str:
            lower = html.lower()
            i = lower.rfind("</body>")
            if i != -1:
                return html[:i] + snippet + html[i:]
            i = lower.rfind("</html>")
            if i != -1:
                return html[:i] + snippet + html[i:]
            return html + snippet


        if file_path.suffix.lower() == ".html":

            if file_path.exists():
                try:
                    raw_html = load_html(file_path)
                    fixed = render_html_with_fixed_img(raw_html)

                    # ✅ 문서 높이만큼 iframe(height) 자동 조정 스크립트
                    # - 이미지/폰트 로딩 이후에도 1~2회 재계산
                    # - 필요하면 cap을 걸어 과도한 높이 방지 가능
                    auto_height_script = """
                    <script>
                    (function () {
                    function docHeight() {
                        const b = document.body;
                        const e = document.documentElement;
                        return Math.max(
                        b ? b.scrollHeight : 0,
                        e ? e.scrollHeight : 0,
                        b ? b.offsetHeight : 0,
                        e ? e.offsetHeight : 0
                        );
                    }

                    function resizeFrame() {
                        try {
                        // 문서 기본 여백 제거(선택)
                        document.documentElement.style.margin = "0";
                        document.body.style.margin = "0";

                        const h = docHeight() + 16;  // 약간의 여유

                        // (선택) 너무 큰 문서로 인한 성능 이슈가 있으면 cap 사용
                        // const cap = 50000; 
                        // const finalH = Math.min(h, cap);

                        const finalH = h;

                        if (window.frameElement) {
                            window.frameElement.style.height = finalH + "px";
                            window.frameElement.style.width = "100%";
                        }
                        } catch (e) {}
                    }

                    // 초기 1회
                    resizeFrame();

                    // 로드 후(이미지/폰트 반영)
                    window.addEventListener("load", function () {
                        resizeFrame();
                        setTimeout(resizeFrame, 100);
                        setTimeout(resizeFrame, 300);
                    }, { once: true });

                    // DOM 변화가 있을 때만 반영 (가볍게)
                    try {
                        const ro = new ResizeObserver(() => resizeFrame());
                        ro.observe(document.documentElement);
                        ro.observe(document.body);
                    } catch (e) {}
                    })();
                    </script>
                    """

                    final_html = inject_before_close_tag(fixed, auto_height_script)

                    # ✅ 핵심: scrolling=False (iframe 내부 스크롤 제거)
                    # ✅ height는 “초기값”일 뿐, 스크립트가 최종 높이를 덮어씀
                    st.components.v1.html(final_html, height=600, scrolling=False)

                except Exception as e:
                    st.error(f"HTML 파일을 불러오는 중 오류가 발생했습니다: {e}")
                    st.warning(f"파일 경로: {str(file_path)}")
            else:
                st.error(f"HTML 파일이 지정된 경로에 존재하지 않습니다: {str(file_path)}")
                
        # ----------------------------------------------------
        # PDF 상세 페이지 렌더링 로직 (이전 최종 코드를 사용한다고 가정)
        # ----------------------------------------------------
        elif file_path.suffix.lower() == ".pdf":
            st.write("PDF 렌더링 로직이 여기에 위치합니다.")
            # ... (이전에 제공된 Base64 + Fallback 로직 삽입) ...

        st.markdown("</div>", unsafe_allow_html=True) # k_detail_box 닫기
        
        st.stop()


# ---------------------------------------------------------------
# 📌 9) 기본 홈 페이지 (카드 그리드)
# ---------------------------------------------------------------
# -----------------------------------------------------------
# (1) 버튼 텍스트 좌측 정렬을 위한 CSS 오버라이드
# -----------------------------------------------------------
st.markdown("""
<style>

div.stButton > button {
    /* Gradient background */
    background: linear-gradient(135deg, #1E3C72 0%, #2A5298 50%, #0E1117 100%) !important;

    /* Text */
    color: white !important;
    font-family: 'Noto Sans KR', sans-serif !important;         
    font-weight: 600 !important;
    font-size: 17px !important;
    text-align: left !important;
    justify-content: flex-start !important;
    padding-left: 16px !important;

    /* Shape */
    border-radius: 12px !important;
    border: none !important;

    /* Premium shadow */
    box-shadow: 0 4px 12px rgba(0,0,0,0.25) !important;
    transition: all 0.25s ease-in-out !important;
}

/* Hover effect: Brighter + Glow */
div.stButton > button:hover {
    background: linear-gradient(135deg, #264B8E 0%, #3C66B2 50%, #6B91D6 100%) !important;
    transform: translateY(-2px);
    box-shadow: 0 6px 18px rgba(50, 120, 255, 0.45) !important;
}

div.stList {
    /* Gradient background */
    background: linear-gradient(135deg, #1E3C72 0%, #2A5298 50%, #0E1117 100%) !important;

    /* Text */
    color: white !important;
    font-family: 'Noto Sans KR', sans-serif !important;         
    font-weight: 600 !important;
    font-size: 17px !important;
    text-align: left !important;
    justify-content: flex-start !important;
    padding-left: 16px !important;

    /* Shape */
    border-radius: 12px !important;
    border: none !important;

    /* Premium shadow */
    box-shadow: 0 4px 12px rgba(0,0,0,0.25) !important;
    transition: all 0.25s ease-in-out !important;
}         

/* Active (click) effect */
div.stButton > button:active {
    transform: translateY(0px) !important;
    box-shadow: 0 3px 8px rgba(0,0,0,0.35) !important;
}

</style>
""", unsafe_allow_html=True)


# -----------------------------------------------------------
# (2) 프로젝트 카드 UI
# -----------------------------------------------------------
st.subheader("📁 프로젝트 목록")
LIST_HTML = """
<div class="stList header-container">
    <div class="st.subheader">📁 프로젝트 목록</div>
</div>
"""
st.markdown(LIST_HTML, unsafe_allow_html=True)


cols_per_row = 3

for i in range(0, len(projects), cols_per_row):

    cols = st.columns(cols_per_row)

    for col, proj in zip(cols, projects[i:i + cols_per_row]):

        # 버튼 (텍스트 좌측 정렬됨)
        if col.button(proj["title"], key=f"btn_{proj['id']}", use_container_width=True):
            st.session_state.selected = proj["id"]
            st.rerun()

        # 이미지 렌더링
        img_html = render_project_image(proj["img"])
        col.markdown(img_html, unsafe_allow_html=True)

        # 제목 + 설명
        col.markdown(f"""
            <div style="text-align: left;font-size:18px;font-weight:650;margin-top:8px;">
                {proj['title']}
            </div>
            <div style="font-size:14px;opacity:0.75;">
                {proj['desc']}
            </div>
        """, unsafe_allow_html=True)

    st.markdown("<hr>", unsafe_allow_html=True)


# ---------------------------------------------------------------
# 📌 푸터
# ---------------------------------------------------------------
#    st.markdown("---")
#    st.markdown("""
#        <div style="text-align: center; color: #6b7280; padding: 2rem;">
#            <p>© 2024 Data-driven VX Strategist | Kⁱ⁰⁷ | 📧 io7hub@naver.com</p>
#            <p style="font-size: 0.875rem;">데이터 기반 가치 전환 전략가</p>
#        </div>
#    """, unsafe_allow_html=True)    