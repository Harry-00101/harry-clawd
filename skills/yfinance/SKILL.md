# yfinance Integration

Free stock data from Yahoo Finance.

## What

Python library for downloading market data from Yahoo Finance.
- 10k+ stars
- Completely free
- No API key needed

## Installation

```bash
pip install yfinance
```

## Usage

```python
import yfinance as yf

# Get stock data
stock = yf.Ticker("VOO")
history = stock.history(period="1y")
info = stock.info

# Get multiple stocks
data = yf.download("VOO SPY QQQ", period="1mo")
```

## For Harry-001

Use for:
- Daily price updates
- Historical data for charts
- Financial statements
- Analyst recommendations
- Earnings calendar

## Example: VOO Daily Analysis

```python
import yfinance as yf

voo = yf.Ticker("VOO")
hist = voo.history(period="1y")
info = voo.info

print(f"Price: ${info.get('currentPrice', 'N/A')}")
print(f"P/E: {info.get('trailingPE', 'N/A')}")
print(f"Market Cap: {info.get('marketCap', 'N/A')}")
print(f"52W High: ${info.get('fiftyTwoWeekHigh', 'N/A')}")
print(f"52W Low: ${info.get('fiftyTwoWeekLow', 'N/A')}")
```

## References

- https://github.com/ranaroussi/yfinance
- https://pypi.org/project/yfinance/
