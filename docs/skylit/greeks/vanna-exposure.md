<!-- Source: https://www.skylit.ai/learn/vanna-exposure -->

# Vanna Exposure (VEX): The Vol–Spot Feedback Loop

# Vanna Exposure (VEX): The Vol–Spot Feedback Loop

greeks·12 min read

vannavexdealer-positioningheatseeker

## What is Vanna?

**Vanna** measures how [delta](https://www.skylit.ai/learn/delta) changes as implied volatility changes, or equivalently, how vega changes as the underlying price moves. It's the bridge between two worlds that are usually treated separately: the price dimension and the volatility dimension.

When implied volatility shifts, every option's delta shifts with it. A call that was 0.30 delta at a given IV level will carry a different delta at a lower IV level. That change in delta requires dealers to rebalance their stock hedges. Vanna quantifies exactly how large that rebalancing will be.

Vanna is a second-order effect: it only becomes visible when volatility moves. In a flat, low-vol tape it hums quietly in the background. When IV compresses or spikes, vanna becomes one of the dominant forces shaping dealer flow.

🎯ELI5

Vanna is a tailwind you only notice when it stops blowing. In calm conditions the market grinds higher and it feels like nothing is happening. What's actually happening is that falling IV is mechanically pushing dealer hedges in one direction, producing a quiet, sustained bid. The tailwind becomes obvious only when it reverses.

## The VEX Exposure Table

**Vanna Exposure (VEX)** is the aggregate sum of vanna across all open options positions at a given strike. It tells you the direction and magnitude of the hedging flow dealers will produce as IV moves.

| Exposure | Vol Down | Vol Up | Dealer Flow | Market Bias |
| --- | --- | --- | --- | --- |
| **+VEX Below Spot** | Dealers buy stock | Dealers sell stock | Supportive in calm | Pin and drift |
| **–VEX Below Spot** | Dealers sell stock | Dealers buy stock | Fragile floor | Whipsaw |
| **+VEX Above Spot** | Dealers buy stock | Dealers sell stock | Resistance melts away | Breakout in calm |
| **–VEX Above Spot** | Dealers sell stock | Dealers buy stock | Elastic ceiling | Squeeze in stress |

The sign and location of VEX relative to spot price determine whether vol moves are stabilizing or destabilizing. Positive VEX creates supportive flow when vol compresses; negative VEX does the opposite.

## How VEX Drives Market Flow

The mechanism is straightforward. A dealer who is short options carries positive vanna on net. As implied volatility falls, those options' deltas decrease. The dealer needs less stock to stay hedged, so they buy back the stock. That buying adds flow that has nothing to do with fundamental news or price discovery.

**Positive VEX (dealer deltas increase as vol rises):** When vol falls, dealers reduce their long delta and buy back hedges. When vol rises, dealers need more delta and they sell. In a vol compression environment, +VEX below spot produces a mechanical bid under the market. In a vol expansion environment, that same +VEX becomes sell flow.

**Negative VEX (dealer deltas decrease as vol rises):** When vol rises, dealer delta requirements fall and they buy. When vol falls, they sell. This is the inverse: –VEX creates buy flow in stressed markets and sell flow in calm ones. A market sitting on a layer of –VEX below spot has a floor that appears during panics but evaporates the moment vol settles.

💡Core Idea

The position of VEX relative to spot matters as much as its sign. Large +VEX below spot is a vol-compression tailwind: every tick lower in the VIX produces mechanical buying. The same +VEX above spot is a resistance-dissolution mechanism. As IV falls, the wall dissolves and the market can drift through levels that previously held.

Understanding the table above is the foundation for reading dealer flows in a low-VIX environment. Most of the slow, grindy, catalyst-free upside seen during calm periods isn't random. It's positive VEX working.

## Vanna and Charm Drift

Vanna rarely operates alone. In low-vol regimes, it combines with [charm](https://www.skylit.ai/learn/charm) to produce a sustained, compounding drift that can last for hours and sometimes days.

**Vanna Drift:** When implied volatility compresses, dealers who carry +VEX buy back the hedges they no longer need. Upward price drift follows, in proportion to the size of the aggregate positive vanna exposure in the market. No catalyst required. It's a mechanical consequence of IV moving.

**Charm Drift:** Separately, time decay reduces option deltas. Dealers rebalance by buying stock to maintain delta neutrality. More upward drift, no vol move required.

When both mechanisms are present simultaneously, falling IV and passing time, the flows stack. Each is individually modest, but together they sustain a grinding, low-range bid for an entire session. The tape feels impervious to selling without any obvious reason why.

The practical implication: afternoon hours in low-VIX regimes are often dominated by the combined effect of vanna and charm. Identifying where those forces are pointing is more useful than watching the order book.

## Cross-Expiry Dynamics

One of the most counterintuitive aspects of vanna is what happens across expiration dates during volatility events.

Short-dated options near expiry have vanna close to zero. Their vega is already negligible, so there's little sensitivity to vol to transmit into delta change. 0DTE and same-week options contribute almost nothing to aggregate VEX. The drivers of vanna flows are the medium-dated and back-end expirations, where vega is still substantial and small IV moves translate into meaningful delta shifts.

A layering effect results. On a normal day, same-day [gamma exposure](https://www.skylit.ai/learn/gamma-exposure) may dominate intraday price action: large gamma swings around key strikes controlling the range. But below the surface, longer-dated vanna is adding a background buy flow during vol compression that never appears in a 0DTE gamma map.

When vol spikes, the interaction reverses and becomes dangerous. Back-end options suddenly create significant sell flow as their dealer delta requirements rise sharply with IV. That sell flow overrides whatever short-term GEX support was holding price. What looked like a stable +GEX pin breaks, not because gamma flipped, but because cross-expiry vanna turned net sell flow.

Tracking only the front expiration gives you an incomplete picture. The full expiration surface, particularly the vanna contribution from options 30 to 90 days out, determines how robust any support level actually is when IV moves.

Vanna also fades into expiry. As an option approaches its final hours, vega collapses and vanna approaches zero. The largest vanna exposures in any term structure sit in the slightly out-of-the-money strikes of the medium-dated contracts, where both vega and delta sensitivity to vol remain meaningful. Vanna scales approximately with the square root of time to expiry: long-dated options carry strong vanna; 0DTE options carry near zero.

See this in Heatseeker

Visualize vanna exposure (VEX) across all strikes and expirations, see where dealer vol-spot coupling creates drift, support, and rug-pull risk.

[Try Heatseeker](https://www.skylit.ai/#pricing)

## Key Properties

* Measures delta change per unit change in implied volatility (equivalently, vega change per unit change in underlying price)
* Largest for slightly out-of-the-money options; diminishes deep ITM and deep OTM
* Scales approximately with √T: strong in longer-dated options, near zero for 0DTE
* Fades into expiry as vega collapses
* Positive VEX produces buy flow when vol falls, sell flow when vol rises
* Negative VEX produces sell flow when vol falls, buy flow when vol rises
* Combines with charm during low-vol sessions to produce slow, compounding drift
* Back-end expiry vanna can override front-month GEX support during vol spikes

For a full picture of how vanna interacts with other flows, see the guides on [VEX trading setups](https://www.skylit.ai/learn/vex-trading), [GEX and VEX alignment](https://www.skylit.ai/learn/gex-vex-alignment), [charm](https://www.skylit.ai/learn/charm), and [gamma exposure](https://www.skylit.ai/learn/gamma-exposure).

## Frequently Asked Questions

### What is vanna exposure (VEX)?

Vanna Exposure (VEX) is the aggregate sum of vanna across all open options positions at a given strike. It tells you the direction and magnitude of the hedging flow dealers will produce as implied volatility moves. Positive VEX means dealers buy the underlying when vol falls and sell when vol rises. Negative VEX does the opposite. The sign and location of VEX relative to spot price determine whether volatility moves are stabilizing or destabilizing for price.

### How does vanna affect stock prices?

When implied volatility changes, every option's delta changes with it. Dealers must rebalance their stock hedges to stay delta-neutral, and that rebalancing produces real order flow in the underlying. A dealer carrying positive VEX below spot will mechanically buy stock as IV compresses. That buying has nothing to do with fundamental news. It's a structural consequence of the options book. In calm, low-vol regimes, this flow can sustain a grinding bid for hours or days without any catalyst.

### What is the difference between GEX and VEX?

Gamma exposure (GEX) describes how dealer delta changes as the underlying price moves. It's a price-dimension effect that dominates intraday trading, especially in short-dated options. Vanna exposure (VEX) describes how dealer delta changes as implied volatility moves. It's a vol-dimension effect that becomes dominant in medium-dated options and during volatility compression or expansion events. GEX governs the range; VEX governs the drift. In low-VIX regimes, VEX is often the more important force for multi-day directional bias.

### Why does vanna matter more than gamma for multi-day trades?

Gamma's effect on dealer hedging is strongest at short tenors and close to major strikes. Its influence on a specific price level diminishes quickly as you move away from expiry. Vanna, by contrast, scales with the square root of time to expiry and is largest for medium-dated options in the 30 to 90 DTE range. For trades held over multiple days, the vol path matters as much as the price path. VEX tells you which direction dealer hedging will push the market as IV trends higher or lower, and that directional push compounds over time in a way that front-month GEX can't capture.

### Start Trading Smarter

See these concepts in action with Skylit's dealer exposure tools.

[Get access](https://www.skylit.ai/#pricing)[Try Heatseeker](https://www.skylit.ai/#pricing)
