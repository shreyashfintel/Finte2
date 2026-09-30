import pandas as pd

df = pd.read_csv('NIFTY_FINANCIAL_PROCESSED.csv')

print("\n" + "="*50)
print("    NIFTY FINANCIAL SERVICES - BASIC SUMMARY")
print("="*50)
print(f"Total Trading Days       : {len(df)}")
print(f"Highest Closing Price    : ₹{df['Close'].max():.2f}")
print(f"Lowest Closing Price     : ₹{df['Close'].min():.2f}")
print(f"Average Closing Price    : ₹{df['Close'].mean():.2f}")
print(f"Highest 1-Day Turnover   : ₹{df['Turnover (₹ Cr)'].max():.2f} Cr")
print("="*50 + "\n")