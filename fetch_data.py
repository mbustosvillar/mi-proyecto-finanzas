import yfinance as yf
import pandas as pd
from datetime import datetime
from config import TICKERS, CRYPTO_TICKERS, START_DATE, END_DATE

def get_market_data():
    """
    Descarga datos de Yahoo Finance (acciones y cripto) y los guarda en un CSV.
    Maneja errores cuando 'Adj Close' no está disponible.
    """
    print(f"🔄 Descargando datos en vivo... ({datetime.now().strftime('%Y-%m-%d %H:%M:%S')})")
    
    # Descargar datos de acciones
    stock_data = yf.download(TICKERS, start=START_DATE, end=END_DATE)

    # Usar 'Adj Close' si está disponible, sino usar 'Close'
    if 'Adj Close' in stock_data.columns:
        stock_data = stock_data["Adj Close"]
    else:
        stock_data = stock_data["Close"]

    # Descargar datos de criptomonedas
    crypto_data = yf.download(CRYPTO_TICKERS, start=START_DATE, end=END_DATE)

    if 'Adj Close' in crypto_data.columns:
        crypto_data = crypto_data["Adj Close"]
    else:
        crypto_data = crypto_data["Close"]

    # Verificar si los datos están vacíos
    if stock_data.empty or crypto_data.empty:
        print("⚠️ Advertencia: No se descargaron datos correctamente.")
        return
    
    # Unir los datos en un solo DataFrame
    market_data = pd.concat([stock_data, crypto_data], axis=1)

    # Guardar en CSV
    market_data.to_csv("data/market_data.csv")
    
    print("✅ Datos guardados en data/market_data.csv")
    return market_data

if __name__ == "__main__":
    get_market_data()
