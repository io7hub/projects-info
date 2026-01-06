import streamlit as st
import streamlit.components.v1 as components
from pathlib import Path
from collections import Counter
import re

st.set_page_config(
    page_title="Kⁱ⁰⁷ AI 기반 가치 전환 전략_270525_0913",
    page_icon="🌎",
    layout="wide",
    initial_sidebar_state="expanded"
)

st.balloons()

st.markdown("""
<style>
    .main {
        margin-top: 0.5rem;    
    }
    
    .block-container {
        padding-top: 3rem;
        padding-bottom: 0rem;
    }    
            
    body, .stApp, p, h1, h2, h3, h4, .stText, .stMarkdown {
        font-family: 'Noto Sans KR', sans-serif !important; 
    }        

    .header-container {
        background: linear-gradient(135deg, #1a1a2e 0%, #16213e 50%, #0f3460 100%);
        padding: 2rem 2rem;
        border-radius: 12px;
        margin-bottom: 2rem;
        text-align: center;
        box-shadow: 0 8px 16px rgba(0,0,0,0.3);
        border: 1px solid rgba(255,255,255,0.1);
    }
    
    .header-title {
        color: #00d9ff;
        font-size: 2.5rem;
        font-weight: 800;
        margin-bottom: 0.8rem;
        text-shadow: 0 2px 10px rgba(0, 217, 255, 0.3);
        letter-spacing: -0.5px;
    }
    
    .header-subtitle {
        color: rgba(255,255,255,0.85);
        font-family: 'Noto Sans KR', sans-serif;
        font-size: 1.1rem;
        margin-bottom: 1.2rem;
        line-height: 1.6;
        font-weight: 400;
    }
    
    .header-tags {
        display: flex;
        justify-content: center;
        gap: 0.8rem;
        flex-wrap: wrap;
        margin-top: 1rem;
    }
    
    .header-tag {
        background: rgba(0, 217, 255, 0.15);
        padding: 0.5rem 1.2rem;
        border-radius: 20px;
        color: #00d9ff;
        font-family: 'Noto Sans KR', sans-serif;             
        font-size: 0.85rem;
        border: 1px solid rgba(0, 217, 255, 0.3);
        font-weight: 500;
        transition: all 0.3s;
    }
    
    .header-tag:hover {
        background: rgba(0, 217, 255, 0.25);
        border-color: rgba(0, 217, 255, 0.5);
    }
    
    .stats-container {
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
        gap: 1rem;
        margin-bottom: 2rem;
    }
    
    .stat-card {
        background: #f8f9fa;
        padding: 1.5rem;
        border-radius: 10px;
        text-align: center;
        border-left: 4px solid #0066cc;
    }
    
    .stat-number {
        font-size: 2.5rem;
        font-weight: bold;
        color: #0066cc;
    }
    
    .stat-label {
        color: #666;
        font-size: 0.9rem;
        margin-top: 0.5rem;
    }
    
    .project-card {
        background: #e3f2fd
        border-radius: 10px;
        padding: 1rem;
        box-shadow: 0 2px 8px rgba(0,0,0,0.1);
        transition: transform 0.2s, box-shadow 0.2s;
        height: 100%;
    }
    
    .project-card:hover {
        transform: translateY(-5px);
        box-shadow: 0 4px 12px rgba(0,0,0,0.15);
    }
    
    .project-image {
        width: 300px !important;
        height: 200px !important;
        object-fit: cover;
        border: 4px solid #ffffff; 
        border-radius: 8px;
        box-shadow: 0 4px 10px rgba(0, 0, 0, 0.3); 
        box-sizing: border-box; 
    }
    
    .project-title {
        font-size: 1.1rem;
        font-weight: bold;
        margin-bottom: 0.5rem;
        color: #333;
    }
    
    .project-desc {
        color: #666;
        font-size: 0.9rem;
        margin-bottom: 1rem;
    }
    
    .tag-container {
        display: flex;
        flex-wrap: wrap;
        gap: 0.3rem;
        margin-top: 0.5rem;
    }
    
    .tag {
        background: #e3f2fd;
        color: #0066cc;
        padding: 0.5rem 0.6rem;
        border-radius: 12px;
        font-size: 1rem;
        border: 1px solid #bbdefb;
    }
    
    .stButton > button {
        width: 100%;
        background: linear-gradient(135deg, #0066cc 0%, #00cc99 100%);
        color: white;
        border: none;
        padding: 0.1rem 0.1rem;
        border-radius: 5px;
        font-weight: 500;
        transition: transform 0.2s, box-shadow 0.2s;
        margin-top: 0.1rem;    
    }
    
    .stButton > button:hover {
        transform: translateY(-2px);
        box-shadow: 0 4px 8px rgba(0, 102, 204, 0.3);
    }
    
    .footer {
        background: #2c3e50;
        color: white;
        padding: 2rem;
        margin-top: 4rem;
        border-radius: 10px;
    }
    
    .footer-content {
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
        gap: 2rem;
    }
    
    .footer-section h4 {
        margin-bottom: 1rem;
        color: #00cc99;
    }
    
    .footer-link {
        color: #ecf0f1;
        text-decoration: none;
        display: block;
        margin-bottom: 0.5rem;
    }
    
    .footer-link:hover {
        color: #00cc99;
    }
    
    .footer-bottom {
        text-align: center;
        margin-top: 2rem;
        padding-top: 1rem;
        border-top: 1px solid rgba(255,255,255,0.1);
        color: #95a5a6;
    }
    
    .filter-section {
        background: #f8f9fa;
        padding: 1rem;
        border-radius: 10px;
        margin-bottom: 2rem;
    }

    .search-result-count {
        color: #666;
        font-size: 0.9rem;
        margin-bottom: 1rem;
    }
</style>
""", unsafe_allow_html=True)


def img_path(id):
    return f"img/p{id}.png"

def html_path(id):
    return f"projects/p{id}.html"

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
        "tags": ["제조AI", "ROI", "Simulation", "Pareto", "Risk", "Cycle Time", "Operation", "Compensation", "AI Agent", "KPI"]
    },
    {
        "id": 4,
        "title": "전략 AI | LATAM 맞춤형 IoT Master 플랫폼 구축",
        "desc": "Raspberry Pi 기반 IoT Edge & SCADA 구축",
        "img": str(img_path(4)),
        "url": str(html_path(4)),
        "tags": ["IoT Sensor", "PLC", "Streamlit", "Edge", "Modbus TCP", "HMI", "Node-RED", "MLOps", "Rest API", "Local DB", "Cloud", "SCADA"]
    },
    {
        "id": 5,
        "title": "전략 AI | AI + 온톨로지 기반 전략 플래너",
        "desc": "AI + 온톨로지 기반 차세대 스마트 제조 솔루션_알루미늄 산업편",
        "img": str(img_path(5)),
        "url": str(html_path(5)),
        "tags": ["Aluminum", "Ontology", "Strategy Planner", "Rule Engine", "KPIs", "Parameter", "Analysis", "IoT"]
    },
    {
        "id": 6,
        "title": "전략AI | Industrial IoT Master Architecture",
        "desc": "네트워크 불안정과 도입 비용을 극복하는 솔루션",
        "img": str(img_path(6)),
        "url": str(html_path(6)),
        "tags": ["IoT Master", "IoT Platform", "Edge-Cloud", "Field Layer", "10.1인치", "1280x800", "Raspberry Pi", "Streamlit UI", "Node-RED", "InfluxDB", "Grafana", "MQTT", "Modbus TCP", "OPC UA", "RS485", "RS232", "SQLite DB", "Edge Layer", "Cloud Layer", "LATAM", "DX"]
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
        "tags": ["Welding", "AXDX", "공정지능화", "로봇용접", "온톨로지", "ONTOLOGY", "ROBOT", "AION01"]
    },
    {
        "id": 9,
        "title": "농산업AI | Kⁱ⁰⁷ Smart Farm AI Agent",
        "desc": "🍓 딸기 스마트팜 AI 전략 보고서",
        "img": str(img_path(9)),
        "url": str(html_path(9)),
        "tags": ["SmartFarm", "IoT", "Storyboard", "AI Agent", "실시간대시보드", "농가AI", "실행로드맵", "스마트팜전략"]
    },
    {
        "id": 10,
        "title": "전략AI | KADI 에콰도르 농기계 ODA 사업",
        "desc": "고산지대 농기계 도입 및 현지화 전략",
        "img": str(img_path(10)),
        "url": str(html_path(10)),
        "tags": ["Maquinaria Agricola", "Ecosistema Sostenible", "Sierra", "Tractor", "Kubota", "John Deere", "Localizacion", "ODA", "Agricultura", "KADI", "에콰도르", "농기계", "고산지대", "현지화"]
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
        "tags": ["Graphviz", "KPIs", "AI", "3D Viewer", "Industrial Diagram", "Pipeline", "Workflow", "Streamlit UI", "Analytics", "Dashboard"]
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
        "tags": ["DigitalTwin", "3D Viewer", "Strategic Pipeline", "DOT", "Strategic Decision", "Node-Edge", "AS-IS vs TO-BE", "Simulation", "Insight", "Visualization"]
    },
    {
        "id": 18,
        "title": "전략AI | 중남미 중소기업 DX 전략",
        "desc": "경량 IoT 플랫폼 기반의 현지 맞춤형 DX 솔루션 개발 및 전개 방안",
        "img": str(img_path(18)),
        "url": str(html_path(18)),
        "tags": ["IoT", "Streamlit", "Google_Chat", "Trello", "디지털성숙도", "데이터분석", "알림&의사결정", "대응조치&이력조회", "폐쇄루프파이프라인", "Edge", "Cloud", "DigitalMaturity", "KPIsMonitering", "LATAM", "FabrikMonitor", "QSI", "Eco-Sensor", "MES-Lite", "DX"]
    },
    {
        "id": 19,
        "title": "전략AI | DX Strategy for LATAM SMEs",
        "desc": "중남미 정부·기업 대상 DX 맞춤형 컨설팅 교육 프로그램",
        "img": str(img_path(19)),
        "url": str(html_path(19)),
        "tags": ["IoT", "PoCs", "Local Partner", "Empower People", "MES lite", "Road map", "Technology_Blueprint", "Lightweight_IoT_Architecture", "DX Education", "LATAM", "IoT_Platform", "IoT_Master", "Streamlit_UI"]
    },
    {
        "id": 20,
        "title": "전략AI | KPIs Rule Engine Editor",
        "desc": "규칙 기반 KPIs 진단 엔진 개발",
        "img": str(img_path(20)),
        "url": str(html_path(20)),
        "tags": ["XAI", "Ruleset", "Graph-Rule", "If-Then", "Decision Matrix","Neo4j", "Low-Code", "No-Code", "Domain Knowledge", "Semantic Web Rule Language", "Reasoning", "Semantic Reasoning", "Rule_Engine", "Ontology", "KPIs", "Intelligent Knowledge Graph", "Vector DB", "Analysis", "DX"]
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
        "tags": ["IA", "Desafíos enfrentados", "Tiempo Perdidos", "IoT", "Errores en cálculo manuales", "Decisiones para mejoras", "SmartFactory", "Manufacturing Intelligence", "LATAM", "Kⁱ⁰⁷ Platform", "DX"]
    },
    {
        "id": 33,
        "title": "전략AI | 생산 ROI 기준선 분석 AGENT",
        "desc": "보유 데이터 기반 문제 진단·시각화 및 실행 로드맵 제시",
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

def normalize_tags(tags):
    """태그 정규화 - 언더스코어를 공백으로, 소문자 변환"""
    return [tag.replace("_", " ").lower() for tag in tags]

def get_all_tags(projects):
    """모든 태그 추출 및 정규화"""
    all_tags = []
    for project in projects:
        all_tags.extend(normalize_tags(project["tags"]))
    return sorted(set(all_tags))

def get_category(title):
    """프로젝트 카테고리 추출"""
    if "전략AI" in title or "전략 AI" in title:
        return "전략 AI"
    elif "제조AI" in title or "제조 AI" in title:
        return "제조 AI"
    elif "농산업AI" in title:
        return "농산업 AI"
    else:
        return "기타"

def search_projects(projects, search_term, selected_categories, selected_tags):
    """프로젝트 검색 및 필터링"""
    filtered = projects
    
    if selected_categories:
        filtered = [p for p in filtered if get_category(p["title"]) in selected_categories]
    
    if selected_tags:
        filtered = [p for p in filtered if any(
            tag in normalize_tags(p["tags"]) for tag in selected_tags
        )]
    
    if search_term:
        search_term = search_term.lower()
        filtered = [p for p in filtered if 
            search_term in p["title"].lower() or 
            search_term in p["desc"].lower() or
            any(search_term in tag.lower() for tag in p["tags"])
        ]
    
    return filtered

def get_statistics(projects):
    """프로젝트 통계 계산"""
    categories = Counter([get_category(p["title"]) for p in projects])
    all_tags = []
    for p in projects:
        all_tags.extend(normalize_tags(p["tags"]))
    unique_tags = len(set(all_tags))
    
    return {
        "total": len(projects),
        "categories": categories,
        "unique_tags": unique_tags,
        "avg_tags": round(len(all_tags) / len(projects), 1)
    }

def render_header():
    st.markdown("""
    <div class="header-container">
        <div class="header-title">🌎 Kⁱ⁰⁷ <span font-family: 'Noto Sans KR', sans-serif;>AI 기반 가치 전환 전략</span></div>
        <div class="header-subtitle">
            데이터로 현장을 읽고, AI로 전략을 실행합니다.
        </div>
        <div class="header-tags">
            <span class="header-tag">✨ XAI · Ontology Systems</span>
            <span class="header-tag">🌐 IoT · Edge AI</span>
            <span class="header-tag">📊 Data Strategy</span>
            <span class="header-tag">🏭 Manufacturing DX</span>
        </div>
    </div>
    """, unsafe_allow_html=True)

def render_statistics(stats, filtered_count):
    st.markdown("""
    <div class="stats-container">
        <div class="stat-card">
            <div class="stat-number">{}</div>
            <div class="stat-label">총 프로젝트</div>
        </div>
        <div class="stat-card">
            <div class="stat-number">{}</div>
            <div class="stat-label">표시 중</div>
        </div>
        <div class="stat-card">
            <div class="stat-number">{}</div>
            <div class="stat-label">고유 기술</div>
        </div>
        <div class="stat-card">
            <div class="stat-number">{}</div>
            <div class="stat-label">평균 태그/프로젝트</div>
        </div>
    </div>
    """.format(stats["total"], filtered_count, stats["unique_tags"], stats["avg_tags"]), 
    unsafe_allow_html=True)

def render_project_card(project):
    """프로젝트 카드를 렌더링하거나 상세보기를 표시"""
    
    if st.session_state.get(f"show_modal_{project['id']}", False):
        render_project_detail(project)
        return True
    
    category = get_category(project["title"])
    category_colors = {
        "전략 AI": "#0066cc",
        "제조 AI": "#00cc99",
        "농산업 AI": "#ff9800",
        "기타": "#9c27b0"
    }
    
    with st.container():
        col_text, col_img = st.columns([2, 1])
        
        with col_text:
            st.markdown(f"""
            <div style="
                background: #1e1e1e;
                border-radius: 10px;
                padding: 1.2rem;
                box-shadow: 0 2px 8px rgba(0,0,0,0.3);
                height: 133px;
                border-left: 4px solid {category_colors[category]};
                border-bottom: 1px solid rgba(255,255,255,0.1);
            ">
                <div style="font-size: 1.1rem; font-weight: bold; margin-bottom: 0.5rem; color: #e0e0e0;">
                    {project['title']}
                </div>
                <div style="color: #b0b0b0; font-size: 0.9rem; margin-bottom: 0.8rem; line-height: 1.5;">
                    {project['desc']}
                </div>
            </div>
            """, unsafe_allow_html=True)
            
            
            st.markdown(f"""
            <div style="display: flex; flex-wrap: wrap; gap: 0.4rem; margin-top: 1.5rem;">
                {''.join([f'<span style="background: #e3f2fd; color: #0066cc; padding: 0.25rem 0.7rem; border-radius: 12px; font-size: 0.75rem; border: 1px solid #bbdefb;">{tag}</span>' for tag in project['tags'][:4]])}
            </div>
            """, unsafe_allow_html=True)

           
        
        with col_img:
            try:
                from PIL import Image
                import io
                import base64
                
                img = Image.open(project["img"])
                img_resized = img.resize((200, 133), Image.LANCZOS)
                
                buffered = io.BytesIO()
                img_resized.save(buffered, format="PNG")
                img_str = base64.b64encode(buffered.getvalue()).decode()
                
                st.markdown(f"""
                <img src="data:image/png;base64,{img_str}" 
                     style="width: 200px; 
                            height: 133px; 
                            object-fit: cover; 
                            border: 0.5px solid #0066cc; 
                            border-radius: 8px; 
                            box-shadow: 0 4px 10px rgba(0, 0, 0, 0.3); 
                            box-sizing: border-box; 
                            display: block;"
                     alt="프로젝트 썸네일">
                """, unsafe_allow_html=True)
            except:
                st.markdown(f"""
                <div style="width: 200px; height: 133px; background: linear-gradient(135deg, #e0e0e0 0%, #f5f5f5 100%); 
                     display: flex; align-items: center; justify-content: center; border-radius: 8px;">
                    <span style="color: #999; font-size: 0.8rem;">이미지 준비중</span>
                </div>
                """, unsafe_allow_html=True)

            if st.button("📄 Project Detail", key=f"view_{project['id']}", use_container_width=True):
                st.session_state[f"show_modal_{project['id']}"] = True
                st.rerun()      

    st.markdown("---")    
    return False


def render_project_detail(project):
    """프로젝트 상세보기 화면 렌더링 - 이중 스크롤 방식"""
    
    st.markdown(f"""
    <div style="background: linear-gradient(135deg, #005CFF 0%, #00C06F 100%); 
         padding: 2rem; border-radius: 10px; margin: 1rem 0 2rem 0; color: white;">
        <h1 style="margin: 0; color: white; font-size: 2rem;">📋 {project['title']}</h1>
        <p style="margin: 0.8rem 0 0 0; opacity: 0.9; font-size: 1.1rem;">{project['desc']}</p>
    </div>
    """, unsafe_allow_html=True)
    
    try:
        with open(project['url'], 'r', encoding='utf-8') as f:
            html_content = f.read()
        
        col1, col2, col3 = st.columns([3, 1, 1])
        
        with col1:
            st.info("💡 iframe 내부를 스크롤하여 문서를 확인하세요. 높이를 조절할 수 있습니다.")
        
        with col2:
            height_option = st.selectbox(
                "높이",
                ["보통 (800px)", "크게 (1200px)", "매우 크게 (1800px)"],
                key=f"height_{project['id']}",
                label_visibility="collapsed"
            )
        
        with col3:
            if st.button("🏠 Home", key=f"home_top_{project['id']}", use_container_width=True):
                st.session_state[f"show_modal_{project['id']}"] = False
                st.rerun()
        
        if height_option == "보통 (800px)":
            iframe_height = 800
        elif height_option == "크게 (1200px)":
            iframe_height = 1200
        else:  
            iframe_height = 1800
        
        if '<html' in html_content.lower() or '<body' in html_content.lower():
            if '<head>' in html_content:
                modified_html = html_content.replace(
                    '<head>',
                    '<head><meta name="viewport" content="width=device-width, initial-scale=1.0">'
                )
            else:
                modified_html = html_content
        else:
            modified_html = f"""
            <!DOCTYPE html>
            <html>
            <head>
                <meta charset="UTF-8">
                <meta name="viewport" content="width=device-width, initial-scale=1.0">
                <style>
                    body {{
                        margin: 0;
                        padding: 20px;
                        width: 100%;
                        max-width: 100%;
                        box-sizing: border-box;
                        overflow-x: hidden;
                    }}
                </style>
            </head>
            <body>
                {html_content}
            </body>
            </html>
            """
        
        components.html(modified_html, height=iframe_height, scrolling=True)
        
    except Exception as e:
        st.error(f"❌ 파일을 불러올 수 없습니다: {project['url']}")
        st.info(f"💡 파일 경로를 확인해주세요. 에러: {str(e)}")
    
    st.markdown("---")
    
    col1, col2, col3 = st.columns([1, 1, 1])
    
    
    with col2:
        if st.button("🏠 홈으로 가기", key=f"close_{project['id']}", use_container_width=True, type="primary"):
            st.session_state[f"show_modal_{project['id']}"] = False
            st.rerun()
    

# ================================================================
# 
# ================================================================
def main():

    render_header()
    
    stats = get_statistics(projects)
    
    with st.sidebar:
        
        st.title("🔍 Kⁱ⁰⁷ AI AGENT")
        
        search_term = st.text_input("🔎 검색", placeholder="프로젝트명, 설명, 태그...")
        
        st.markdown("---")
        
        st.subheader("📁 카테고리")
        categories = ["전략 AI", "제조 AI", "농산업 AI"]
        selected_categories = []
        for cat in categories:
            if st.checkbox(f"{cat} ({stats['categories'][cat]})", key=f"cat_{cat}"):
                selected_categories.append(cat)
        
        st.markdown("---")
        
        st.subheader("🏷️ 기술 태그")
        all_tags = get_all_tags(projects)
        
        tag_counter = Counter()
        for p in projects:
            tag_counter.update(normalize_tags(p["tags"]))
        popular_tags = [tag for tag, count in tag_counter.most_common(10)]
        
        selected_tags = st.multiselect(
            "기술 선택 (인기 태그)",
            options=popular_tags,
            placeholder="태그를 선택하세요..."
        )
        
        st.markdown("---")
        
        sort_option = st.selectbox(
            "🔀 정렬",
            ["오래된순", "최신순", "이름순"]
        )
        
        if st.button("🔄 필터 초기화", use_container_width=True):
            st.rerun()

        st.markdown("---")
        st.markdown("## 📊 포트폴리오 통계")
        render_statistics(stats, stats['total'])
    
    filtered_projects = search_projects(projects, search_term, selected_categories, selected_tags)
    
    if sort_option == "오래된순":
        filtered_projects = sorted(filtered_projects, key=lambda x: x["id"])
    elif sort_option == "이름순":
        filtered_projects = sorted(filtered_projects, key=lambda x: x["title"])
    else:  
        filtered_projects = sorted(filtered_projects, key=lambda x: x["id"], reverse=True)
    
    if search_term or selected_categories or selected_tags:
        st.markdown(f"""
        <div class="search-result-count">
            🔍 <strong>{len(filtered_projects)}개</strong>의 프로젝트를 찾았습니다.
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown("""
    <h2 style="background-color: rgba(255, 255, 255, 0.05); font-weight: 800;color: rgba(0, 255, 0, 0.7);margin-bottom: 1rem; padding: 0.8rem; border-radius: 8px;">
                📂 Project List</h2>
    """, unsafe_allow_html=True)
    
    if not filtered_projects:
        st.warning("⚠️ 검색 조건에 맞는 프로젝트가 없습니다. 필터를 조정해보세요.")
    else:

        for project in filtered_projects:
            if st.session_state.get(f"reopen_modal_{project['id']}", False):
                st.session_state[f"show_modal_{project['id']}"] = True
                st.session_state[f"reopen_modal_{project['id']}"] = False
                break
        
        show_detail = False
        for project in filtered_projects:
            if st.session_state.get(f"show_modal_{project['id']}", False):
                show_detail = True
                render_project_card(project)
                break
        
        if not show_detail:
            for i in range(0, len(filtered_projects), 2):
                col1, col2 = st.columns(2, gap="large")
                
                with col1:
                    render_project_card(filtered_projects[i])
                
                if i + 1 < len(filtered_projects):
                    with col2:
                        render_project_card(filtered_projects[i + 1])
                
                st.markdown("<br>", unsafe_allow_html=True)
    
    st.markdown("---")
    st.markdown("""
        <div style="text-align: center; color: #6b7280; padding: 2rem;">
            <p style="font-size: 1.2rem;">Kⁱ⁰⁷ 데이터 기반 가치 전환 전략</p>
            This work is based on my personal field analysis of data-driven value transformation strategies.<br>
            © 2023-2025 Data-driven VX Strategist | powered by Kⁱ⁰⁷ Ken KIM| 📧 <a href='mailto:io7hub@naver.com' style='text-decoration: none;'>io7hub@naver.com</a><br></p>   
        </div>
    """, unsafe_allow_html=True)     

if __name__ == "__main__":
    main()
