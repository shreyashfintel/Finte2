import pandas as pd
from ta import add_all_ta_features

df = pd.read_csv("NIFTY OIL & GAS-25-03-2026-to-25-09-2026.csv")
df.columns = df.columns.str.strip()
df = add_all_ta_features(
    df, open="Open", high="High", low="Low", close="Close", volume="Volume", fillna=True
)

df.to_csv("NIFTY_OIL_GAS_PROCESSED11.csv", index=False)
print("Done! Processed file saved.")