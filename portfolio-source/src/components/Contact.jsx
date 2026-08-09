import Icon from './Icon'
import { profile } from '../data/portfolio'

/** GitHub와 프로젝트 탐색으로 이어지는 마지막 연락 섹션을 표시합니다. */
function Contact() {
  return (
    <footer className="contact-section" id="contact">
      <div className="contact-orbit" aria-hidden="true"/>
      <p className="section-kicker">LET'S BUILD SOMETHING USEFUL</p>
      <h2>함께 해결할 문제가 있다면<br/><em>이야기를 나누고 싶습니다.</em></h2>
      <a className="button primary large" href={profile.github} target="_blank" rel="noreferrer"><Icon name="github"/> GitHub에서 더 보기 <Icon name="arrow"/></a>
      <div className="footer-bottom"><span>© 2026 {profile.name}</span><span>Designed & built with React</span></div>
    </footer>
  )
}

export default Contact
