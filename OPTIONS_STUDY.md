# Options Trading — Study Roadmap

This is an independent study notebook; source documents are separately archived under `docs/skylit/`.

## 1. Foundations
- Calls and puts, strike, expiration, premium and contract multiplier
- Moneyness: ITM / ATM / OTM
- Payoff at expiry vs. mark-to-market P&L; break-even points
- Long/short option risk, assignment, exercise, margin, liquidity and spread costs

## 2. Greeks and volatility
- Delta, Gamma, Theta, Vega, Rho
- Higher-order Greeks: Vanna, Charm, Vomma
- Implied volatility vs. realized volatility; volatility smile/skew and term structure
- How expiry and strike change Greeks

## 3. Market microstructure
- Dealer inventory and dynamic delta hedging
- GEX and VEX estimation: assumptions, data limitations and sign uncertainty
- Open interest vs. volume; interpreting options flow without inferring intent
- Key support/resistance levels, price structure and scenario invalidation

## 4. Strategy design
- Covered calls and cash-secured puts
- Vertical debit/credit spreads and defined-risk structures
- Straddles, strangles, calendars and iron condors
- Risk/reward, transaction costs, liquidity and position sizing

## 5. Validation and trading journal
- Separate hypotheses from observations; record timestamp and data source
- Define entry, exit, stop conditions, maximum loss and alternative scenarios
- Backtest with realistic costs and avoid look-ahead bias
- Track expectancy, win rate, payoff ratio, drawdown and regime dependence

## Source organization
- `docs/skylit/INDEX.md`: generated links to original Skylit articles
- `docs/skylit/manifest.json`: successful and failed archive entries

> Notes are educational, not trade recommendations. Options can cause rapid losses, and short options can expose a trader to losses larger than the initial premium.
