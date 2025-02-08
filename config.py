# 📊 Activos Tradicionales (Acciones, Índices y ETFs)
TICKERS = [
    # Tecnología
    "AAPL", "MSFT", "GOOGL", "AMZN", "NVDA", "META", "TSLA", "AMD",

    # Bancos y Finanzas
    "JPM", "GS", "BAC", "C", "WFC", "MS",

    # Consumo y Retail
    "KO", "PEP", "MCD", "SBUX", "PG", "WMT", "NKE", "DIS",

    # Energía y Materias Primas
    "XOM", "CVX", "BP", "SLB", "BHP", "FCX",

    # Salud y Biotecnología
    "JNJ", "PFE", "MRNA", "BIIB", "ABBV", "LLY",

    # Índices de Mercado
    "^GSPC",  # S&P 500
    "^IXIC",  # Nasdaq
    "^DJI",   # Dow Jones

    # ETFs de Sectores Claves
    "SPY",  # S&P 500 ETF
    "QQQ",  # Nasdaq-100 ETF
    "XLF",  # Sector Financiero ETF
    "XLE",  # Sector Energético ETF
    "XLV",  # Sector Salud ETF
    "XLY",  # Sector Consumo ETF
]

# 🔹 Criptomonedas más importantes
CRYPTO_TICKERS = [
    "BTC-USD", "ETH-USD", "SOL-USD", "BNB-USD", "XRP-USD", "ADA-USD", 
    "DOGE-USD", "DOT-USD", "MATIC-USD", "LTC-USD", "LINK-USD", "AVAX-USD"
]

# 📅 Fechas de inicio y fin para los datos históricos
START_DATE = "2020-01-01"
END_DATE = "2025-01-01"

# 💰 Tasa libre de riesgo (Ejemplo: Bonos del Tesoro de EE.UU. a 10 años)
RISK_FREE_RATE = 0.04  # 4% anual

# 🔔 Configuración de Alertas Automáticas (Definir umbrales)
ALERTS = {
    "AAPL": {"high": 180, "low": 160},
    "BTC-USD": {"high": 50000, "low": 45000},
    "ETH-USD": {"high": 4000, "low": 3000},
    "SPY": {"high": 500, "low": 450},
}

# 🌍 API Key de Alpha Vantage para obtener datos en tiempo real
ALPHA_VANTAGE_API_KEY = "QH2EC6067VX9BCHK"  # 🔑 Reemplázala con tu clave de Alpha Vantage
