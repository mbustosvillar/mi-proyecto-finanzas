import pandas as pd
import numpy as np
import scipy.optimize as sco
from config import TICKERS

def optimize_portfolio():
    data = pd.read_csv("data/market_data.csv", index_col=0, parse_dates=True)
    returns = data.pct_change().dropna()
    
    mean_returns = returns.mean() * 252
    cov_matrix = returns.cov() * 252

    # Función de volatilidad para minimizar
    def portfolio_volatility(weights):
        return np.sqrt(np.dot(weights.T, np.dot(cov_matrix, weights)))

    num_assets = len(TICKERS)
    constraints = {"type": "eq", "fun": lambda x: np.sum(x) - 1}  # Pesos suman 1
    bounds = tuple((0, 1) for _ in range(num_assets))  # Pesos entre 0% y 100%

    initial_weights = num_assets * [1. / num_assets]
    optimal = sco.minimize(portfolio_volatility, initial_weights, method="SLSQP", bounds=bounds, constraints=constraints)

    # Retornar los pesos óptimos
    optimized_weights = dict(zip(TICKERS, optimal.x))
    return optimized_weights

if __name__ == "__main__":
    result = optimize_portfolio()
    print("Pesos óptimos:", result)


from pypfopt.black_litterman import BlackLittermanModel
from pypfopt.efficient_frontier import EfficientFrontier

def optimize_black_litterman():
    data = pd.read_csv("data/market_data.csv", index_col=0, parse_dates=True)
    returns = data.pct_change().dropna()
    
    market_prior = returns.mean() * 252  # Retornos esperados del mercado

    # Suposición: crees que AAPL subirá 10% más que el mercado
    viewdict = {"AAPL": 0.10}
    
    bl = BlackLittermanModel(returns.cov(), market_prior, absolute_views=viewdict)
    
    ef = EfficientFrontier(bl.bl_returns, returns.cov())
    weights = ef.max_sharpe()

    return weights

if __name__ == "__main__":
    result = optimize_black_litterman()
    print("Pesos optimizados con Black-Litterman:", result)

