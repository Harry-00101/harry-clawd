# Remotion Integration

Make videos programmatically with React - 34k stars!

## What is Remotion?

Framework for creating videos using React:
- Write React code → Render video
- Full React ecosystem support
- Timeline-based editing
- Component-based video design
- By Jina AI team

## Features

| Feature | Description |
|---------|-------------|
| **React-based** | Use React components for video |
| **Timeline** | Frame-by-frame control |
| **Composition** | Combine video parts |
| **Animation** | Smooth transitions |
| **Rendering** | Export to MP4/WebM |
| **Streaming** | Real-time preview |

## Use Cases

- **Stock Reports** - Automated market updates
- **Social Media** - Auto-generated content
- **Data Viz** - Charts in video form
- **Tutorials** - Code-generated walkthroughs
- **Presentations** - Programmatic slides

## Installation

```bash
# Via npm
npm init remotion@latest

# Or add to existing project
npm install @remotion/react @remotion/player
```

## Example: Stock Report Video

```tsx
import { useVideoConfig, useCurrentFrame } from 'remotion';

const StockReport = ({ ticker, price, change }) => {
  const frame = useCurrentFrame();
  
  return (
    <div style={{ background: 'black', color: 'white' }}>
      <h1>{ticker}</h1>
      <h2>${price}</h2>
      <h3 style={{ color: change > 0 ? 'green' : 'red' }}>
        {change > 0 ? '▲' : '▼'} {change}%
      </h3>
      
      {/* Animate chart */}
      <Chart data={chartData} frame={frame} />
    </div>
  );
};
```

## For Harry-001

Create automated video reports:
1. **Stock Analysis Videos** - VOO daily recap
2. **Market Updates** - Automated news videos
3. **Data Visualization** - Charts in motion
4. **Social Content** - Auto-generated posts

## Architecture

```
React Components (Video Parts)
        ↓
Remotion Engine
        ↓
FFmpeg Rendering
        ↓
MP4/WebM Output
```

## References

- https://github.com/remotion-dev/remotion
- https://remotion.dev (docs)
- Made by Jina AI team
