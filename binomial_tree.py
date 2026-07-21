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







if __name__ == "__main__":
    print(up_down_factors(0.2,0.01))
    print(stock_price_tree(100, 1.02, .98, 3))
