import Header from './components/Header'
import Hero from './components/Hero'
import About from './components/About'
import Projects from './components/Projects'
import Experience from './components/Experience'
import Contact from './components/Contact'
import './styles/portfolio.css'

/** 포트폴리오의 주요 섹션을 순서대로 조합해 단일 페이지를 구성합니다. */
function App() {
  return (
    <div className="site-shell">
      <Header />
      <main>
        <Hero />
        <About />
        <Projects />
        <Experience />
        <Contact />
      </main>
    </div>
  )
}

export default App
