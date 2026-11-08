<!-- Source: https://www.skylit.ai/learn/vomma -->

# Vomma (Volga): The Convexity of Volatility

# Vomma (Volga): The Convexity of Volatility

greeks·6 min read

vommagreeksvega

## What is Vomma?

**Vomma** (also called Volga) measures how sensitive [vega](https://www.skylit.ai/learn/vega) is to a change in implied volatility. Put simply: it's the second derivative of an option's value with respect to IV, the rate at which vega itself accelerates as volatility moves.

A position with high Vomma doesn't gain vega in a straight line. As IV rises, vega grows faster than it would without convexity. The option reprices non-linearly, so the P&L curve curves upward in a vol spike rather than responding at a fixed rate.

🎯ELI5

Volga is a turbocharger for volatility. Vega tells you how fast the engine runs at a given RPM. Volga tells you how fast the engine *accelerates* as you push down the throttle. In quiet markets the boost stays dormant; during a vol shock it kicks in and multiplies every unit of vega exposure you hold.

## Where Vomma Lives on the Surface

Vomma isn't uniformly distributed across strikes and tenors. Its concentration follows two rules:

| Dimension | High Vomma Region |
| --- | --- |
| **Strike** | ATM to slightly OTM |
| **Tenor** | Medium and long-dated expirations |

Short-dated options bleed Vomma quickly because their vega decays toward expiry. Long-dated options retain convexity because there's more time for IV to travel a wide range, and the second-order response of vega to those moves stays meaningful. This is the opposite of gamma, which concentrates at short tenors and fades in the back months. Vomma persists where gamma has already collapsed.

## How Vomma Interacts With Vega

On a flat vol surface, vega changes linearly with IV. Once Vomma is meaningful, that assumption breaks down. A 1-vol-point move in IV produces a different vega response at low IV versus high IV. Two practical consequences follow:

* **P&L convexity:** Long Vomma positions gain more vega on the way up than they lose on the way down. The exposure compounds during vol expansion.
* **Ultima interaction:** Vomma's own rate of change is captured by Ultima. For large IV gaps, Ultima becomes relevant, but in most macro regimes, Vomma alone explains the non-linearity.

💡Core Idea

During volatility shocks, IV doesn't drift higher. It gaps. Long Volga structures benefit precisely because the gap bypasses the linear vega regime and lands directly in the convex zone. You collect the accelerated vega re-pricing, not just the delta-of-vol.

## Dealer and Player Behavior

Vomma is a second-order exposure, so it requires active management only for desks running large vol books:

| Role | Behavior |
| --- | --- |
| **Dealer** | Hedges Vomma with calendar spreads and butterfly structures that neutralize convexity without disrupting vega neutrality |
| **Player** | Buys convexity ahead of known catalysts: earnings, macro events, FOMC, where IV is expected to move sharply rather than drift |

The dealer problem is that hedging gamma and hedging Vomma pull in different directions. Short-dated hedges help gamma; long-dated flies help Vomma. A desk balancing both across tenors is also managing [vanna exposure](https://www.skylit.ai/learn/vanna-exposure), since vol moves that shift vega also shift delta through the skew.

## Practical Takeaway

Vomma matters most when you expect IV to *move*, not just be *high*. A position that's long vega but flat Vomma participates in a steady IV grind but underperforms when vol reprices in a gap. Building Vomma exposure, buying options in the medium-tenor, slightly OTM range, converts a linear vol position into one that accelerates through the shock.

For a foundational map of how all second-order exposures relate, see [options greeks](https://www.skylit.ai/learn/options-greeks).

## Frequently Asked Questions

### What is vomma (volga)?

Vomma, also called volga, measures how sensitive vega is to a change in implied volatility. It's the second derivative of an option's value with respect to IV. A position with high positive vomma doesn't gain vega linearly as IV rises. Its vega accelerates as vol moves higher, producing non-linear P&L that curves upward in a vol spike rather than responding at a fixed rate. Vomma is highest for at-the-money to slightly out-of-the-money options in medium and long-dated expirations, where there's enough time for implied volatility to travel a wide range.

### Why does vomma matter for tail hedging?

Tail hedges are meant to pay off during vol shocks, which means they need to perform when IV doesn't drift higher but gaps. A position that's long vega but flat vomma participates in a slow IV grind but underperforms when volatility reprices in a sudden jump. The gap bypasses the linear vega regime and lands directly in the convex zone, where long vomma positions collect accelerated vega repricing rather than just the first-order vol sensitivity. Building vomma by buying medium-tenor, slightly OTM options converts a linear vol position into one that compounds through the shock precisely when the hedge is needed most.

### When is vomma most relevant?

Vomma is most relevant when you expect IV to move significantly, not simply when IV is high. It matters ahead of known catalysts such as earnings, FOMC announcements, or macro events where volatility is expected to reprice sharply in a short window. It's also relevant for dealers managing large complex books across many strikes and expirations, where hedging gamma and hedging vomma pull in opposite directions: short-dated structures help gamma neutrality while long-dated butterfly structures help vomma neutrality. For a single-leg directional trade, vomma is a background consideration. For structured vol positions and tail hedges, it's central to whether the position performs during the event it was designed for.

See this in Heatseeker

Monitor how volatility convexity affects positioning and dealer hedging across the options surface with Heatseeker.

[Try Heatseeker](https://www.skylit.ai/#pricing)

### Start Trading Smarter

See these concepts in action with Skylit's dealer exposure tools.

[Get access](https://www.skylit.ai/#pricing)[Try Heatseeker](https://www.skylit.ai/#pricing)
