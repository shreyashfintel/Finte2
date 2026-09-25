import pandas as pd
import matplotlib.pyplot as plt

# 1. Load the dataset
file_path = 'NIFTY OIL & GAS-25-03-2026-to-25-09-2026.csv'
df = pd.read_csv(file_path)

# 2. Clean the data
# Forcefully rename columns to prevent KeyErrors
df.columns = ['Date', 'Open', 'High', 'Low', 'Close', 'Shares Traded', 'Turnover']
df['Date'] = pd.to_datetime(df['Date'], format='%d-%b-%Y')
df = df.sort_values('Date')

# 3. Print Data Summary
print("--- NIFTY Oil & Gas Data Summary ---")
print(f"Total Trading Days: {len(df)}")
print(f"Average Closing Price: ₹{df['Close'].mean():.2f}")
print(f"Highest Close: ₹{df['Close'].max():.2f}")
print(f"Lowest Close: ₹{df['Close'].min():.2f}")
print("------------------------------------")

# 4. Plot the 6-Month Trend
plt.figure(figsize=(12, 6))
plt.plot(df['Date'], df['Close'], color='blue', linewidth=2)

# Chart Formatting
plt.title('NIFTY Oil & Gas - 6 Month Closing Price Trend', fontsize=14, fontweight='bold')
plt.xlabel('Date', fontsize=12)
plt.ylabel('Closing Price (₹)', fontsize=12)
plt.grid(True, linestyle='--', alpha=0.6)
plt.xticks(rotation=45)
plt.tight_layout()

# Show the interactive chart
plt.show()