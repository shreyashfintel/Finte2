import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('NIFTY_OIL_GAS_PROCESSED.csv')
df['Date'] = pd.to_datetime(df['Date'])

# Plot 1: Trend
plt.figure(figsize=(12, 6))
plt.plot(df['Date'], df['Close'], marker='o', linestyle='-', color='blue', markersize=3)
plt.title('NIFTY Oil & Gas - 6 Month Closing Price Trend')
plt.xlabel('Date')
plt.ylabel('Closing Price (₹)')
plt.grid(True)
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig('Figure_1_Oil_Gas_Trend.png')
plt.close()

# Plot 2: Moving Average
plt.figure(figsize=(12, 6))
plt.plot(df['Date'], df['Close'], label='Actual Closing Price', color='purple')
plt.plot(df['Date'], df['SMA_20'], label='20-Day Moving Average (SMA)', color='orange')
plt.title('NIFTY Oil & Gas - Closing Price vs. 20-Day Moving Average')
plt.xlabel('Date')
plt.ylabel('Price (₹)')
plt.legend()
plt.grid(True)
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig('Figure_2_Oil_Gas_Moving_Avg.png')
plt.close()

print("Oil & Gas graphs successfully generated!")