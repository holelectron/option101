<!-- Source: https://www.skylit.ai/learn/gex-trading -->

# How to Trade with GEX: Nodes, Flip Zones & Scenarios

# How to Trade with GEX: Nodes, Flip Zones & Scenarios

trading·14 min read

gextradingheatseekerdealer-positioning

## Reading the GEX Map

[Gamma exposure](https://www.skylit.ai/learn/gamma-exposure) isn't a single number. It's a landscape. Every strike on the board carries a GEX value determined by the aggregate net notional gamma exposure sitting there and the gamma of those options. When you view a GEX heatmap, you're seeing that landscape all at once: deep greens marking where dealer long gamma creates structural support and resistance, deep reds marking where dealer short gamma removes it.

The first thing to orient yourself on is the sign at spot.

**Positive GEX (+GEX)** means dealers are net long gamma. Their hedges are contrarian. As price rises, they sell; as price falls, they buy. The mechanical flow opposes the market's move. Dips fade, rips fade, and range-bound behavior dominates. The market self-corrects. In Heatseeker, +GEX nodes are referred to as **Pika nodes** (the Academy's "yellow node"). Cell color follows the value, not the sign, so read the number, not the color.

**Negative GEX (–GEX)** means dealers are net short gamma. Their hedges now chase the move. As price falls, they sell more; as price rises, they buy more. That pro-cyclical flow amplifies every tick. Breakouts extend, breakdowns deepen, and the market trends rather than reverts. In Heatseeker, –GEX nodes are referred to as **Barney nodes** (the Academy's "purple node"). A negative node carries a minus sign; the color alone doesn't tell you the sign.

The transition between these two regimes isn't a gradual hand-off. It's a polarity change, and the market behaves accordingly.

🎯ELI5

Think of +GEX as a racetrack with deep gravel traps at the edges. The car can drift toward the wall, but the gravel drags it back. –GEX removes the gravel. The car that reaches the edge accelerates off the track entirely.

## Dealer Hedge Logic

The exact dealer response depends on both GEX and the direction of implied volatility. A dealer who is long gamma in falling-vol conditions behaves differently from one who is long gamma in rising-vol conditions. That difference determines how firm the structural effects actually are.

| Exposure | IV Falling | IV Rising | Dealer Hedge Behavior | Market Feedback |
| --- | --- | --- | --- | --- |
| **+GEX** | Dealers buy dips / sell rips | Still stabilizing (until vol overwhelms) | Mean reversion, range-bound | Dips fade, rips fade |
| **–GEX** | Dealers sell dips / buy rips | Both legs accelerate | Trend and breakout expansion | Dips deepen, rallies overshoot |

When implied volatility is rising in a –GEX environment, there's no natural counterweight. Both the gamma hedge and the vanna-driven delta adjustment point in the same direction. That's when the most violent moves occur: not merely fast, but reflexively self-reinforcing.

When implied volatility is falling in a +GEX environment, the gamma hedge and vol-compression flow both stabilize price. That's the classic melt-up setup: no catalyst, quiet tape, grinding higher because two separate mechanical forces are both bidding.

Understanding how [dealer positioning](https://www.skylit.ai/learn/dealer-positioning) converts options exposure into live market flow is essential context before the scenario matrix below becomes fully intuitive.

## The Core Scenario Matrix

The practical value of a GEX heatmap comes from reading the combination of GEX and VEX at specific locations relative to spot. Four setups define the entire framework.

| Setup | Dealer Flow | Vol Feedback | Market Behavior | Trader Playbook |
| --- | --- | --- | --- | --- |
| **+GEX +VEX Below Spot** | Buy dips + buy as vol falls | Calm reinforces both | Tight range, melt-up | Fade extremes, long pullbacks |
| **+GEX +VEX Above Spot** | Sell rips + sell more as vol rises | Rising vol amplifies suppression | Ceiling thickens; rejections | Fade breakouts; short spikes |
| **–GEX –VEX Below Spot** | Sell dips + sell as vol falls | Both pro-cyclical | Sharp breakdowns | Momentum short, ride continuation |
| **–GEX –VEX Above Spot** | Buy rips + buy more as vol rises | Reflexive loop | Violent short squeezes | Follow breakout continuation |

The top-left cell, **+GEX and +VEX stacked below spot**, is full dealer control. Every dip is caught by two separate buying mechanisms: gamma rebalancing and vol-compression vanna flow. Fade-the-dip works here mechanically, not just anecdotally.

The bottom-left cell, **–GEX and –VEX stacked below spot**, is the panic zone. No mechanical floor. Both dealer flows are pro-cyclical. Trying to fade a selloff here means fighting two simultaneous forces with nothing underneath to help you.

💡Core Idea

The GEX heatmap doesn't predict whether price will move. It predicts how price will behave once it does move. In a +GEX environment, a catalyst that produces a 1% selloff may fade to 0.3% by close. The same catalyst in a –GEX environment may see that 1% extend to 2.5% with no additional news required.

## King Nodes and GEX Polarity Levels

Two specific features of the GEX heatmap produce consistently tradeable setups: king nodes and GEX polarity levels.

**King nodes** are the strikes with the largest absolute GEX in the structure: the highest peaks on the heatmap. More precisely, the King Node is the strike with the largest absolute exposure value, the center of structural gravity for price. The King Node represents where market makers are most likely to pin price at the NYSE close. Dealers carry their largest hedge requirement at these strikes, so price is drawn toward them like a reversion magnet. When spot is far away, king nodes are dormant. As spot approaches, the delta at those strikes starts to matter and dealers ramp hedging in a way that pulls price further toward the node rather than through it. Trading *through* a large king node requires enough momentum to overpower that magnet. It's possible, but the node will fight it. The safer trade is to recognize the magnetic effect and fade the approach rather than chase the break.

**Gatekeeper nodes** are prominent nodes that sit between price and the King Node. They influence whether price can move from one region to another, functioning as checkpoints within the structure. A Gatekeeper doesn't anchor price the way a King Node does, but it determines the ease of transit. If a Gatekeeper holds, price stays contained in the current region. If a Gatekeeper fails, the path to the next major node opens.

**GEX polarity levels** are the strikes where GEX sign changes from positive to negative or negative to positive. Not just neutral ground. These are the locations where the entire dealer hedge orientation inverts. Approaching a GEX polarity level from +GEX territory, the market is being cushioned, then suddenly the cushion disappears. Crossing from –GEX territory into +GEX, momentum that was self-reinforcing suddenly meets contrarian flow.

GEX sign changes produce two signature moves: the rug-pull (spot crosses from +GEX to –GEX and momentum immediately accelerates downward with no further catalyst) and the slingshot (spot crosses from –GEX to +GEX and contrarian flow reverses a fast-moving selloff in a sharp V-shape).

Identifying where GEX sign changes on the heatmap is the single most important step in knowing where structural regime changes are likely to occur. See the [GEX support and resistance guide](https://www.skylit.ai/learn/support-resistance-gex) for how to build levels from these structural features.

## Practical Signal Map

| Signal | Interpretation | Tactical Bias |
| --- | --- | --- |
| **+GEX and +VEX stack under spot** | Full dealer control | Fade dips, expect compression |
| **–GEX and –VEX stack under spot** | Panic zone | Trend following; avoid fading |
| **Crossing a GEX polarity level** | Polarity change | Expect rug-pull or slingshot |
| **Large king node** | Max exposure → reversion magnet | Trade around, not through |
| **Wide air pocket** | Sparse exposure | Expect acceleration |
| **Vol crush + +VEX** | Supportive → rallies sustain | Ride melt-up |
| **Vol spike + +VEX** | Dealer selling → resistance | Fade rally or reduce longs |

Air pockets deserve particular attention. A wide air pocket, a region of the heatmap where GEX is near zero in both directions, is the opposite of a king node. No magnetic pull. No mechanical damping. Price in an air pocket has no structural reason to slow down. When a GEX sign change borders an air pocket, the combination is especially significant: once polarity flips, the acceleration into the air pocket can be extreme.

**Velocity Mode** in Heatseeker tracks the rate of change in dealer positioning, showing how quickly nodes are growing or decaying. Space (an air pocket) plus fuel (high rate of change) equals acceleration. When Velocity Mode shows a rapidly growing node adjacent to an air pocket, that combination is one of the highest-conviction setups in the framework.

The [negative GEX environments guide](https://www.skylit.ai/learn/negative-gex) covers in depth how these air-pocket acceleration events play out through expiration cycles.

See this in Heatseeker

See live GEX maps with king nodes, GEX polarity levels, and scenario overlays, the complete dealer exposure picture.

[Try Heatseeker](https://www.skylit.ai/#pricing)

## Frequently Asked Questions

### How do you trade using GEX heatmaps?

You start by identifying the sign of GEX at spot. Positive GEX means dealers are long gamma and their hedges are contrarian, so you fade extremes and buy pullbacks. Negative GEX means dealers are short gamma and their hedges are pro-cyclical, so you trade with momentum, not against it. From there you locate the nearest king nodes, check for air pockets, and identify any GEX polarity levels between spot and your target. The heatmap isn't a directional signal by itself; it's a behavioral signal. The correct workflow is to start with chart structure, form a thesis from price action, then use the heatmap to confirm or challenge it. The map tells you why structure exists mechanically and how durable it's likely to be.

### What is a King Node on a GEX map?

A King Node is the strike with the largest absolute GEX value in the current structure, the peak of the heatmap. It represents where market makers are most likely to pin price at the NYSE close because dealers carry their largest hedge requirement at these strikes. As price approaches a King Node, the delta at that strike begins to matter and dealers ramp hedging in a way that pulls price toward the node rather than through it, creating a gravitational or magnetic effect. Trading through a large King Node requires enough momentum to overpower that magnetic pull. The safer trade is to recognize the magnetic effect and fade the approach rather than chase the break. A first-tap on a fresh King Node carries roughly 80% reaction probability.

### What happens when GEX and VEX are both positive below spot?

When both GEX and VEX are positive below spot, you're in a state of full dealer control on two separate hedging dimensions. The gamma hedge means dealers buy dips as price falls. The vanna hedge means dealers also buy as implied volatility drops. Both forces push in the same direction. Dips get caught by two independent mechanical buying flows, not just one. This is the setup behind the classic low-volatility melt-up: no catalyst, quiet tape, grinding higher because two separate mechanical forces are both bidding. Fade-the-dip works here mechanically. The playbook is to fade extremes, expect compression, and avoid directional breakout bets unless a catalyst is strong enough to overwhelm both layers of dealer buying simultaneously.

### What is an air pocket in GEX analysis?

An air pocket is a region of the GEX heatmap where exposure is near zero in both directions, the opposite of a King Node. With no meaningful GEX at those strikes, dealers have almost no hedge obligation there and the mechanical damping that normally slows price disappears. Price in an air pocket has no structural reason to slow down. When a GEX sign change borders an air pocket, the combination is especially significant: once polarity flips, the acceleration into the air pocket can be extreme. Velocity Mode in Heatseeker tracks the rate of change in dealer positioning, and a rapidly growing node adjacent to an air pocket is one of the highest-conviction setups in the framework because space plus fuel equals acceleration.

## Regime Day Types

The GEX regime at the open predicts the character of the day more reliably than most other inputs. Three day types cover the majority of sessions:

**Range/Choppy Day:** Positive gamma predominates. Dealer hedges are contrarian. Dips are bought mechanically, rips are sold mechanically, and the tape oscillates inside the structure. The playbook is to fade extremes and expect mean reversion.

**Trend Day:** Negative gamma with rapid node accumulation and rolling floors/ceilings. Dealer hedges are pro-cyclical. Each new low (or high) builds momentum rather than reversing it. New nodes form quickly as positioning shifts, and what was resistance becomes support (or vice versa) as the structure migrates in the direction of the move. The playbook is to follow the structure, not fade it.

**Whipsaw Day:** Negative gamma combined with air pockets and conflicting signals across indices. The most dangerous tape. Fast moves in both directions that each look decisive but reverse quickly. No sustained directional momentum. Index divergence signals this from the open: when SPY and QQQ gamma readings point in opposite directions, the probability of a Whipsaw Day is elevated.

## Node Lifecycle and Tap Strength

Nodes are not static. Each interaction weakens the level. Fresh nodes produce the strongest reactions, and that strength decays with use.

A useful approximation: the **1st tap** on a node carries roughly 80% reaction probability. The **2nd tap** drops to around 66%. The **3rd tap** falls to about 33%. If you're trading a third test of a level, you're trading a weakening level. The structural thesis is valid, but the mechanical edge is materially lower than it was on the first contact. Position size should reflect that decay.

New nodes that have never been tested carry maximum structural weight. A king node or Gatekeeper that prints fresh in the session and gets tested immediately is the highest-probability setup in the framework. The inverse also holds: a node that has been tapped three or more times and is still present has absorbed significant pressure. It may be resilient, but the easy mechanical edge has been extracted.

## Charts First

Heatseeker is a confirmation tool, not a prediction engine. The correct workflow is: start with chart structure. Form your thesis from price action first, then check Heatseeker to confirm or challenge it. The map confirms or challenges your thesis. It isn't the thesis itself.

A common mistake is to open the heatmap, find a prominent node, and build a trade around it without first asking what the chart says. This inverts the process. The chart tells you what the market has done and where structure exists in price. The GEX map tells you why that structure exists mechanically and how durable it is likely to be. Together they're powerful. The heatmap alone can produce confirmation bias: you will find a node to justify almost any directional view if you look for one.

## The Casino Mental Model

The most useful frame for reading a GEX heatmap consistently: every structure on the map belongs to a casino table, not a directional prediction.

* **The dealer is the casino.** The house doesn't bet on direction. It reacts mechanically to maintain neutrality and extract spread. Its hedges aren't opinions, they're obligations.
* **GEX is the table shape.** The geometry of how the ball rolls: whether the table slopes back toward center (+GEX) or toward the edges (–GEX).
* **VEX is gravity.** How quickly the ball accelerates or decelerates as it rolls. Positive gravity pulls it back toward equilibrium. Negative gravity lets momentum compound.
* **Vol is the energy in the system.** How far any given push will carry before natural damping takes over. High vol means every nudge travels farther.
* **The trade is a bet on who hedges next.** You aren't predicting price, you're positioning ahead of the forced mechanical flows that dealer hedging will produce when price reaches the next meaningful strike.

This reframe resolves a common confusion: why the GEX heatmap isn't a directional signal but a behavioral signal. Two setups can both have price moving higher, but if one is in a +GEX ceiling and the other is in a –GEX air pocket, the dealer flow in each case produces entirely different outcomes. Same direction. Opposite mechanics.

Reading the map well means asking not "which way is price going?" but "when price moves, which dealers will be forced to hedge, in which direction, and how much?" Those answers are already visible in the heatmap, stacked in the exposure of every node between spot and wherever the next structural feature sits.

### Start Trading Smarter

See these concepts in action with Skylit's dealer exposure tools.

[Get access](https://www.skylit.ai/#pricing)[Try Heatseeker](https://www.skylit.ai/#pricing)
