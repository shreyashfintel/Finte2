import pandas as pd
import ta

file_path = '/home/shreyash-mhatre/fintel/shreyashgit/System monitoring/data/NIFTY OIL & GAS-25-03-2026-to-25-09-2026.csv'
df = pd.read_csv(file_path)

df.columns = df.columns.str.strip()

for col in df.columns:
    if 'date' in col.lower():
        df[col] = pd.to_datetime(df[col])
        break
    
df['Daily_Return'] = df['Close'].pct_change() * 100

macd_indicator = ta.trend.MACD(close=df['Close'])
df['MACD'] = macd_indicator.macd()
df['MACD_Signal'] = macd_indicator.macd_signal()
df['MACD_Diff'] = macd_indicator.macd_diff()

atr_indicator = ta.volatility.AverageTrueRange(high=df['High'], low=df['Low'], close=df['Close'], window=14)
df['ATR'] = atr_indicator.average_true_range()

cci_indicator = ta.trend.CCIIndicator(high=df['High'], low=df['Low'], close=df['Close'], window=20)
df['CCI'] = cci_indicator.cci()

df['EMA_20'] = df['Close'].ewm(span=20, adjust=False).mean()

output_path = '/home/shreyash-mhatre/fintel/shreyashgit/System monitoring/data/NIFTY_OIL_GAS_PROCESSED.csv'
df.to_csv(output_path, index=False)

print("Technical indicators are successfully added.")

print(df.tail(3))