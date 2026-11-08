<!-- Source: https://www.skylit.ai/learn/dealer-positioning -->

# Dealer Positioning: How Market Makers Move Price

# Dealer Positioning: How Market Makers Move Price

trading·16 min read

dealer-positioningmarket-makersgexmicrostructure

**Dealer positioning is the net options exposure that market makers (dealers) carry at each strike and expiration, and the stock or futures hedging that exposure forces them to do as price moves.** Dealers don't bet on direction; they hedge to stay neutral. When dealer gamma exposure (dealer GEX) is positive, those hedges lean against the move and tend to calm price. When it is negative, the hedges go with the move and tend to speed it up. That is why the strikes where dealer exposure is concentrated are often where price stalls, bounces or accelerates.

## The Casino and the Gambler

Every options market has exactly two sides of the trade, and they play entirely different games.

The **dealer**, the market maker, doesn't take a directional view. Their sole objective is to stay delta-neutral, collect the spread, and earn premium from flow over time. To do that, they hedge mechanically. When they're sold options, they buy or sell the underlying to offset the delta exposure those contracts create. They're the house. They don't bet; they react.

The **gambler**, the customer, fund, or retail trader, buys or sells options to express a directional or volatility view. They want to profit from a move. The larger the move and the closer they are to the right strike, the more their option is worth. But the mechanics of that payoff have a ceiling: once an option is deep in-the-money, delta approaches its maximum value and stops changing. The leverage is gone.

| Role | Objective | Tools | Limitation |
| --- | --- | --- | --- |
| Dealer (Casino) | Stay delta-neutral, extract premium from flow | Hedging stock/futures, vol trades | Must react mechanically to crowd exposure |
| Gambler (Customer/Fund/Trader) | Profit from direction or volatility | Buys/sells calls and puts | Runs out of gamma or delta leverage once ITM |

These two roles are inseparable. Every option the gambler buys creates a hedge the dealer must execute. The dealer's hedging activity then feeds back into price, which is what makes [gamma exposure](https://www.skylit.ai/learn/gamma-exposure) matter so much for understanding market structure.

💡Core Idea

The dealer's hedge isn't optional. When crowd exposure shifts, dealers must rebalance, mechanically, continuously, and in the direction that reinforces or reverses the prevailing trend depending on where spot is relative to major strikes.

## Dealer Gamma Exposure (Dealer GEX)

Dealer gamma exposure, usually shortened to dealer GEX, measures how much the dealers' hedge has to change as price moves. It is worked out strike by strike from the options positions the crowd holds against dealers.

* **Positive dealer GEX:** dealers hedge contra-trend. They buy dips and sell rips, which tends to dampen moves and keep price in a range.
* **Negative dealer GEX:** dealer hedges are pro-cyclical. They sell weakness and buy strength, which tends to amplify moves.

Summed across the chain, GEX tells you which regime the market is in. Mapped strike by strike and expiration by expiration, it shows where the hedging is concentrated: heavy strikes where price tends to stall, bounce or pin, and thin stretches where price can slide through quickly. The sign describes how price tends to move through a level, not which way it goes: a positive node is not bullish and a negative node is not bearish.

One caveat applies to every dealer GEX number you see anywhere. Exchanges don't report dealer positioning. It is derived: a platform has to estimate which side of each position dealers hold and model the exposure that results, so methods differ between platforms. Skylit's [Heatseeker](https://www.skylit.ai/modules/heatseeker) computes it with Skylit's own models from licensed market data, and maps dealer GEX and VEX at every strike and expiration. The [gamma exposure guide](https://www.skylit.ai/learn/gamma-exposure) covers the math behind GEX in more depth, and [GEX tools for 0DTE SPX](https://www.skylit.ai/learn/best-gex-tools-0dte-spx) covers reading dealer GEX on same-day index options.

## Lifecycle of a Strike

Not every options strike on the board matters equally. What drives market impact is where spot is relative to the strikes where most dealer exposure lives. Each strike passes through a predictable lifecycle as price moves toward it.

| Phase | Option Status | Delta | Dealer Hedge | Market Impact |
| --- | --- | --- | --- | --- |
| 1. Far OTM | Speculative chips | Δ ≈ 0 | Almost nothing | Price ignores the node |
| 2. ATM | Maximum sensitivity | Δ ≈ 0.5 | Must adjust rapidly | Volatility explodes; feedback active |
| 3. Deep ITM | Deltas saturated | Δ → 1 or −1 | Fully sized; no more adjustment | Flow stops; feedback collapses |

When an option is far out-of-the-money, its delta is near zero. The dealer needs almost no hedge position. As spot approaches that strike, delta climbs, and every tick of that climb requires the dealer to add or reduce their hedge. This is the zone of maximum dealer activity and maximum market sensitivity. The [options Greeks](https://www.skylit.ai/learn/options-greeks) that govern this, gamma, vanna, charm, all peak near the at-the-money level.

Once an option goes deep in-the-money, the delta has nowhere left to go. It's already at or near one. The dealer's hedge is fully sized. Further price movement in the same direction adds no new hedging pressure. The feedback loop goes quiet.

That three-phase lifecycle is the foundation for understanding why markets accelerate into certain strikes and then abruptly stop.

## What Happens at Negative Exposure

[Negative GEX](https://www.skylit.ai/learn/negative-gex) environments develop when the crowd holds a large number of puts. Here's what the mechanics look like as price falls into those strikes.

When gamblers bought puts earlier, for protection, speculation, or both, they positioned themselves to profit from a decline. As spot falls, their puts move from out-of-the-money toward at-the-money and then into-the-money. Their delta increases, their profit grows, and their leverage is at its peak while the puts are at-the-money.

The dealers who sold those puts are on the other side. When a put's delta increases in magnitude, the dealer, who is short the put, becomes long delta. To stay neutral, they sell stock or futures. That selling adds downward pressure on price. The decline accelerates not because sentiment suddenly worsened, but because mechanical hedging is pro-cyclical in a negative gamma environment.

The key insight is what happens next. Once those puts go deep in-the-money, delta saturates at −1. It stops changing. The dealer no longer needs to sell more stock. The fuel for the decline, incremental hedge selling, disappears.

At the same time, gamblers sitting on large profits begin to close their positions. They sell their puts back into the market. The dealers who take the other side of that close are now buying back the stock they previously sold to hedge. That buyback is a direct reversal force.

## Why Price Reverses: Hedge Exhaustion

When price reaches a major negative exposure cluster, several forces converge to create a reversal. They operate simultaneously and reinforce each other.

**Dealer hedge exhaustion** is the primary driver. Dealers have already sold enough stock to fully hedge the puts in that cluster. Once deltas saturate, there's no incremental sell pressure from hedging. The relentless mechanical selling that drove the decline simply stops. Removing that force, even with no new buying, is enough to cause price to stabilize.

**Gambler profit-taking** adds active reversal pressure. Option buyers close profitable positions by selling their puts. Dealers buy back stock to unwind their hedges. That buying flows directly into the market.

**Charm and theta decay** create a passive drift upward. Options that were at-the-money but didn't move into-the-money lose delta as time passes. Dealers buy stock back to reflect those smaller hedge requirements even with no change in spot.

**Vanna support** adds a volatility-linked bid. After a sharp decline, implied volatility often mean-reverts lower. When IV falls, the delta on puts declines. Positive VEX below spot means dealers buy stock to re-hedge to a smaller delta. See [GEX and trading](https://www.skylit.ai/learn/gex-trading) for more on how vanna shapes these inflection zones.

🎯ELI5

Think of a beach ball pushed underwater. As price falls into a deep negative GEX cluster, it's like pushing that ball further down, pressure builds with every inch. When the ball hits the bottom of the pool (ITM saturation), there's nothing left to push against. The stored pressure releases upward all at once.

## The Gambler-Casino Loop

These mechanics don't occur in isolation. They cycle through predictable phases that repeat across different time frames and different underlying assets. The loop describes the full arc from low-volatility stability to high-volatility capitulation and back to a new equilibrium.

| Phase | Gambler | Dealer | Flow | Outcome |
| --- | --- | --- | --- | --- |
| 1. Vol Low | Sell options | Long vol, long gamma | Buy dips / sell rips | Stability |
| 2. Vol Rising | Buy protection | Short vol, short gamma | Sell dips / buy rips | Acceleration |
| 3. Strike Approached | In profit | Hedge aggressively | Pro-cyclical | Capitulation |
| 4. Deltas Saturate | Cash in | Unwind hedges | Buyback flow | V-reversal |
| 5. Vol Crush | New longs | Long gamma again | Range pin | Melt-up drift |

In Phase 1, dealers are long gamma from gamblers being short options. Their hedging is contrarian: they buy dips and sell rips. Volatility gets suppressed, the range holds, and the market drifts calmly.

In Phase 2, gamblers begin buying protection as volatility rises or a narrative emerges. Dealers are now net short options. Their hedging turns pro-cyclical. Each move begets a larger hedge and a larger subsequent move. Volatility feeds on itself.

In Phase 3, as spot approaches the strike cluster where most of the crowd's puts live, dealers are hedging aggressively in the direction of the move. This is the capitulation zone: where it feels like the bottom is falling out, and mechanically it almost is.

In Phase 4, deltas saturate. Dealers stop selling. Gamblers who bought those puts close for profit. The buyback begins. V-shaped reversals aren't random. They're the mechanical exhaust of a one-sided exposure cluster.

In Phase 5, volatility collapses. Dealers are long gamma again from the fresh options written during the chaos. Their hedging turns contrarian. The range re-establishes and the melt-up begins.

💡Core Idea

The loop isn't random sentiment. It's the mechanical consequence of how options are priced, hedged, and closed. The same structure plays out on a weekly expiration cycle, a monthly cycle, and during major macro events. The scale differs; the mechanics don't.

## Why Big Nodes Far Away Do Nothing

A common mistake is treating every large exposure cluster on the options chain as equally important. A massive put wall two hundred points below spot doesn't constrain price today. It's too far out-of-the-money for its delta to require any meaningful hedge.

The delta of a far OTM option approaches zero. The dealer holds almost no hedge position against it. That strike has no mechanical grip on price. It can't create the buying or selling pressure that produces pinning or acceleration.

What matters is proximity. As spot moves toward that node, its delta begins to grow. The dealer's required hedge grows with it. That growing hedge pressure is what creates the structural effects described throughout this article. Until spot gets close enough for that delta to matter, the node is inert: potential energy that hasn't been activated yet.

Tracking the full [gamma exposure](https://www.skylit.ai/learn/gamma-exposure) profile across all strikes, not just the largest ones, matters for identifying which nodes are live and which are dormant. The active zone shifts continuously as price moves and as time decays OTM options toward zero.

## Real Nodes vs. Hedge Nodes

Not all large exposure clusters matter equally. Hedge nodes are protection, not intent. They sit far OTM, look large in aggregate notional, but don't grow. They were placed as portfolio insurance against tail events and have no directional conviction behind them. Real nodes build over time and strengthen. Growth equals intent. Decay equals protection being rolled or unwound. A tool that can't distinguish between a growing real node and a static hedge node is treating the two as equivalent when they have completely different mechanical implications.

The node lifecycle follows from this. Fresh nodes, those that have accumulated recently and haven't yet been tested by price, produce the strongest reactions when spot approaches. Each time price touches and retreats from a level, the crowd closes some of their positions and dealers unwind the associated hedge. The node weakens. A level that has been tested multiple times is no longer the same structural feature it was when fresh. Displaying this distinction, tracking not just where nodes are but how old they are and whether they're growing or decaying, is what separates current positioning data from a static map of where exposure happened to sit at some point in the past.

In Heatseeker, positive nodes are called Pika nodes and negative nodes Barney nodes. Cell color follows the chosen palette and the node's size, not its sign, so read the number and its minus sign. Velocity Mode layers the rate of change on top, showing which nodes are actively building and which have been stable or are unwinding.

See this in Heatseeker

See exactly where dealers are positioned, positive and negative GEX zones, king nodes, and GEX transition levels, all in real-time.

[Try Heatseeker](https://www.skylit.ai/#pricing)

## Frequently Asked Questions

### What is dealer positioning?

Dealer positioning is the net options exposure market makers carry at each strike and expiration, and the hedging it forces them to do as price moves. Dealers hedge to stay neutral rather than to bet on direction, so their hedging is mechanical. Where that exposure is concentrated, the hedging flows can make price stall, bounce or speed up.

### What is dealer gamma exposure (dealer GEX)?

Dealer gamma exposure (dealer GEX) measures how much dealers' hedges have to change as price moves, strike by strike. Positive dealer GEX means dealers hedge against the move (buying dips, selling rips), which tends to dampen volatility. Negative dealer GEX means their hedges go with the move, which tends to amplify it. Dealer GEX is derived from options data with a model, not reported by the exchanges.

### Where can I see dealer positioning?

Dealer positioning is shown as a map of exposure by strike and expiration. Skylit's [Heatseeker](https://www.skylit.ai/modules/heatseeker) shows dealer GEX and VEX at every strike and every expiration on one board, with a switch between them, the strongest node starred, and Trinity Mode puts SPXW, SPY and QQQ side by side. It shows where dealers are positioned; it doesn't predict direction.

### How do market makers affect stock prices?

Market makers (dealers) affect stock prices through their mechanical delta-hedging activity. When dealers are sold options, they must buy or sell the underlying stock to offset the delta exposure those contracts create. In a positive GEX environment, dealers buy dips and sell rips, suppressing volatility and keeping price in a range. In a negative GEX environment, their hedges are pro-cyclical: they sell as price falls and buy as price rises, amplifying every move. This hedging isn't discretionary. Dealers don't take directional views. Their flow is the direct mechanical consequence of the options positioning the crowd has put on.

### What is dealer hedge exhaustion?

Dealer hedge exhaustion is the point at which dealers have already sold (or bought) all the stock their options exposure requires them to hedge and can't generate any additional mechanical flow in the same direction. It occurs when put deltas approach -1 deep in-the-money: delta is already at its maximum magnitude, so further price movement in the direction of the decline creates no incremental hedging demand. The relentless mechanical selling that drove the move simply stops, not because sentiment reversed, but because the math ran out of room. That removal of sell pressure, even with no new buying, is often enough to stabilize price and trigger a sharp reversal.

### Why do stocks reverse at major options levels?

Stocks reverse at major options levels because of the three-force convergence described in the dealer positioning framework. First, dealer hedge exhaustion stops the incremental mechanical selling that powered the move. Second, gamblers who bought puts close their profitable positions, which forces dealers to buy back the stock they previously sold as hedges. Third, charm and vanna flows add passive reversal pressure as options move deeper ITM and IV mean-reverts. None of these forces require a fundamental catalyst. The reversal is built into the structure of the exposure itself. V-shaped recoveries from major negative GEX levels aren't random. They're the mechanical exhaust of a one-sided exposure cluster hitting its mathematical ceiling.

### What is the casino vs gambler framework?

The casino vs. gambler framework describes the two sides of every options trade and the fundamentally different games they're playing. The dealer (casino) doesn't take directional views. They hedge mechanically, collect the spread, and earn premium over time. Their hedging activity feeds back into price, creating the structural effects GEX captures. The gambler (customer, fund, or retail trader) buys or sells options to express a directional or volatility view, seeking to profit from a move. Their leverage peaks when the option is near at-the-money and collapses once it goes deep in-the-money, which is when the delta stops changing and the gamma feedback loop dies. Understanding which side of the trade you're modeling, whether you're analyzing the casino's mechanical obligations or the gambler's leverage curve, is the foundation for reading options market structure correctly.

### Start Trading Smarter

See these concepts in action with Skylit's dealer exposure tools.

[Get access](https://www.skylit.ai/#pricing)[Try Heatseeker](https://www.skylit.ai/#pricing)
