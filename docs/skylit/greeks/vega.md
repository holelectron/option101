<!-- Source: https://www.skylit.ai/learn/vega -->

# Vega: The Breath of the Market — Volatility Sensitivity

# Vega: The Breath of the Market — Volatility Sensitivity

greeks·7 min read

vegagreeks

## What is Vega?

**Vega (ν)** measures the sensitivity of an option's price to a one-point change in implied volatility (IV). It's one of the core [options greeks](https://www.skylit.ai/learn/options-greeks) and sits at the heart of how options premiums expand and contract around events, fear cycles, and calm regimes.

When implied volatility rises, option premiums expand. Long vega positions benefit. When implied volatility falls, premiums contract. Short vega positions benefit. Every option has vega, but its magnitude depends heavily on time to expiry and moneyness.

🎯ELI5

Vega is the market's breathing. When fear enters, the market inhales, implied volatility rises and premiums inflate. When calm returns, the market exhales, IV compresses and premiums deflate. Trading vega is trading the breath itself, not the direction.

## How Vega Works

| Role | Behavior |
| --- | --- |
| **Dealer** | Usually short vol; hedges exposure by trading options against inventory |
| **Player (retail/fund)** | Buys vol in fear, sells vol in calm |

Dealers who sell options to meet demand accumulate short vega. As IV rises, their books lose value, so they must hedge by buying volatility. Players do the opposite, leaning into fear by purchasing protection or speculative calls, adding to long vega exposure across the market.

This structural dynamic means that **vol regime changes often feed themselves**: a spike in fear pushes IV higher, forcing dealer hedging that can amplify the move further.

## Key Properties of Vega

**Vega is highest at-the-money (ATM).** An ATM option has the greatest uncertainty about where it will land at expiry, so its price is most sensitive to changes in the market's implied volatility estimate.

**Vega scales approximately with √T.** Long-dated options carry large vega; short-dated options carry very little. A 90-day option might have ten times the vega sensitivity of a 1-week option at the same strike. At 0DTE, vega is effectively zero. There's no time left for volatility to matter in dollar terms.

**Time decay reduces dollar vega.** As expiry approaches, even if IV stays constant, the absolute dollar sensitivity of the option to vol changes shrinks. Vega risk bleeds away over time for held positions.

💡Core Idea

IV crush after an earnings event is pure vega mechanics. Before the event, implied volatility inflates as market participants pay up for protection or speculation. The moment results are announced, uncertainty resolves and IV collapses, even if the stock moves significantly. Long options holders lose on vega faster than they gain on delta.

## Vega and Cross-Greek Interactions

Vega feeds two important second-order greeks:

* **[Vanna](https://www.skylit.ai/learn/vanna-exposure)**, the sensitivity of delta to changes in IV (∂Δ/∂σ). When vega is large and IV moves, vanna governs how dealer delta hedges need to be adjusted. This drives vanna flows during vol spikes.
* **[Vomma](https://www.skylit.ai/learn/vomma)**, the sensitivity of vega itself to changes in IV (∂ν/∂σ). High vomma means a position's vega exposure accelerates as IV rises, making it particularly powerful in vol expansion regimes.

Understanding these interactions is what separates surface-level options analysis from genuine structural edge.

## Event Runs and IV Crush

Vega governs the lifecycle of event trades:

* **Pre-event:** Market participants buy options ahead of earnings, macro data, or Fed decisions. IV rises, lifting all premiums regardless of direction.
* **Post-event:** Uncertainty resolves. IV collapses rapidly, a phenomenon known as **IV crush**. Long options positions that were right on direction can still lose money if the vega loss outweighs the delta gain.

That's why experienced traders distinguish between buying premium ahead of events versus selling it. The direction trade is separate from the volatility trade.

## Vega Across Tenors

* **0DTE:** Vega is near zero. Delta and gamma dominate intraday.
* **1–7 DTE:** Transition zone. Small but non-trivial vega; IV events can still move premiums meaningfully.
* **30+ DTE:** Vega world. The IV path, not just spot price, determines whether a position is profitable.

Long-dated options are fundamentally vol instruments. Short-dated options become increasingly directional as expiry nears.

See this in Heatseeker

Track how implied volatility shifts affect dealer positioning across strikes with Heatseeker.

[Try Heatseeker](https://www.skylit.ai/#pricing)

## Summary

Vega measures how much an option's price changes for each one-point move in implied volatility. It's highest at-the-money, scales with the square root of time to expiry, and drives the premium expansion and contraction traders experience around events. Long vega benefits from vol rises; short vega benefits from vol crush. Vega also feeds [vanna](https://www.skylit.ai/learn/vanna-exposure) and [vomma](https://www.skylit.ai/learn/vomma), making it central to understanding how dealer hedging flows propagate through the market during volatility regime changes.

## Frequently Asked Questions

### What is vega in options?

Vega measures the sensitivity of an option's price to a one-point change in implied volatility. When implied volatility rises, option premiums expand and long vega positions gain value. When implied volatility falls, premiums contract and short vega positions benefit. It's the greek that captures the market's fear or complacency, not its direction.

### How does implied volatility affect options prices?

Implied volatility is the market's expectation of future movement embedded in an option's price. When fear enters the market, IV rises and all option premiums inflate regardless of direction. When calm returns, IV compresses and premiums deflate. This is why a trader who was right on direction can still lose money after an earnings event: the vega loss from IV crush can outweigh the delta gain from the stock's actual move.

### What happens to vega near expiration?

Vega decays toward zero as expiration approaches. A 90-day option can have ten times the vega sensitivity of a 1-week option at the same strike, and at 0DTE vega is effectively zero. Short-dated options are increasingly driven by delta and gamma, not volatility. Long-dated options are fundamentally vol instruments where the IV path matters as much as the direction of spot price.

### Start Trading Smarter

See these concepts in action with Skylit's dealer exposure tools.

[Get access](https://www.skylit.ai/#pricing)[Try Heatseeker](https://www.skylit.ai/#pricing)
