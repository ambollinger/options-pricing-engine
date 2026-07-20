import numpy as np
from scipy.stats import norm
def d1(S, K, T, r, sigma):
    numerator = np.log(S/K) + (r + sigma**2/2)*T
    denominator = sigma * np.sqrt(T)
    return numerator / denominator
if __name__ == '__main__':
    print(d1(100, 100, 1, 0.05, 0.2))
