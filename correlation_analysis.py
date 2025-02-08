import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

# Cargar datos de mercado desde CSV
data = pd.read_csv("data/market_data.csv", index_col=0, parse_dates=True)

# Calcular retornos diarios
returns = data.pct_change().dropna()

# Calcular la matriz de correlación
correlation_matrix = returns.corr()

# Guardar la matriz en CSV para referencia futura
correlation_matrix.to_csv("data/correlation_matrix.csv")

# Visualizar con un heatmap
plt.figure(figsize=(14, 10))
sns.heatmap(correlation_matrix, annot=False, cmap="coolwarm", linewidths=0.5)
plt.title("Matriz de Correlación entre Activos del Portafolio", fontsize=14)
plt.show()

# Mostrar las correlaciones más altas y más bajas
top_correlations = correlation_matrix.unstack().sort_values(ascending=False)
filtered_correlations = top_correlations[(top_correlations < 1) & (top_correlations > 0.7)]  # Altamente correlacionados
filtered_negative_correlations = top_correlations[top_correlations < -0.5]  # Negativamente correlacionados

print("\n🔹 Activos con correlaciones más altas (movimiento similar):")
print(filtered_correlations)

print("\n🔹 Activos con correlaciones más bajas (movimiento opuesto):")
print(filtered_negative_correlations)
