import Icon from './Icon'
import { impactMetrics, profile } from '../data/portfolio'

/** 개발자 소개와 핵심 경험 지표를 첫 화면에 표시합니다. */
function Hero() {
  return (
    <section className="hero-section" id="top">
      <div className="hero-grid">
        <div className="hero-copy">
          <p className="eyebrow"><span/> BACKEND · AI APPLICATION</p>
          <h1>기술을 연결해<br/><em>쓸 수 있는 서비스</em>로<br/>만듭니다.</h1>
          <p className="hero-summary">{profile.summary}</p>
          <div className="hero-actions">
            <a className="button primary" href="#projects">프로젝트 보기 <Icon name="arrow"/></a>
            <a className="button ghost" href={profile.github} target="_blank" rel="noreferrer"><Icon name="github"/> GitHub</a>
          </div>
        </div>
        <div className="hero-visual" aria-label="백엔드와 AI 서비스 연결을 표현한 장식">
          <div className="visual-grid"/>
          <div className="orbit orbit-one"><span>API</span></div>
          <div className="orbit orbit-two"><span>AI</span></div>
          <div className="core-card">
            <span className="core-label">CURRENT FOCUS</span>
            <strong>Backend<br/>& AI</strong>
            <div className="core-status"><i/> Building reliable flows</div>
          </div>
          <div className="code-chip chip-one">Spring Boot</div>
          <div className="code-chip chip-two">FastAPI</div>
          <div className="code-chip chip-three">React</div>
        </div>
      </div>
      <div className="impact-row">
        {impactMetrics.map((metric) => <div className="impact-item" key={metric.label}><strong>{metric.value}</strong><span>{metric.label}</span></div>)}
      </div>
    </section>
  )
}

export default Hero
