import pandas as pd
import numpy as np
import scipy.optimize as sco
from config import TICKERS  # Asegúrate de importar los tickers definidos en config.py

def optimize_portfolio(file="data/market_data.csv"):
    # 1️⃣ Cargar datos y eliminar columnas vacías
    data = pd.read_csv(file, index_col=0, parse_dates=True).dropna(how="all", axis=1)
    
    # 2️⃣ Ver qué columnas hay realmente en el dataset
    print("🔍 Columnas originales del DataFrame:", data.columns)

    # 3️⃣ Filtrar los tickers que realmente están en los datos
    valid_tickers = [ticker for ticker in TICKERS if ticker in data.columns]
    
    if len(valid_tickers) == 0:
        print("❌ No hay activos válidos para optimizar.")
        return {}

    print("✅ Activos válidos para optimización:", valid_tickers)

    # 4️⃣ Calcular retornos y eliminar filas con NaN
    returns = data[valid_tickers].pct_change().dropna()
    cov_matrix = returns.cov() * 252  # Convertir a varianza anualizada

    # 5️⃣ Asegurar que no haya NaNs en la matriz de covarianza
    if cov_matrix.isnull().values.any():
        print("⚠️ Hay NaNs en la matriz de covarianza. Revisa los datos.")
        return {}

    # 6️⃣ Definir número de activos y pesos iniciales
    num_assets = len(valid_tickers)
    initial_weights = np.array([1.0 / num_assets] * num_assets)

    print("🔢 Número de activos optimizados:", num_assets)
    print("🔹 Dimensión de cov_matrix:", cov_matrix.shape)
    print("🔹 Dimensión de initial_weights:", initial_weights.shape)

    # 7️⃣ Función objetivo: minimizar la volatilidad del portafolio
    def portfolio_volatility(weights):
        return np.sqrt(np.dot(weights.T, np.dot(cov_matrix, weights)))

    # 8️⃣ Restricciones y límites
    constraints = {"type": "eq", "fun": lambda x: np.sum(x) - 1}  # La suma de pesos debe ser 1
    bounds = [(0, 1) for _ in range(num_assets)]  # Pesos entre 0% y 100%

    # 9️⃣ Optimización
    optimal = sco.minimize(
        portfolio_volatility,
        initial_weights,
        method="SLSQP",
        bounds=bounds,
        constraints=constraints
    )

    # 🔟 Verificar si la optimización fue exitosa
    if not optimal.success:
        print("❌ La optimización falló:", optimal.message)
        return {}

    # 🔥 Retornar los pesos optimizados
    return dict(zip(valid_tickers, optimal.x))

# 🔍 Test de depuración local
if __name__ == "__main__":
    optimized_weights = optimize_portfolio()
    print("✅ Pesos óptimos del portafolio:", optimized_weights)
