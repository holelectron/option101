<!-- Source: https://www.skylit.ai/learn/charm -->

# Charm: The Invisible Drift That Moves Markets

# Charm: The Invisible Drift That Moves Markets

greeks·7 min read

charmgreeksvanna

## What is Charm?

**Charm** measures how [delta](https://www.skylit.ai/learn/delta) changes as time passes, holding price and implied volatility constant. It's sometimes called delta decay, because it describes how a dealer's hedge erodes with every hour that passes, even when the underlying doesn't move.

As time passes, the [options greeks](https://www.skylit.ai/learn/options-greeks) shift: an out-of-the-money call loses delta as expiry approaches. For puts, the delta becomes less negative, drifting toward zero. In both cases, dealers holding stock or futures as hedges find those hedges are now too large for the delta they need to carry.

🎯ELI5

Charm is cruise control adding slow throttle. The road hasn't changed, the speed limit hasn't changed, but the car is quietly adjusting power in the background to hold a target. Dealers are doing the same thing: incrementally buying or selling stock as their delta targets drift with time.

## How Charm Drives Dealer Flow

| Role | Behavior |
| --- | --- |
| **Dealer (long calls)** | As call delta shrinks with time, dealer reduces long stock hedge, but if they are short the calls, they buy stock to maintain a flat book |
| **Net effect in +GEX regimes** | Dealers rebalance toward higher delta by buying, producing slow upward drift into high-exposure strikes |

This rebalancing happens **without any price move and without any vol move**. Charm is purely a function of time. Even on a completely flat, quiet tape, a dealer's hedge requirement is shifting beneath the surface.

Charm is strongest for options that are close to at-the-money and close to expiration. Deep in-the-money or far out-of-the-money options see very little charm because their deltas are already near 1 or 0 respectively. Long-dated options have negligible charm. The decay is too slow to drive intraday flow.

## Afternoon Drift

Because charm is time-driven, its effects concentrate in the afternoon. As the session progresses, more time-value has decayed. In low-VIX regimes, when the tape is quiet and dealers aren't being forced to hedge large price moves, charm becomes the dominant flow mechanism in the final hours before close.

The observed pattern: price grinds slowly toward the strike with maximum options positioning. This is sometimes called **pinning**, but drift is more accurate. Dealers aren't defending a level. They're mechanically rebalancing their books toward a position that requires less stock.

💡Core Idea

Charm is strongest near ATM and close to expiry, and weakest for deep ITM/OTM options and long-dated contracts. In calm sessions, the afternoon tape is often charm-dominated: slow, grindy, hard to short, with no obvious catalyst.

## Vanna and Charm Drift

Charm rarely works in isolation. In calm, low-volatility sessions it combines with [vanna exposure](https://www.skylit.ai/learn/vanna-exposure) to produce what traders describe as a steady upward "melt."

* **Vanna Drift:** When implied volatility compresses, dealers who were long vega buy back their hedges. Upward price drift follows, proportional to the size of the positive vanna exposure in the market.
* **Charm Drift:** Separately, time decay reduces deltas. Dealers rebalance by buying. More upward drift, no vol move required.

When both are present, falling IV and passing time, the flows stack. Each mechanism is individually small, but together they can sustain a grinding bid for hours.

### Cross-Expiry Interactions

The interaction across expiration dates matters especially when 0DTE gamma dominates the headline conversation. Even as same-day options drive the intraday range with large gamma swings, longer-dated vanna exposure adds a background buy flow during vol compression that's invisible in 0DTE gamma maps alone. In vol spikes, that same longer-dated vanna flips to sell flow, overriding whatever short-term gamma exposure support was present.

Tracking the full expiration surface, not just the front date, gives a more complete picture of where dealer rebalancing flow is pointing.

See this in Heatseeker

Track how charm-driven drift interacts with GEX/VEX positioning across expirations in Heatseeker.

[Try Heatseeker](https://www.skylit.ai/#pricing)

## Key Properties

* Measures delta change with time, holding price and vol constant
* OTM call delta falls; put delta rises (less negative). Dealers rebalance in both cases
* Strongest near ATM close to expiry; negligible for deep strikes and long-dated options
* Shifts the dealer hedge intraday with no price or vol move required
* Combines with vanna in low-VIX sessions to produce slow afternoon drift toward peak exposure strikes

## Frequently Asked Questions

### What is charm in options trading?

Charm measures how an option's delta changes as time passes, with price and implied volatility held constant. Because delta shifts with each passing hour, dealers who are delta-hedging must continuously rebalance their stock positions even when the underlying hasn't moved. This time-driven rebalancing produces real order flow in the underlying. For out-of-the-money calls, delta falls as expiry approaches. For puts, delta becomes less negative. In both cases dealers adjust their hedges, and those adjustments create systematic buy or sell pressure in the underlying.

### What causes afternoon drift in the stock market?

In low-VIX regimes, charm is one of the primary drivers of the slow, grinding price action seen in the final hours of a session. As the trading day progresses, more time-value has decayed and more charm-driven rebalancing has accumulated. Dealers aren't defending a level or responding to news. They're mechanically adjusting their books toward a smaller hedge requirement. The result is price that drifts quietly toward the strike with maximum options positioning. Charm is strongest near at-the-money strikes and close to expiration, so its effect concentrates in the afternoon on days with weekly expiry nearby.

### How do charm and vanna work together?

Charm and vanna are both silent, catalyst-free sources of dealer flow. Charm operates purely through time: delta shifts as expiry approaches, regardless of what price or vol does. Vanna operates through implied volatility: delta shifts as IV compresses or expands. In a low-vol session where IV is slowly drifting lower while time is passing, both forces push in the same direction. Each mechanism is individually modest, but together they can sustain a compounding bid for an entire session. Traders who recognize both forces are working simultaneously understand why the tape can feel impervious to selling even with no obvious news or order flow catalyst.

### Start Trading Smarter

See these concepts in action with Skylit's dealer exposure tools.

[Get access](https://www.skylit.ai/#pricing)[Try Heatseeker](https://www.skylit.ai/#pricing)
