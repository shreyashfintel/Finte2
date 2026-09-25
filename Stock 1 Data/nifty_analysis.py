import pandas as pd
import matplotlib.pyplot as plt
import ta

# 1. Load the dataset
file_path = 'NIFTY OIL & GAS-25-03-2026-to-25-09-2026.csv'
df = pd.read_csv(file_path)

# 2. Clean the data
df.columns = ['Date', 'Open', 'High', 'Low', 'Close', 'Shares Traded', 'Turnover']
df['Date'] = pd.to_datetime(df['Date'], format='%d-%b-%Y')
df = df.sort_values('Date')

print("Calculating technical indicators...")

# 3. FEATURE ENGINEERING: Calculate the Indicators
# A. Day-over-Day Return (%)
df['DoD_Return_%'] = df['Close'].pct_change() * 100

# B. ATR (Average True Range) - Measures Volatility
df['ATR_14'] = ta.volatility.AverageTrueRange(
    high=df['High'], low=df['Low'], close=df['Close'], window=14
).average_true_range()

# C. MACD (Moving Average Convergence Divergence) - Measures Trend Direction
macd = ta.trend.MACD(close=df['Close'], window_slow=26, window_fast=12, window_sign=9)
df['MACD'] = macd.macd()
df['MACD_Signal'] = macd.macd_signal()

# D. CCI (Commodity Channel Index) - Identifies Overbought/Oversold conditions
df['CCI_20'] = ta.trend.CCIIndicator(
    high=df['High'], low=df['Low'], close=df['Close'], window=20
).cci()

# 4. Save and Display the Results
# Drop the first few rows because 14-day and 26-day indicators need time to "warm up"
df = df.dropna()

output_file = 'NIFTY_OIL_GAS_Enriched.csv'
df.to_csv(output_file, index=False)

print(f"\nSUCCESS! Enriched data saved to: {output_file}")
print("\nHere are the most recent 5 days of your technical analysis:")
# Display only the relevant columns to keep the terminal clean
print(df[['Date', 'Close', 'DoD_Return_%', 'ATR_14', 'MACD', 'CCI_20']].tail())