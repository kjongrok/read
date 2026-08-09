import { useState } from 'react'
import Icon from './Icon'

const navigation = [
  { label: '소개', href: '#about' },
  { label: '프로젝트', href: '#projects' },
  { label: '성장 과정', href: '#journey' },
  { label: '연락처', href: '#contact' },
]

/** 데스크톱과 모바일에서 사용할 상단 탐색 메뉴를 제공합니다. */
function Header() {
  const [open, setOpen] = useState(false)

  /** 선택한 섹션으로 이동한 뒤 모바일 메뉴를 닫습니다. */
  const handleNavigate = () => setOpen(false)

  return (
    <header className="site-header">
      <div className="header-inner">
        <a className="brand" href="#top" aria-label="김종록 포트폴리오 첫 화면">
          <span className="brand-mark">KJ</span>
          <span className="brand-text">김종록<span>.portfolio</span></span>
        </a>
        <nav className={open ? 'nav-links open' : 'nav-links'} aria-label="주요 메뉴">
          {navigation.map((item) => <a key={item.href} href={item.href} onClick={handleNavigate}>{item.label}</a>)}
          <a className="nav-github" href="https://github.com/kjongrok" target="_blank" rel="noreferrer"><Icon name="github" size={18}/> GitHub</a>
        </nav>
        <button className="menu-button" type="button" onClick={() => setOpen((current) => !current)} aria-label={open ? '메뉴 닫기' : '메뉴 열기'}>
          <Icon name={open ? 'close' : 'menu'} />
        </button>
      </div>
    </header>
  )
}

export default Header
