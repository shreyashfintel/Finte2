import pandas as pd
import matplotlib.pyplot as plt

# 1. Load the dataset
file_path = 'NIFTY OIL & GAS-25-03-2026-to-25-09-2026.csv'
df = pd.read_csv(file_path)

# 2. Clean the data
# Forcefully rename all columns to clean, exact names
df.columns = ['Date', 'Open', 'High', 'Low', 'Close', 'Shares Traded', 'Turnover']

# Convert the 'Date' column to actual datetime objects for proper time-series plotting
df['Date'] = pd.to_datetime(df['Date'])

# Sort the data chronologically (oldest to newest)
df = df.sort_values('Date')

# 3. Basic Analysis
print("--- NIFTY Oil & Gas Data Summary ---")
print(f"Total Trading Days: {df.shape[0]}")
print(f"Average Closing Price: ₹{df['Close'].mean():.2f}")
print(f"Highest Close: ₹{df['Close'].max():.2f}")
print(f"Lowest Close: ₹{df['Close'].min():.2f}")
print("-" * 36)

# 4. Visualization (Closing Price Trend)
plt.figure(figsize=(12, 6))
plt.plot(df['Date'], df['Close'], marker='o', linestyle='-', color='b', markersize=4)

plt.title('NIFTY Oil & Gas - 6 Month Closing Price Trend', fontsize=14)
plt.xlabel('Date', fontsize=12)
plt.ylabel('Closing Price (₹)', fontsize=12)
plt.grid(True, linestyle='--', alpha=0.7)
plt.xticks(rotation=45)
plt.tight_layout()

# Show the plot
plt.show()