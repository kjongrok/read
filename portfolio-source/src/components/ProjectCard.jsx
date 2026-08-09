import { useState } from 'react'
import Icon from './Icon'
import ProjectVisual from './ProjectVisual'

/** 프로젝트 요약과 상세 기여·문제 해결 내용을 확장형 카드로 보여줍니다. */
function ProjectCard({ project }) {
  const [expanded, setExpanded] = useState(project.featured)
  const imageClass = project.visual === 'image-contain' ? 'project-image contain' : 'project-image'

  return (
    <article className={`project-card tone-${project.tone} ${project.featured ? 'featured' : ''}`}>
      <div className="project-topline"><span>PROJECT {project.index}</span><span>{project.period}</span></div>
      <div className="project-layout">
        <div className="project-media">
          {project.video ? (
            <video className="project-video" src={project.video} poster={project.image} autoPlay muted loop playsInline aria-label={`${project.title} 핵심 기능 미리보기`} />
          ) : project.image ? (
            <img className={imageClass} src={project.image} alt={`${project.title} 대표 화면`}/>
          ) : (
            <ProjectVisual type={project.visual}/>
          )}
          <span className="project-role">{project.role}</span>
        </div>
        <div className="project-info">
          <p className="project-subtitle">{project.subtitle}</p>
          <h3>{project.title}</h3>
          <p className="project-description">{project.description}</p>
          <div className="tag-list">{project.tags.map((tag) => <span key={tag}>{tag}</span>)}</div>
          <div className="project-links">
            {project.links.map((link) => <a key={link.label} href={link.url} target="_blank" rel="noreferrer">{link.label} <Icon name="external" size={15}/></a>)}
            <button type="button" onClick={() => setExpanded((current) => !current)} aria-expanded={expanded}>{expanded ? '상세 닫기' : '기여 내용 보기'} <span>{expanded ? '−' : '+'}</span></button>
          </div>
        </div>
      </div>
      {expanded && (
        <div className="project-detail">
          <div><h4>주요 기여</h4><ul>{project.contributions.map((item) => <li key={item}><Icon name="check" size={17}/><span>{item}</span></li>)}</ul></div>
          <div className="detail-notes"><div><span>PROBLEM SOLVING</span><p>{project.challenge}</p></div><div><span>RESULT</span><p>{project.outcome}</p></div></div>
        </div>
      )}
    </article>
  )
}

export default ProjectCard
