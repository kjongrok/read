import { skillGroups } from '../data/portfolio'

/** 개발 방향과 실제 사용 기술을 간결하게 소개합니다. */
function About() {
  return (
    <section className="section about-section" id="about">
      <div className="section-heading">
        <span className="section-number">01</span>
        <div><p className="section-kicker">ABOUT</p><h2>문제를 이해하고,<br/>끝까지 연결합니다.</h2></div>
      </div>
      <div className="about-content">
        <div className="about-statement">
          <p>기능 하나를 만드는 데서 멈추지 않고, 사용자 화면부터 API·데이터·AI 처리와 실패 대응까지 이어지는 전체 흐름을 고민합니다.</p>
          <p>두 달 동안 정형데이터 머신러닝, 영상 딥러닝, LLM 에이전트와 공공입찰 서비스를 차례로 구현하며 기술을 실제 서비스에 적용하는 경험을 쌓았습니다.</p>
        </div>
        <div className="skill-board">
          {skillGroups.map((group) => (
            <article className="skill-group" key={group.label}>
              <h3>{group.label}</h3>
              <div>{group.skills.map((skill) => <span key={skill}>{skill}</span>)}</div>
            </article>
          ))}
        </div>
      </div>
    </section>
  )
}

export default About
