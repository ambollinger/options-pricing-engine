import numpy as np
from scipy.stats import norm

def up_down_factors(sigma,dt):
    u = np.exp(sigma * np.sqrt(dt))
    d = 1 / u
    return u, d
def stock_price_tree(S, u, d, n):
    prices = []
    for j in range(n+1):
        price = S * (u**j) * (d ** (n-j))
        prices.append(price)
    return prices
def risk_neutral_probability(r, dt, u,d):
    return (np.exp(r * dt) - d) / (u -d)
def call_payoff(prices, K):
    payoffs = []
    for price in prices:
        payoff = max(price - K, 0)
        payoffs.append(payoff)
    return payoffs





if __name__ == "__main__":
    print(up_down_factors(0.2,0.01))
    print(stock_price_tree(100, 1.02, .98, 3))
    print(risk_neutral_probability(0.05, 0.01, 1.02, .98))
    print(call_payoff([94.12, 97.96, 101.96, 106.12], 100))
