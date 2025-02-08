import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM, Dense
from sklearn.preprocessing import MinMaxScaler

def predict_lstm(ticker="AAPL"):
    data = pd.read_csv("data/market_data.csv", index_col=0, parse_dates=True)
    df = data[[ticker]].dropna()
    
    scaler = MinMaxScaler()
    scaled_data = scaler.fit_transform(df.values.reshape(-1, 1))
    
    seq_length = 30
    X_lstm, y_lstm = [], []
    for i in range(len(scaled_data) - seq_length):
        X_lstm.append(scaled_data[i:i+seq_length])
        y_lstm.append(scaled_data[i+seq_length])

    X_lstm, y_lstm = np.array(X_lstm), np.array(y_lstm)
    split = int(0.8 * len(X_lstm))
    X_train, X_test, y_train, y_test = X_lstm[:split], X_lstm[split:], y_lstm[:split], y_lstm[split:]

    model = Sequential([
        LSTM(50, return_sequences=True, input_shape=(seq_length, 1)),
        LSTM(50, return_sequences=False),
        Dense(25),
        Dense(1)
    ])

    model.compile(optimizer="adam", loss="mean_squared_error")
    model.fit(X_train, y_train, epochs=20, batch_size=16)
    y_pred = model.predict(X_test)
    return scaler.inverse_transform(y_pred)

if __name__ == "__main__":
    print(predict_lstm())
