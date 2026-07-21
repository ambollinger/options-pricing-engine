import numpy as np
from scipy.stats import norm

def d1(S, K, T, r, sigma):
    numerator = np.log(S/K) + (r + sigma**2/2)*T
    denominator = sigma * np.sqrt(T)
    return numerator / denominator
def d2(S, K, T, r, sigma):
    numerator = d1(S, K, T, r, sigma) - sigma*np.sqrt(T)
    return numerator
def call_price(S, K, T, r, sigma):
    N_d1 = norm.cdf(d1(S, K, T, r, sigma))
    N_d2 = norm.cdf(d2(S, K, T, r, sigma))
    price = S * N_d1 - K * np.exp(-r*T) * N_d2
    return price
def put_price(S, K, T, r, sigma):
    call = call_price(S, K, T, r, sigma)
    price = call - S + K * np.exp(-r*T)
    return price

def delta(S, K, T, r, sigma):
    return norm.cdf(d1(S, K, T, r, sigma))
def gamma(S, K, T, r, sigma):
    numerator = norm.pdf(d1(S, K, T, r, sigma))
    denominator = S *sigma * np.sqrt(T)
    return numerator / denominator
def vega(S, K, T, r, sigma):
    return S * norm.pdf(d1(S, K, T, r, sigma))



if __name__ == '__main__':
    print(d1(100, 100, 1, 0.05, 0.2))
    print(d2(100, 100, 1, 0.05, 0.2))
    print(call_price(100, 100, 1, 0.05, 0.2))
    print(put_price(100, 100, 1, 0.05, 0.2))
    print(delta(100, 100, 1, 0.05, 0.2))
    print(gamma(100, 100, 1, 0.05, 0.2))
    print(vega(100, 100, 1, 0.05, 0.2))




