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
def binomial_price(S, K, T, r, sigma, n):
    dt = T / n
    u, d = up_down_factors(sigma, dt)
    p = risk_neutral_probability(r, dt, u, d)

    prices = stock_price_tree(S, u, d, n)
    values = call_payoff(prices, K)

    for step in range(n):
        new_values = []
        for i in range(len(values) - 1 ):
            value = np.exp(-r*dt) * (p * values[i+1] + (1-p) * values[i])
            new_values.append(value)
        values = new_values
    return values[0]






if __name__ == "__main__":
    print(up_down_factors(0.2,0.01))
    print(stock_price_tree(100, 1.02, .98, 3))
    print(risk_neutral_probability(0.05, 0.01, 1.02, .98))
    print(call_payoff([94.12, 97.96, 101.96, 106.12], 100))
    print(binomial_price(100, 100, 1, 0.05, 0.2, 100))

