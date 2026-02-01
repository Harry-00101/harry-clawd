# PaddleOCR Integration

World's most popular OCR toolkit (60k+ stars).

## What is PaddleOCR?

From Baidu's PaddlePaddle platform:
- **PDF/Image to structured data** (JSON, Markdown)
- **100+ languages** support
- **Real-world document parsing** (skew, warping, scanning)
- **MCP server** for agent integration

## Key Models

| Model | Purpose |
|-------|---------|
| **PaddleOCR-VL-1.5** | Document parsing (0.9B VLM) |
| **PP-OCRv5** | Scene text recognition |
| **PP-StructureV3** | PDF to Markdown/JSON |
| **PP-ChatOCRv4** | Intelligent info extraction |

## Installation

```bash
# Python pip
pip install paddlepaddle paddleocr

# Or with pip for CPU
pip install paddlepaddle==3.0.0b1 paddleocr

# Docker
docker pull paddlepaddle/paddleocr
```

## Usage

```python
from paddleocr import PaddleOCR

# Initialize
ocr = PaddleOCR(use_angle_cls=True, lang='en')

# Extract text from image
result = ocr.img_cv2('image.jpg')

# PDF to text
from paddleocr import PaddleOCR
ocr = PaddleOCR(lang='ch')
result = ocr.ocr('document.pdf')
```

## MCP Server Integration

PaddleOCR has MCP server for agent integration!

```bash
# Install MCP server
pip install paddleocr-mcp

# Configure in agent
{
  "mcpServers": {
    "paddleocr": {
      "command": "paddleocr-mcp",
      "args": ["--port", "7860"]
    }
  }
}
```

## For Harry-001

Perfect for:
1. **Stock chart OCR** - Extract data from charts
2. **Financial documents** - Parse PDFs, annual reports
3. **News image extraction** - Text from images
4. **Document parsing** - Tables, charts, formulas

## Example: Extract from Stock Chart

```python
from paddleocr import PaddleOCR

ocr = PaddleOCR(lang='en')
result = ocr.img_cv2('voo-chart.png')

# Get text
for line in result:
    print(line[1][0])
```

## References

- https://github.com/PaddlePaddle/PaddleOCR
- https://www.paddleocr.com (official website)
- https://paddlepaddle.org.cn (PaddlePaddle)
- MCP Server: https://paddlepaddle.github.io/PaddleOCR/latest/en/version3.x/deployment/mcp_server.html
