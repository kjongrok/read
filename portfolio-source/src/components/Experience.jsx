import { journey } from '../data/portfolio'

/** 프로젝트 경험이 확장된 과정을 세 단계로 설명합니다. */
function Experience() {
  return (
    <section className="section journey-section" id="journey">
      <div className="section-heading">
        <span className="section-number">03</span>
        <div><p className="section-kicker">GROWTH JOURNEY</p><h2>배운 기술을<br/>다음 문제에 적용했습니다.</h2></div>
      </div>
      <div className="journey-list">
        {journey.map((item) => <article key={item.phase}><span>{item.phase}</span><div><h3>{item.title}</h3><p>{item.text}</p></div></article>)}
      </div>
    </section>
  )
}

export default Experience
