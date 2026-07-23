# options-pricing-engine

A from-scratch implementation of options pricing models, built to deepen my 
understanding of quantitative finance and options theory.

## What it does

- **Black-Scholes pricing** — European call and put option pricing
- **The Greeks** — delta, gamma, vega, theta, and rho, calculated from scratch
- **Binomial tree pricing** — European and American-style options, verified to 
  converge with Black-Scholes as the number of steps increases
- **Implied volatility solver** — reverse-engineers market-implied volatility 
  from real option prices, using live SPY options data

## Files

- `black_scholes.py` — Black-Scholes formula, call/put pricing, and all five Greeks
- `binomial_tree.py` — Binomial tree pricing model (Cox-Ross-Rubinstein), 
  including American-style early exercise
- `implied_vol.py` — Implied volatility solver using `scipy.optimize.brentq`, 
  pulling real options chain data via `yfinance`

## How to run

Each file can be run on its own to see example output:
python black_scholes.py
python binomial_tree.py
python implied_vol.py

## What I learned

This project was built to understand options pricing beyond just reading 
about it — implementing Black-Scholes, a numerical alternative (binomial 
tree), and an implied volatility solver from scratch, then testing each 
against known results and real market data.

## Notes

This is a learning project, not a production trading tool. It doesn't 
account for dividends, bid-ask spreads, or other real-world trading frictions.