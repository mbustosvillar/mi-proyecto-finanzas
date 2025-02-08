import pandas as pd
import numpy as np
import xgboost as xgb
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error
from llm_interface import ask_llm  # Importamos DeepSeek

def predict_stock(ticker="AAPL"):
    """
    Predice el precio de un activo usando XGBoost y permite que DeepSeek R1 B7 Q4 interprete los resultados.
    """
    data = pd.read_csv("data/market_data.csv", index_col=0, parse_dates=True)
    df = data[[ticker]].dropna()

    df["Lag_1"] = df[ticker].shift(1)
    df["Lag_5"] = df[ticker].shift(5)
    df["Lag_10"] = df[ticker].shift(10)
    df = df.dropna()

    X = df[["Lag_1", "Lag_5", "Lag_10"]]
    y = df[ticker]

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, shuffle=False)
    
    model = xgb.XGBRegressor(n_estimators=1000, learning_rate=0.05)
    model.fit(X_train, y_train)

    y_pred = model.predict(X_test)
    mae = mean_absolute_error(y_test, y_pred)

    # Generar interpretación con DeepSeek
    pred_summary = f"""
    📈 Predicción de {ticker} con XGBoost:
    - Error medio absoluto (MAE): {mae}
    - Últimos precios reales: {y_test.values[-5:]}
    - Últimos precios predichos: {y_pred[-5:]}
    """
    
    resultado_ia = ask_llm(f"Analiza esta predicción financiera y da recomendaciones:\n{pred_summary}")
    
    print("\n🔹 Recomendaciones de la IA:")
    print(resultado_ia)

    return y_test, y_pred

if __name__ == "__main__":
    predict_stock()
