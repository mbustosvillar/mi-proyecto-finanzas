import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

def monte_carlo_simulation(ticker="AAPL", num_simulations=1000, days=252):
    data = pd.read_csv("data/market_data.csv", index_col=0, parse_dates=True)
    returns = data[ticker].pct_change().dropna()
    
    mean_return = returns.mean()
    std_dev = returns.std()

    simulated_prices = np.zeros((days, num_simulations))
    simulated_prices[0] = data[ticker].iloc[-1]

    for i in range(1, days):
        simulated_prices[i] = simulated_prices[i - 1] * np.exp(
            (mean_return - 0.5 * std_dev ** 2) + std_dev * np.random.normal(size=num_simulations))

    plt.figure(figsize=(10, 5))
    plt.plot(simulated_prices)
    plt.title(f"Simulación Monte Carlo para {ticker}")
    plt.xlabel("Días futuros")
    plt.ylabel("Precio simulado")
    plt.show()

if __name__ == "__main__":
    monte_carlo_simulation()
