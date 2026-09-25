import pandas as pd
import matplotlib.pyplot as plt

# 1. Load the enriched data
df = pd.read_csv('NIFTY_OIL_GAS_Enriched.csv')
df['Date'] = pd.to_datetime(df['Date'])

# 2. CALCULATE SMA_20 ON THE FLY
# This looks at the 'Close' price, takes a 20-day rolling window, and finds the mean (average)
df['SMA_20'] = df['Close'].rolling(window=20).mean()

# 3. Set up the visualization
plt.figure(figsize=(12, 6))

# 4. Plot the actual Closing Prices (thinner line)
plt.plot(df['Date'], df['Close'], label='Actual Closing Price', color='blue', alpha=0.6, linewidth=1.5)

# 5. Plot the 20-Day Moving Average (thicker, contrasting line)
plt.plot(df['Date'], df['SMA_20'], label='20-Day Moving Average (SMA)', color='orange', linewidth=2.5)

# 6. Chart Formatting
plt.title('NIFTY Oil & Gas - Closing Price vs. 20-Day Moving Average', fontsize=14, fontweight='bold')
plt.xlabel('Date', fontsize=12)
plt.ylabel('Price (₹)', fontsize=12)
plt.legend(loc='best')
plt.grid(True, linestyle='--', alpha=0.5)
plt.xticks(rotation=45)
plt.tight_layout()

# 7. Show the graph
plt.show()
