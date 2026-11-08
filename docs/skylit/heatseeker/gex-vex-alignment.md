<!-- Source: https://www.skylit.ai/learn/gex-vex-alignment -->

# GEX vs VEX: When Greeks Align and When They Fight

# GEX vs VEX: When Greeks Align and When They Fight

trading·12 min read

gexvextradingheatseeker

## What is Alignment?

[Gamma Exposure (GEX)](https://www.skylit.ai/learn/gamma-exposure) and [Vanna Exposure (VEX)](https://www.skylit.ai/learn/vex-trading) are two distinct dealer hedging forces. GEX governs how dealers respond to price movement: buying dips and selling rips when long gamma, or chasing moves when short gamma. VEX governs how dealers respond to implied volatility movement, adding or reducing stock hedges as IV rises and falls.

Most of the time these two forces operate in parallel. When they point in the same direction, dealer flows reinforce each other and market behavior becomes predictable. When they point in opposite directions, they compete, and you get the jerky, confusing price action that traps one-directional traders.

**GEX/VEX alignment** describes the degree to which these two hedging dimensions are cooperating or fighting across the options surface. Understanding alignment tells you not just what the market is likely to do, but how *stable* that behavior will be.

🎯ELI5

GEX is the hand brake; VEX is the slope of the hill. When both point the same way, you roll steadily: either slowing to a controlled stop or accelerating down the grade. When they fight, you alternately lurch and stall. The car isn't broken. Two mechanical forces are just working against each other.

## The Four States

Every market at any given moment sits in one of four alignment states. The combination of GEX sign and VEX sign determines the expected character of dealer flow and therefore the expected character of price action.

| Alignment State | What It Means | Dealer Flow | Market Behavior | Example |
| --- | --- | --- | --- | --- |
| **Aligned (+GEX, +VEX)** | Long gamma and long vanna | Buy dips, sell rips; buy when vol drops | Stable, supportive drift | Classic low-VIX melt-up; SPX pinning days |
| **Aligned (–GEX, –VEX)** | Short gamma and short vanna | Sell dips, buy rips; sell when vol drops | Pro-cyclical acceleration, elevated vol | Trend days, gap-and-go selloffs |
| **Misaligned (+GEX, –VEX)** | Long gamma but short vanna | Buy dips, yet sell when vol drops | Conflicting hedges, range with sudden breaks | Choppy regime where calm fades fail |
| **Misaligned (–GEX, +VEX)** | Short gamma but long vanna | Sell dips, but buy when vol drops | Short-term volatility with long-term support | Panic lows that bounce violently next session |

The aligned states are easier to trade. In +GEX/+VEX, dealers are mechanically long on both dimensions: they stabilize price and add a bid on vol compression. In –GEX/–VEX, both forces amplify every move, directional participants get rewarded and mean-reversion strategies get punished.

The misaligned states are where strategy selection matters most. +GEX/–VEX looks calm on the surface but hides a ceiling: gamma holds price in a range while negative vanna quietly suppresses rallies as vol compresses. –GEX/+VEX looks dangerous but contains a self-correcting mechanism: short gamma accelerates the initial drop while positive vanna below spot creates mechanical buying when IV eventually fades.

## Why Misalignment Happens

Misalignment isn't random noise. It has structural causes rooted in how options expirations are layered across the term structure.

**Time Skew.** The GEX signal is dominated by 0DTE and 1DTE options, where gamma per dollar of notional is explosive. The VEX signal is dominated by options 5 to 30 days out, where vanna is meaningful but gamma is modest. When short-term and medium-term option flows diverge, as they do before major events, during expiration weeks, or after large positioning rotation, GEX and VEX can point in opposite directions even in an otherwise coherent market.

**Skew Asymmetry.** Put options carry significantly higher vanna than equivalent calls because the put skew is steeper. A market where protective put buying has been heavy will carry elevated positive VEX below spot regardless of where GEX sits. Downside vanna exposure can persist through multiple GEX sign changes simply because the put positioning is stickier.

**OI Rotation.** As front-month expiries roll off, their GEX contribution collapses rapidly, gamma scales as 1/√T and short-dated GEX is nearly zero immediately after expiration. VEX from the same expiry decays more slowly and the longer-tenor options that dominate VEX remain on the board unchanged. The days immediately following a large expiry often show misalignment purely as a mechanical consequence of this differential decay.

**Vol Regime Change.** A sudden spike in implied volatility alters vanna sign faster than GEX updates. When IV jumps, the delta sensitivity of options changes rapidly, particularly for OTM puts, while the dealer's gamma position, which is driven by existing options positioning, adjusts more slowly. You get a temporary state where GEX says one thing and VEX says another, until new options flow re-establishes coherent positioning.

## Reading Alignment on the Map

Alignment isn't just a market-level concept, it applies strike by strike. The most useful analysis examines the GEX and VEX contributions at the same price levels, particularly at or near current spot.

| Observation | Interpretation | Expected Flow | Trade Implication |
| --- | --- | --- | --- |
| **+GEX and +VEX in same region** | Dealer control on both dimensions | Pin and drift | Fade extremes; buy-the-dip |
| **–GEX but +VEX below spot** | Gamma short, vanna supportive | Vol crush rebound likely | Long into panic lows |
| **+GEX but –VEX above spot** | Gamma pins but vanna suppresses rallies | Ceiling holds until vol collapses | Short rips in calm |
| **GEX flat, VEX dominant** | Low delta convexity | Price follows VIX flow | Trade vol regime, not direction |
| **GEX/VEX polarity shift at same strike** | GEX transition confirmed | Directional acceleration | Use as breakout trigger |

The most powerful signal is when GEX and VEX flip sign at the same strike. A level where dealers transition from long gamma to short gamma *and* from long vanna to short vanna simultaneously is a structural breakout zone. Once price clears that level, both hedging forces reverse: the dealer who was buying dips is now chasing, and the vanna support that was cushioning vol expansion is now amplifying it. Moves through a confirmed GEX/VEX polarity shift are self-sustaining.

The opposite, a region of deeply aligned +GEX and +VEX, is the structural pinning zone. Two independent hedging mechanisms are both adding buy flow on weakness and sell flow on strength. Breaking out from this region requires a catalyst large enough to overwhelm both forces simultaneously.

**Trinity Mode** extends this alignment analysis across instruments. It displays dealer exposure side by side for SPXW, SPY, and QQQ by default, and you can change the instruments. Because these instruments share underlying price but carry distinct options positioning distributions, Trinity Mode shows whether the GEX/VEX alignment signal is coherent across all three or limited to one instrument. The Academy framework for reading Trinity Mode alignment: full alignment (all three agree) represents high-probability conditions. Partial alignment (two of three agree) is the bare minimum for a trade. Divergence across all three means no trade or significantly reduced size.

See this in Heatseeker

See GEX and VEX alignment in real-time, identify whether dealer flows are cooperating or fighting across the entire options surface, with Trinity Mode for cross-instrument alignment.

[Try Heatseeker](https://www.skylit.ai/#pricing)

## Practical Playbook

Understanding alignment changes how you approach each session.

**When aligned and positive (+GEX/+VEX):** Fade extremes. The range is likely to hold and vol compression is your ally. Dip-buying works because both gamma and vanna are mechanically supportive. Avoid directional breakout bets unless a catalyst is strong enough to overwhelm two layers of dealer buying. This is the environment that produces the grindy, low-range melt-ups that frustrate directional traders.

**When aligned and negative (–GEX/–VEX):** Trade with momentum, not against it. Dealers are selling dips and vol expansion makes vanna a further drag on any recovery. Mean-reversion strategies fail here. Trend-following and gap-and-go setups have structural support from dealer flow. Reduce position size because the vol amplification cuts both ways.

**When misaligned (+GEX/–VEX):** Expect a choppy, directionless range with occasional sharp downside breaks. Gamma stabilizes intraday price, but negative vanna means any vol compression, which normally fuels rallies, instead produces sell flow. Calm fades will underperform. Trade the range while it holds and treat any break from it as potentially self-sustaining rather than mean-reverting.

**When misaligned (–GEX/+VEX):** This is the panic-low template. Short gamma accelerates the initial selloff and produces the fear-driven vol spike. But positive vanna below spot means that once implied volatility eventually fades, as it almost always does after a spike, dealer buying flows mechanically. The setup favors being long into the panic with a defined-risk structure, particularly when VIX is elevated and large positive VEX sits at or below current spot. Violent next-session reversals are the mechanical consequence of this configuration.

In all cases, the alignment analysis supplements, not replaces, a read on overall market context. For an understanding of how [GEX levels](https://www.skylit.ai/learn/gex-trading) set individual support and resistance zones, and how [VEX flows](https://www.skylit.ai/learn/vex-trading) interact with the volatility surface, those articles provide the underlying mechanics. The alignment lens connects the two into a single coherent picture of where dealer flows are pulling simultaneously.

For the structural foundations of how GEX levels create [support and resistance](https://www.skylit.ai/learn/support-resistance-gex), see that guide alongside this one.

## Frequently Asked Questions

### What does GEX/VEX alignment mean?

GEX/VEX alignment describes whether gamma exposure and vanna exposure are cooperating or competing at the same price levels. GEX governs how dealers respond to price movement: buying dips and selling rips when long gamma, or chasing moves when short gamma. VEX governs how dealers respond to implied volatility movement, adding or reducing hedges as IV rises and falls. When both forces point in the same direction, dealer flows reinforce each other and market behavior becomes predictable. Positive alignment (both GEX and VEX positive) means two independent buying mechanisms catch dips simultaneously, producing the low-volatility melt-up. Negative alignment (both negative) means two pro-cyclical forces amplify every move. Alignment tells you not just what the market is likely to do, but how stable that behavior will be.

### Why do GEX and VEX sometimes disagree?

GEX and VEX disagree because they're driven by different parts of the options term structure on different timescales. GEX is dominated by 0DTE and 1DTE options where gamma is explosive but vanna is negligible. VEX is dominated by options five to thirty days out where vanna is meaningful but gamma is modest. Before major events, during expiration weeks, or after large positioning rotations, these two cohorts can point in opposite directions. Skew asymmetry also contributes: put options carry significantly higher vanna than equivalent calls because put skew is steeper, so heavy protective put buying can sustain positive VEX below spot through multiple GEX sign changes. Vol regime changes cause temporary misalignment too, because IV shifts alter vanna sign faster than GEX updates as existing options positioning adjusts more slowly.

### How do you trade when GEX and VEX are misaligned?

The two misaligned states call for different approaches. In +GEX/negative VEX, gamma stabilizes intraday price but negative vanna means any vol compression, which normally fuels rallies, instead produces dealer sell flow. Calm fades underperform. The range holds while it holds, but any break should be treated as potentially self-sustaining rather than mean-reverting, because once the gamma pin gives way there's no vanna cushion underneath. In negative GEX/+VEX, short gamma accelerates the initial selloff and produces the fear-driven vol spike. But positive vanna below spot means that once implied volatility eventually fades, dealer buying flows mechanically. This is the panic-low template: being long into the panic with a defined-risk structure is favored, particularly when the VIX is elevated and large positive VEX sits at or below current spot, because violent next-session reversals are the mechanical consequence of this configuration.

### Start Trading Smarter

See these concepts in action with Skylit's dealer exposure tools.

[Get access](https://www.skylit.ai/#pricing)[Try Heatseeker](https://www.skylit.ai/#pricing)
