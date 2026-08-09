import ProjectCard from './ProjectCard'
import { projects } from '../data/portfolio'

/** 완성도와 최근 작업 순서에 따라 프로젝트 목록을 배치합니다. */
function Projects() {
  return (
    <section className="section projects-section" id="projects">
      <div className="section-heading compact">
        <span className="section-number">02</span>
        <div><p className="section-kicker">SELECTED WORK</p><h2>프로젝트</h2></div>
        <p className="heading-note">서비스 구현에서 시작해 ML·DL·LLM을 거쳐, 백엔드와 AI가 결합된 제품으로 발전했습니다.</p>
      </div>
      <div className="project-list">{projects.map((project) => <ProjectCard key={project.id} project={project}/>)}</div>
    </section>
  )
}

export default Projects
