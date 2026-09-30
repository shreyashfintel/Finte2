import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('NIFTY_OIL_GAS_PROCESSED.csv')

df.columns = df.columns.str.strip()


for col in df.columns:
    if 'date' in col.lower():
        df[col] = pd.to_datetime(df[col])
        df = df.sort_values(by=col)
        date_col = col
        break

plt.figure(figsize=(12, 6))
plt.plot(df[date_col], df['Close'], label='Close Price', color='blue', linewidth=1.5)
plt.plot(df[date_col], df['EMA_20'], label='EMA 20', color='orange', linestyle='--', linewidth=1.5)

plt.title('NIFTY OIL & GAS - Close Price & EMA 20', fontsize=14)
plt.xlabel('Date', fontsize=12)
plt.ylabel('Price', fontsize=12)
plt.legend()
plt.grid(True)
plt.tight_layout()

plt.show()