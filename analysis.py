import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from config import RISK_FREE_RATE
from llm_interface import ask_llm  # Importamos DeepSeek

def analyze_portfolio():
    """
    Analiza el portafolio calculando Sharpe Ratio, volatilidad y correlaciones.
    Luego, DeepSeek R1 interpreta los resultados.
    """
    data = pd.read_csv("data/market_data.csv", index_col=0, parse_dates=True)
    returns = data.pct_change().dropna()
    
    mean_returns = returns.mean() * 252
    volatility = returns.std() * np.sqrt(252)
    sharpe_ratio = (mean_returns - RISK_FREE_RATE) / volatility
    correlation_matrix = returns.corr()

    # Guardar la matriz de correlación
    correlation_matrix.to_csv("data/correlation_matrix.csv")

    # Graficar correlaciones
    plt.figure(figsize=(14, 10))
    sns.heatmap(correlation_matrix, annot=False, cmap="coolwarm", linewidths=0.5)
    plt.title("Matriz de Correlación entre Activos")
    plt.show()

    # Generar interpretación con DeepSeek
    summary = f"""
    📊 Análisis de Portafolio:
    - Retorno Esperado Anual: {mean_returns.to_dict()}
    - Volatilidad Anualizada: {volatility.to_dict()}
    - Ratio de Sharpe: {sharpe_ratio.to_dict()}
    - Correlaciones guardadas en: data/correlation_matrix.csv
    """
    
    resultado_ia = ask_llm(f"Analiza este portafolio y da recomendaciones:\n{summary}")
    
    print("\n🔹 Recomendaciones de la IA:")
    print(resultado_ia)
    
    return sharpe_ratio, correlation_matrix

if __name__ == "__main__":
    analyze_portfolio()
