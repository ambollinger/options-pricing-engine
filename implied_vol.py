import numpy as np
from scipy.optimize import brentq
from black_scholes import call_price
import yfinance as yf


def price_difference(sigma, S, K, T, r, market_price):
    model_price = call_price(S, K, T, r, sigma)
    return model_price - market_price

def find_implied_vol(S, K, T, r, market_price):
    implied_vol = brentq(price_difference, 0.01, 5.0, args=(S, K, T, r, market_price))
    return implied_vol

if __name__ == "__main__":
    test_price = call_price(100, 100, 1, 0.05, 0.2)
    print(test_price)
    print(find_implied_vol(100, 100, 1, 0.05, test_price))

    ticker = yf.Ticker("SPY")
    expirations = ticker.options
    print(expirations)