# Firecrawl Integration Skill

Web scraping API for AI - Turn websites into LLM-ready markdown.

## Features
- Scrape any website to markdown
- Support 100+ languages
- LLM-ready output
- 78.7k stars on GitHub

## Setup
```bash
python3 -m venv venv
source venv/bin/activate
pip install firecrawl-py
```

## API Usage
```python
from firecrawl import FirecrawlApp

app = FirecrawlApp(api_key='your-key')
result = app.scrape('https://example.com', formats=['markdown'])
```

## For Harry-001
- Stock news scraping
- Market research automation
- Financial data extraction
