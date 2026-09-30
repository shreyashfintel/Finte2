import pandas as pd
import matplotlib.pyplot as plt

# 1. Processed CSV data load karo
df = pd.read_csv('NIFTY_CEMENT_PROCESSED.csv')
df['Date'] = pd.to_datetime(df['Date'])

# --- Plot 1: 6 Month Closing Price Trend ---
plt.figure(figsize=(12, 6))
plt.plot(df['Date'], df['Close'], marker='o', linestyle='-', color='blue', markersize=3)
plt.title('NIFTY Cement - 6 Month Closing Price Trend')
plt.xlabel('Date')
plt.ylabel('Closing Price (₹)')
plt.grid(True)
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig('Figure_1_Cement_Trend.png')  # Ye Plot 1 save karega
plt.close()

# --- Plot 2: Closing Price vs. 20-Day Moving Average ---
plt.figure(figsize=(12, 6))
plt.plot(df['Date'], df['Close'], label='Actual Closing Price', color='purple')
plt.plot(df['Date'], df['SMA_20'], label='20-Day Moving Average (SMA)', color='orange')
plt.title('NIFTY Cement - Closing Price vs. 20-Day Moving Average')
plt.xlabel('Date')
plt.ylabel('Price (₹)')
plt.legend()
plt.grid(True)
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig('Figure_2_Cement_Moving_Avg.png')  # Ye Plot 2 save karega
plt.close()

print("Dono graphs successfully generate aur save ho gaye hain!")