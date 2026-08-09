/** 이미지가 없는 프로젝트에 기능 성격을 보여주는 코드형 시각 요소를 표시합니다. */
function ProjectVisual({ type }) {
  if (type === 'traffic') {
    return <div className="generated-visual traffic-visual"><div className="road-line"/><span className="vehicle v1"/><span className="vehicle v2"/><span className="vehicle v3"/><div className="scan-line"/><div className="visual-caption"><b>LIVE</b> VISION → DATA → LLM</div></div>
  }

  return <div className="generated-visual vision-visual"><div className="camera-frame"><span className="box b1">CAR 0.94</span><span className="box b2">TRUCK 0.87</span><span className="box b3">BUS 0.91</span></div><div className="signal-chart"><i/><i/><i/><i/><i/><i/></div><div className="visual-caption"><b>ANOMALY</b> DETECTION PIPELINE</div></div>
}

export default ProjectVisual
