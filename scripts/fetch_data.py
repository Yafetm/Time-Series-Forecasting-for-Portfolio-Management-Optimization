import yfinance as yf
import pandas as pd
import os

# Create data folder path
data_folder = os.path.join(os.path.dirname(__file__), "..", "data")
os.makedirs(data_folder, exist_ok=True)

# Define tickers and date range
tickers = ["TSLA", "BND", "SPY"]
start_date = "2015-07-01"
end_date = "2025-07-31"

# Fetch and save data
for ticker in tickers:
    print(f"Downloading {ticker} data...")
    data = yf.download(ticker, start=start_date, end=end_date)
    file_path = os.path.join(data_folder, f"{ticker}.csv")
    data.to_csv(file_path)
    print(f"Saved {ticker} data to {file_path}")

print("Data download complete.")
