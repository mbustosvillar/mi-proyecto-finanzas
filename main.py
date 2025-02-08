from fetch_data import get_market_data
from analysis import analyze_portfolio
from prediction_xgboost import predict_stock
from portfolio_optimization import optimize_portfolio
from llm_interface import ask_llm

# Obtener datos de mercado
print("Descargando datos...")
get_market_data()

# Análisis financiero
print("Analizando portafolio...")
analysis = analyze_portfolio()
print(analysis)

# Predicción con XGBoost
print("Predicción con XGBoost...")
prediction = predict_stock()
print(prediction)

# Optimización del portafolio
print("Optimizando portafolio...")
optimization = optimize_portfolio()
print(optimization)

# Enviar análisis al LLM
print("Consultando a la IA...")
llm_response = ask_llm(f"Analiza este portafolio:\n{analysis}")
print(llm_response)
