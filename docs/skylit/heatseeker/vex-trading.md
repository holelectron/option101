<!-- Source: https://www.skylit.ai/learn/vex-trading -->

# How to Trade with VEX: Vanna Flows & Vol Regimes

# How to Trade with VEX: Vanna Flows & Vol Regimes

trading·10 min read

vextradingvannaheatseeker

## Reading the VEX Map

[Vanna Exposure (VEX)](https://www.skylit.ai/learn/vanna-exposure) is the aggregate dealer hedging sensitivity to implied volatility across all open options positions. When IV moves, dealers must rebalance their delta hedges. The direction, size, and speed of that rebalancing is what VEX quantifies. Reading the map means identifying the sign of VEX at each strike, its location relative to spot, and the vol regime currently in play.

Two variables determine everything: the sign of VEX (positive or negative) and whether that exposure sits above or below spot.

**Positive VEX** means dealer delta requirements increase as vol rises. When vol falls, dealers reduce their hedge, they become buyers. When vol rises, dealers add to their hedge, they become sellers. Positive VEX is stabilizing in a vol compression environment and destabilizing when vol expands.

**Negative VEX** is the mirror. Dealer delta requirements decrease as vol rises. When vol falls, dealers sell. When vol rises, dealers buy. Negative VEX creates fragile conditions in calm markets and reflexive buying during vol spikes.

The location of that exposure relative to spot determines whether the flow acts as support, resistance, a floor, or a ceiling. A large VEX node sitting thirty points below spot has entirely different implications than the same node sitting thirty points above, even if the sign is identical.

💡Core Idea

VEX has no fixed direction. The same positive VEX that held the market up through an entire low-vol session becomes sell flow the moment the VIX starts climbing. Before taking any trade based on VEX, identify whether you're in a vol compression or vol expansion regime. That's what determines which side of the exposure dealers are acting on.

## VEX Scenario Matrix

The four core setups each carry a distinct flow logic, feedback loop, and trader response.

| Setup | Dealer Flow | Vol Feedback | Market Behavior | Trader Playbook |
| --- | --- | --- | --- | --- |
| **+VEX Below Spot** | Buys as vol drops → support | Sells if vol spikes → rug risk | Strong base in calm, rug-pull in stress | Buy dips in calm; cut fast if VIX rises |
| **–VEX Below Spot** | Sells in calm → weak floor | Buys in stress → fast bounces | Fragile in calm, reflexive in panic | Short rallies in calm; scalp long in panic |
| **+VEX Above Spot** | Buys as vol drops → dissolves resistance | Sells if vol rises → caps breakouts | Breakouts sustain in vol compression; fail when vol expands | Buy breakout only if vol falling; fade if VIX surges |
| **–VEX Above Spot** | Sells in calm → soft ceiling | Buys in stress → squeeze fuel | Capped in calm; launches during vol spike | Short pops in calm; flip long on vol breakout |

Each dealer flow entry is conditional on the prevailing vol direction, not a static description. The flows are mechanical and largely predictable. What changes is which side of that condition is active right now.

**+VEX Below Spot** is the most common setup in sustained low-vol tapes. Every tick lower in the VIX generates incremental dealer buying beneath the market. That buying has no fundamental anchor, it's pure hedge rebalancing. The risk is that it inverts instantly when vol spikes. The same mechanism that produced the supportive bid flips to sell flow when IV surges, and there's no warning other than the vol move itself.

**–VEX Below Spot** is the structural setup for choppy, fragile floors. Dealers are net sellers when calm, preventing the market from establishing any stable bid. The floor only appears during stress events, when vol spikes flip dealer flow to the buy side. This regime produces sharp V-bounces during panic that feel counterintuitive: the market falls hard, then reverses violently, not because of fundamental buyers, but because vol expansion triggered mechanical dealer buying.

**+VEX Above Spot** dissolves overhead resistance as IV falls. What looked like a cap is actually a function of vol level. When IV is elevated, dealer selling maintains the ceiling; when IV compresses, that ceiling melts. Breakouts through these levels in vol compression environments are cleaner and more sustained than they appear on a price chart alone.

**–VEX Above Spot** creates an elastic cap in calm and a squeeze generator in stress. In low-vol conditions, dealers sell into any approach of this level. If vol then expands, either organically or through a catalyst, those same dealers become buyers, providing the fuel for fast, violent squeezes through overhead levels.

## The Breakout Paradox

The +VEX above spot setup creates a genuine paradox for anyone trying to trade breakouts mechanically. The setup says: dealers buy as vol drops, so buy breakouts in vol compression and fade if VIX surges. But the breakout itself is a vol event, the move through resistance often generates an IV spike. Does that mean all breakouts through +VEX resistance are fades?

Not exactly. The mechanics unfold in sequence, and the gap between sequence steps is where opportunity lives.

When price breaks through a +VEX level, the move itself generates the vol spike. Dealer selling, the resistance, comes slightly after the breakout, as the IV increase propagates through their delta models and forces a hedge adjustment. If the selling flow that follows is absorbed by real directional demand, genuine buyers stepping into the move, the dealers' selling pressure is neutralized. IV then starts to compress again, and the +VEX resistance that briefly hardened starts dissolving. Traders describe this as a breakout that sticks: price breaks through, consolidates briefly as dealer selling is absorbed, then drifts through the level cleanly on vol crush.

If that selling flow isn't absorbed, if there's no real demand behind the breakout, the dealer selling adds to supply at the wrong moment. Vol expands rather than compresses. The +VEX resistance hardens further. The breakout fails.

🎯ELI5

Think of +VEX resistance above spot as a spring-loaded gate. In vol compression it's lightly latched, a steady push opens it. When vol expands, a mechanism tightens the latch. The breakout is the push. Whether the gate opens or bounces you back depends on how quickly vol responds and whether demand is there to absorb the tightening.

The practical rule: buy breakouts through +VEX resistance only when IV is already falling or flat. Avoid buying breakouts when IV is rising into the move, that's when +VEX resistance is strongest, and the dealer selling will compound rather than absorb. The vol regime at the moment of the break matters more than the price action itself.

## Cross-Expiry Dynamics

VEX isn't a single-expiry phenomenon. The full expiration surface determines the aggregate dealer flow, and the balance between front-end and back-end vanna shifts dramatically with the vol environment.

| Expiry Zone | Dominant Greek | Role in Flow | Vol Spike Impact |
| --- | --- | --- | --- |
| **0–2 DTE** | Gamma | Mechanical intraday hedging | Minimal vanna contribution |
| **7+ DTE** | Vanna | Vol regime steering | High sensitivity to IV moves |

Front-month and same-day options carry most of the intraday gamma exposure. Their vega, and therefore their vanna, is negligible. These options create the mechanical hedging pressure that produces tight ranges and pin effects around major strikes. But they tell you almost nothing about the vol-driven flow that builds up and releases over hours and days.

The back-end expirations, roughly seven days and beyond, are where vanna accumulates. These options still carry meaningful vega, so their delta is substantially sensitive to IV changes. When vol spikes, back-end +VEX creates significant sell flow that's entirely invisible in a front-month gamma map. A market that looks well-supported by +GEX on the day's expiration can experience a sharp rug-pull once far-expiry vanna flips to sell flow from the vol spike.

The reverse is equally powerful: vol crush with large far-dated +VEX reinforces front-month +GEX. Both forces push in the same direction. A multi-day pin that compounds intraday, price barely moves, drifts fractionally higher each session, feels immune to selling. Not random. That's gamma pin and vanna drift working simultaneously from different expiry layers.

Reading the cross-expiry VEX surface before positioning for a multi-day trade matters more than any single strike's net notional exposure. The aggregate far-expiry vanna, particularly from 30 to 90 DTE options, determines whether a support level can hold through a vol expansion event or will crack.

## Vanna Drift

The most actionable expression of positive VEX in a calm market is vanna drift: the slow, sustained, catalyst-free upward creep produced by IV compression mechanically forcing dealers to buy back hedges.

The mechanism is direct. Dealers who are short options carry +VEX. As IV falls, those options' deltas decrease, the dealer no longer needs as much stock to stay delta-neutral. They reduce the hedge by buying stock back. That buying produces upward price drift with no news, no breakout, and no change in the fundamental picture. The move is entirely a flow artifact.

Vanna drift is most consistent in the hours following a vol compression event: after a spike has faded, after an expiration removes near-term uncertainty, or simply during slow mid-week sessions in a low-VIX regime. It combines naturally with [charm](https://www.skylit.ai/learn/charm) drift in the same regimes, where time decay simultaneously reduces delta requirements and forces a parallel set of buybacks. The two flows stack, producing a grinding bid that can last a full session or longer.

The signal to watch for vanna drift isn't price action, it's the VIX. When VEX is positive and the VIX is falling intraday, the drift is active. Trying to short that tape on technicals alone means trading against a mechanical flow that won't stop until the vol move stops. The drift ends when IV stabilizes or reverses, not before.

**Velocity Mode** extends this by tracking the rate of change in dealer vanna positioning in real-time. A vanna node that is growing rapidly signals accumulating dealer urgency that the static VEX map alone won't surface. When Velocity Mode shows a positive VEX cluster below spot expanding quickly during a vol compression session, the drift setup has structural momentum behind it. When that same cluster is decaying, the drift is approaching exhaustion. **Trinity Mode** lets you verify alignment across SPXW, SPY, and QQQ simultaneously, confirming whether the vanna structure is coherent across the full index options complex before committing to a multi-day drift trade.

For a full picture of how VEX interacts with other dealer flows, see the guides on [vanna exposure mechanics](https://www.skylit.ai/learn/vanna-exposure), [GEX and VEX alignment](https://www.skylit.ai/learn/gex-vex-alignment), [charm drift](https://www.skylit.ai/learn/charm), and [GEX trading setups](https://www.skylit.ai/learn/gex-trading).

See this in Heatseeker

See vanna exposure (VEX) across all strikes and expirations, identify drift zones, rug-pull risk, and breakout conditions, with Velocity Mode and Trinity Mode.

[Try Heatseeker](https://www.skylit.ai/#pricing)

## Frequently Asked Questions

### How do you trade VEX (vanna exposure)?

VEX trading starts by identifying two things: the sign of VEX at each strike and whether that exposure sits above or below spot. The sign and location determine whether the dealer flow acts as support, resistance, a floor, or a ceiling. In a vol compression environment, positive VEX below spot means dealers are buying as IV drops, creating a mechanical bid. Positive VEX above spot dissolves overhead resistance as IV falls, making breakouts cleaner. The vol regime is the critical input before any VEX trade. The same positive VEX that held the market up through an entire low-vol session becomes sell flow the moment the VIX starts climbing. You need to identify whether you're in vol compression or vol expansion first, because that's what determines which side of the exposure dealers are acting on.

### What is the breakout paradox in VEX trading?

The breakout paradox describes the conflict that arises when trading breakouts through positive VEX resistance above spot. The setup says to buy breakouts only when IV is falling, because that's when dealer selling at +VEX levels is weakest. But the breakout itself is a vol event and often generates an IV spike, which is exactly when +VEX resistance is strongest. The resolution is that the mechanics unfold in sequence. The IV spike from the breakout triggers dealer selling slightly after the initial move, as the vol increase propagates through dealer delta models. If genuine directional demand is present to absorb that selling, IV starts compressing again, the +VEX resistance dissolves, and the breakout sticks. If there's no real demand behind the move, the dealer selling adds to supply and the breakout fails. The practical rule is to buy breakouts through +VEX resistance only when IV is already falling or flat at the moment of the break.

### How does cross-expiry VEX affect multi-day trades?

Front-month and same-day options carry most of the intraday gamma exposure but almost no vanna, so they don't contribute meaningfully to VEX. Back-end expirations at roughly seven days and beyond are where vanna accumulates, because those options still carry significant vega and their delta is substantially sensitive to IV changes. A market that looks well-supported by +GEX on the current day's expiration can experience a sharp rug-pull once far-expiry vanna flips to sell flow from a vol spike. Conversely, vol crush combined with large far-dated +VEX reinforces front-month +GEX so that both forces push in the same direction, creating the multi-day pin where price barely moves but drifts fractionally higher each session. Reading the full cross-expiry VEX surface before entering a multi-day trade matters more than any single strike's net notional exposure, because the aggregate far-expiry vanna determines whether a support level can hold through a vol expansion event or will crack.

### Start Trading Smarter

See these concepts in action with Skylit's dealer exposure tools.

[Get access](https://www.skylit.ai/#pricing)[Try Heatseeker](https://www.skylit.ai/#pricing)
