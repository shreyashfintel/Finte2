import pandas as pd

# Processed Nifty Cement data load kar rahe hain
df = pd.read_csv('NIFTY_CEMENT_PROCESSED.csv')

print("\n" + "="*45)
print("       NIFTY CEMENT - BASIC SUMMARY")
print("="*45)
print(f"Total Trading Days       : {len(df)}")
print(f"Highest Closing Price    : ₹{df['Close'].max():.2f}")
print(f"Lowest Closing Price     : ₹{df['Close'].min():.2f}")
print(f"Average Closing Price    : ₹{df['Close'].mean():.2f}")
print(f"Highest 1-Day Turnover   : ₹{df['Turnover (₹ Cr)'].max():.2f} Cr")
print("="*45 + "\n")