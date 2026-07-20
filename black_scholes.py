import numpy as np
from scipy.stats import norm
def d1(S, K, T, r, sigma):
    numerator = np.log(S/K) + (r + sigma**2/2)*T
    denominator = sigma * np.sqrt(T)
    return numerator / denominator
def d2(S, K, T, r, sigma):
    numerator = d1(S, K, T, r, sigma) - sigma*np.sqrt(T)
    return numerator

if __name__ == '__main__':
    print(d1(100, 100, 1, 0.05, 0.2))
    print(d2(100, 100, 1, 0.05, 0.2))
