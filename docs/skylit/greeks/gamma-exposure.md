<!-- Source: https://www.skylit.ai/learn/gamma-exposure -->

# Gamma Exposure (GEX) Explained: The Market's Shock Absorber

# Gamma Exposure (GEX) Explained: The Market's Shock Absorber

greeks·12 min read

gammagexdealer-positioningheatseeker

## What is Gamma Exposure?

**Gamma (Γ)** measures the rate of change of delta per $1 move in the underlying. It controls whether the market mean-reverts or accelerates.

When dealers are **long gamma (+GEX)**, called Pika nodes on Heatseeker (the Academy's "yellow node"), their hedges oppose the market's move. They buy dips and sell rips. That creates stability and mean reversion.

When dealers are **short gamma (–GEX)**, called Barney nodes on Heatseeker (the Academy's "purple node"), their hedges chase the move. They sell dips and buy rips. That amplifies volatility.

On the board itself, cell color follows the chosen palette and the node's size, not its sign, so read the number and its minus sign.

🎯ELI5

Gamma is a car's suspension: smooth in calm conditions, but unstable on ice. In +GEX, the shocks absorb bumps. In –GEX, every bump throws you further off course.

## How GEX Affects Market Behavior

| Condition | Dealer Hedge | Market Behavior |
| --- | --- | --- |
| **+GEX (Long Γ)** | Buys dips, sells rips | Stability, mean reversion |
| **–GEX (Short Γ)** | Sells dips, buys rips | Volatility amplification |

**Above/Below Spot:** +GEX below spot acts as support. +GEX above spot acts as resistance. Where GEX sign changes is where polarity flips, and where the most violent moves occur. The node with the highest absolute GEX value across the heatmap is called the **King Node**. It can be positive or negative, and it is where market makers hold the greatest exposure and where price often gravitates near expiration.

## Vol Behavior and GEX

Volatility rising amplifies –GEX effects. Volatility falling strengthens +GEX pins. GEX defines *potential*. VIX defines *reality*.

💡Core Idea

Each Greek is a dimension of risk the dealer must neutralize. When crowd exposure shifts, dealers rebalance. Their hedges feed back into price, volatility, and liquidity.

## Cross-Greek Mechanics

* **If dealer is long delta → they sell stock** to neutralize; **short delta → they buy stock**.
* **Long gamma (+GEX)** makes those buy/sell actions **contrarian** to price (stabilizing).
* **Short gamma (–GEX)** makes them **pro-cyclical** (amplifying).

See this in Heatseeker

Visualize live GEX levels across all strikes and expirations with Heatseeker's gamma exposure heatmaps.

[Try Heatseeker](https://www.skylit.ai/#pricing)

## Time and Tenor

* **0DTE:** Gamma and Charm dominate. Vanna is near zero. Same-day pins and breaks rule intraday. See [GEX tools for 0DTE SPX](https://www.skylit.ai/learn/best-gex-tools-0dte-spx) for reading the same-day column.
* **1–7 DTE:** Transition zone. Gamma is still large, but Vanna begins to matter.
* **>30 DTE:** Vanna/Vega world. The IV path drives price drift via hedging.

Gamma scales approximately as **1/√T**. Short-dated options have explosive gamma. Long-dated options have very little.

## Frequently Asked Questions

### What is gamma exposure (GEX)?

Gamma exposure measures the rate of change of delta per $1 move in the underlying asset. It determines whether market makers' hedging activity stabilizes or amplifies price moves. When you see a GEX reading on a heatmap, you're seeing how much mechanical buying or selling pressure dealers are obligated to apply as price moves through that level.

### How does GEX affect stock prices?

Positive GEX means dealers are long gamma, so their hedges are contrarian: they buy dips and sell rips, which creates stability and mean reversion around those levels. Negative GEX flips that dynamic entirely. Dealers are short gamma, so their hedges chase the move by selling dips and buying rips, which amplifies volatility and accelerates trends.

### What is the difference between positive and negative GEX?

Positive GEX nodes (called Pika nodes on Heatseeker) represent strikes where dealer hedging is contrarian to price, producing mean-reversion behavior. Negative GEX nodes (called Barney nodes) represent strikes where dealer hedging is pro-cyclical, accelerating moves away from that level. The sign change between the two is where polarity flips and the most violent price moves tend to occur.

### What is a King Node?

The King Node is the strike with the largest absolute GEX value across the entire heatmap. It can be positive or negative, so it is not always a stabilizing level. It is where market makers hold the greatest exposure and where price often gravitates near expiration. Market makers often pin price near the King Node late in the session, making it one of the most actionable reference points in any GEX-based analysis.

### Start Trading Smarter

See these concepts in action with Skylit's dealer exposure tools.

[Get access](https://www.skylit.ai/#pricing)[Try Heatseeker](https://www.skylit.ai/#pricing)
