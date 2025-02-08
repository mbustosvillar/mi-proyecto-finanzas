import requests
import pandas as pd
from config import ALPHA_VANTAGE_API_KEY, TICKERS

def fetch_alpha_vantage_data():
    all_data = {}

    for ticker in TICKERS:
        url = f"https://www.alphavantage.co/query?function=TIME_SERIES_DAILY_ADJUSTED&symbol={ticker}&apikey={ALPHA_VANTAGE_API_KEY}&outputsize=compact"
        response = requests.get(url)
        data = response.json()

        if "Time Series (Daily)" in data:
            df = pd.DataFrame(data["Time Series (Daily)"]).T
            df = df.rename(columns={"4. close": "Close"}).astype(float)
            all_data[ticker] = df["Close"]

    market_data = pd.DataFrame(all_data)
    market_data.to_csv("data/market_data_alpha.csv")

    print("✅ Datos guardados en data/market_data_alpha.csv")

if __name__ == "__main__":
    fetch_alpha_vantage_data()
