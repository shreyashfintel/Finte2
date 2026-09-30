import pandas as pd
import numpy as np

def load_and_clean_data(file_path):
    """Loads CSV, cleans column names, formats dates, and handles missing values."""
    df = pd.read_csv(file_path)
    df.columns = df.columns.str.strip()
    
    # Convert Date to datetime and sort chronologically
    df['Date'] = pd.to_datetime(df['Date'], format='mixed')
    df = df.sort_values('Date').reset_index(drop=True)
    
    # Forward-fill missing values to maintain continuity in calculations
    df = df.ffill()
    return df

def engineer_indicators(df):
    """Calculates Returns, Moving Averages, MACD, ATR, and CCI."""
    
    # 1. Day-over-Day Returns
    df['Daily_Return_%'] = df['Close'].pct_change() * 100

    # 2. Simple Moving Averages (SMA)
    df['SMA_20'] = df['Close'].rolling(window=20).mean()
    df['SMA_50'] = df['Close'].rolling(window=50).mean()

    # 3. MACD (Moving Average Convergence Divergence)
    ema_12 = df['Close'].ewm(span=12, adjust=False).mean()
    ema_26 = df['Close'].ewm(span=26, adjust=False).mean()
    df['MACD'] = ema_12 - ema_26
    df['MACD_Signal'] = df['MACD'].ewm(span=9, adjust=False).mean()

    # 4. ATR (Average True Range - 14 period)
    df['Prev_Close'] = df['Close'].shift(1)
    df['TR1'] = df['High'] - df['Low']
    df['TR2'] = abs(df['High'] - df['Prev_Close'])
    df['TR3'] = abs(df['Low'] - df['Prev_Close'])
    df['True_Range'] = df[['TR1', 'TR2', 'TR3']].max(axis=1)
    df['ATR_14'] = df['True_Range'].rolling(window=14).mean()
    df.drop(['Prev_Close', 'TR1', 'TR2', 'TR3', 'True_Range'], axis=1, inplace=True)

    # 5. CCI (Commodity Channel Index - 20 period)
    df['TP'] = (df['High'] + df['Low'] + df['Close']) / 3
    df['TP_SMA_20'] = df['TP'].rolling(window=20).mean()
    
    def mean_abs_dev(x):
        return np.mean(np.abs(x - np.mean(x)))
        
    df['Mean_Dev'] = df['TP'].rolling(window=20).apply(mean_abs_dev, raw=True)
    df['CCI_20'] = (df['TP'] - df['TP_SMA_20']) / (0.015 * df['Mean_Dev'])
    df.drop(['TP', 'TP_SMA_20', 'Mean_Dev'], axis=1, inplace=True)

    return df

if __name__ == "__main__":
    file_path = "NIFTY CEMENT-25-03-2026-to-25-09-2026.csv"
    
    print(f"Processing data for {file_path}...")
    
    # Execute Pipeline
    raw_df = load_and_clean_data(file_path)
    processed_df = engineer_indicators(raw_df)
    
    # Save output to a new CSV for VS Code charting/analysis
    output_path = "NIFTY_CEMENT_PROCESSED.csv"
    processed_df.to_csv(output_path, index=False)
    
    print(f"Success! Engineered dataset saved to {output_path}")
    print("\nRecent Indicator Snapshot:")
    print(processed_df[['Date', 'Close', 'MACD', 'ATR_14', 'CCI_20']].tail())