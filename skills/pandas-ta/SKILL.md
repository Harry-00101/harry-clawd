# pandas-ta Integration

Technical analysis library - 5k+ stars.

## What

Pandas Technical Analysis - 100+ indicators.

## Installation

```bash
pip install pandas-ta
```

## Usage

```python
import pandas as pd
import pandas_ta as ta

# Load data
df = pd.read_csv('voo.csv')

# Add all indicators
df.ta.strategy("All")

# Or specific indicators
df['SMA20'] = ta.sma(df['Close'], length=20)
df['EMA50'] = ta.ema(df['Close'], length=50)
df['RSI'] = ta.rsi(df['Close'], length=14)
df['MACD'] = ta.macd(df['Close'])['MACD_12_26_9']
df['BB'] = ta.bbands(df['Close'], length=20)

print(df[['Close', 'SMA20', 'EMA50', 'RSI', 'MACD']].tail())
```

## Indicators Available

- **Trend**: SMA, EMA, ADX, Ichimoku
- **Momentum**: RSI, MACD, Stochastic
- **Volatility**: Bollinger Bands, ATR
- **Volume**: OBV, VWAP, ADI

## For Harry-001

Use for:
- Technical analysis of VOO
- Buy/sell signals
- Support/resistance levels
- Trend confirmation
