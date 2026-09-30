import pandas as pd

# Sirf processed/enriched data load karo
file_path = 'NIFTY_OIL_GAS_PROCESSED.csv'
df = pd.read_csv(file_path)

print("\n" + "="*50)
print("      NIFTY OIL & GAS - BASIC SUMMARY")
print("="*50)
print(f"Total Trading Days       : {len(df)}")
print(f"Highest Closing Price    : ₹{df['Close'].max():.2f}")
print(f"Lowest Closing Price     : ₹{df['Close'].min():.2f}")
print(f"Average Closing Price    : ₹{df['Close'].mean():.2f}")
print("="*50 + "\n")