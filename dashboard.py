import streamlit as st
import pandas as pd
import subprocess
import time
import matplotlib.pyplot as plt
import seaborn as sns
from analysis import analyze_portfolio
from prediction_xgboost import predict_stock
from portfolio_optimization import optimize_portfolio
from llm_interface import ask_llm
from monte_carlo import monte_carlo_simulation

# Configurar la página del Dashboard
st.set_page_config(page_title="Análisis de Portafolio con IA", layout="wide")

# Título
st.title("📊 Dashboard en Tiempo Real de Análisis Financiero")

# Botón para actualizar datos
if st.button("🔄 Actualizar Datos del Mercado"):
    with st.spinner("Descargando datos..."):
        subprocess.run(["python", "fetch_data.py"])  # Ejecuta el script de descarga
        time.sleep(3)  # Espera un poco para asegurar que se guarden los datos
    st.success("✅ Datos actualizados correctamente!")

# Cargar datos del CSV actualizado
data = pd.read_csv("data/market_data.csv", index_col=0, parse_dates=True)

# Mostrar los últimos precios
st.write("📈 **Últimos Precios del Mercado**")
st.dataframe(data.tail())

# Sección 1: Análisis del Portafolio
st.header("📊 Análisis del Portafolio")

# Obtener Sharpe Ratio y matriz de correlación
sharpe_ratio, correlation_matrix = analyze_portfolio()

# Mostrar Sharpe Ratio
st.write("🔹 **Ratio de Sharpe:**")
st.dataframe(sharpe_ratio)

# Mostrar la Matriz de Correlaciones
st.write("🔹 **Matriz de Correlaciones entre Activos**")
fig, ax = plt.subplots(figsize=(12, 8))
sns.heatmap(correlation_matrix, annot=False, cmap="coolwarm", linewidths=0.5, ax=ax)
st.pyplot(fig)

# Interpretación con DeepSeek
st.write("💡 **Análisis del Portafolio por IA**")
resultado_ia = ask_llm(f"Analiza este portafolio y da recomendaciones:\n{sharpe_ratio.to_dict()}")
st.write(resultado_ia)

# Sección 2: Predicción de Precios
st.header("📈 Predicción de Precios con XGBoost")

# Seleccionar activo para predicción
ticker = st.selectbox("Selecciona un activo para predecir su precio:", data.columns)

# Ejecutar predicción y mostrar gráfico
if st.button("Ejecutar Predicción"):
    y_test, y_pred = predict_stock(ticker)

    fig2, ax2 = plt.subplots(figsize=(10, 5))
    ax2.plot(y_test.index, y_test, label="Precio Real", color="blue")
    ax2.plot(y_test.index, y_pred, label="Predicción XGBoost", linestyle="dashed", color="red")
    ax2.legend()
    st.pyplot(fig2)

    # Análisis con IA
    pred_summary = f"📈 Predicción de {ticker}:\nÚltimos precios reales: {y_test.values[-5:]}\nÚltimos precios predichos: {y_pred[-5:]}"
    resultado_pred = ask_llm(f"Analiza esta predicción financiera y da recomendaciones:\n{pred_summary}")
    st.write("💡 **Análisis de la IA:**")
    st.write(resultado_pred)

# Sección 3: Optimización de Portafolio
st.header("💰 Optimización de Portafolio")

# Optimización con Markowitz
st.write("📌 **Pesos Óptimos del Portafolio (Markowitz)**")
optimized_weights = optimize_portfolio()
st.write(optimized_weights)

# Interpretación con IA
st.write("💡 **Análisis de la IA sobre la Optimización**")
opt_summary = f"Optimización de Portafolio:\n{optimized_weights}"
resultado_opt = ask_llm(f"Analiza la optimización de este portafolio y sugiere mejoras:\n{opt_summary}")
st.write(resultado_opt)

# Sección 4: Simulación Monte Carlo
st.header("🎲 Simulación Monte Carlo")

# Seleccionar activo para simular
ticker_mc = st.selectbox("Selecciona un activo para simular escenarios:", data.columns)

# Ejecutar Simulación Monte Carlo
if st.button("Ejecutar Simulación Monte Carlo"):
    monte_carlo_simulation(ticker_mc)

st.write("📌 Elige un activo y presiona el botón para ver múltiples escenarios de precios en el futuro.")

# Sección 5: Generar Reporte en PDF
st.header("📄 Generar Reporte de Análisis")
if st.button("Generar Reporte PDF"):
    from report_generator import generate_pdf_report
    generate_pdf_report()
    st.write("✅ **Reporte generado! Descarga en `data/report.pdf`**")
