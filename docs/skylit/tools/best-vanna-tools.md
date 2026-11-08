<!-- Source: https://www.skylit.ai/learn/best-vanna-tools -->

# Best Vanna Exposure (VEX) Tools for Trading

# Best Vanna Exposure (VEX) Tools for Trading

tools·8 min read

vexvannatoolscomparisonheatseeker

## The Missing Half of Dealer Flow

Many options analytics platforms are built around gamma. That's not wrong. Gamma governs dealer hedging in the 0-5 DTE window, it explains intraday pinning, same-day acceleration zones, and why markets often close near high-open-interest strikes. For day traders running zero-day setups, a GEX tool is genuinely useful.

But gamma is a short-range instrument. Once you're holding a position for more than a few days, a different Greek takes over.

[Vanna Exposure (VEX)](https://www.skylit.ai/learn/vanna-exposure) measures how dealer deltas shift when implied volatility moves. Every time the VIX compresses, dealers who are net long vanna buy back stock hedges they no longer need. Every time vol expands, they sell. That flow is mechanical, it doesn't respond to price levels or fundamental news, and it runs continuously across the 7-180 DTE expiration window where most institutional positioning lives.

The key insight from studying dealer Greeks: **0-5 DTE is gamma's world. 7-180 DTE is vanna's world.** A trader watching only GEX is watching one screen while the multi-day move plays out on another.

🎯ELI5

Vanna is the tailwind you only notice when it stops blowing. In calm, low-VIX tape the market grinds higher and it feels like nothing is happening. What's actually happening is that falling IV is mechanically pushing dealer hedges in one direction. The tailwind becomes obvious only when it reverses.

## What to Look For in a VEX Tool

Before comparing platforms, it's worth being specific about what "showing vanna" actually requires. Printing a single aggregate VEX number on a dashboard isn't the same thing as surfacing actionable vanna data.

A genuinely useful VEX tool needs to show:

**Strike-level distribution.** Positive VEX above spot and positive VEX below spot produce opposite dealer flows. The same aggregate number can be bullish or bearish depending on where the exposure sits relative to current price. Collapse the distribution into one number and you've lost the directional information.

**Vol regime context.** VEX has no fixed polarity. The same positive exposure that generates grinding upside in a compressing-vol environment becomes sell flow the moment IV starts climbing. Without knowing whether the vol regime is contracting or expanding, a VEX reading tells you very little.

**Cross-expiry tenor breakdown.** Front-end gamma and back-end vanna don't add up cleanly. A market propped up by near-term +GEX may be sitting on short vanna exposure in the 30-90 DTE expirations. When vol spikes, that back-end VEX overrides the gamma support. You can't see this without separating the tenor contributions.

**GEX alongside VEX.** When [GEX and VEX align](https://www.skylit.ai/learn/gex-vex-alignment), dealer flows reinforce each other and price behavior becomes more predictable. When they diverge, they compete, and the resulting tape is choppy and difficult to trade. The two views belong together.

## How the Main Tools Compare

Several platforms now include vanna exposure. Here's what the main ones include.

*Competitor details checked against each vendor's site in September 2026; features change, so check current offerings.*

### SpotGamma

SpotGamma is one of the most established names in dealer flow analytics. Its research notes and education are widely respected, and its tools include key levels, HIRO (a real-time read of options hedging impact) and TRACE (an intraday S&P 500 heatmap of gamma, delta and charm pressure). Its help center also documents a vanna model chart for major indexes and ETFs.

**Known for:** Daily research and education, intraday gamma and charm views, broad stock coverage in Equity Hub.

### OptionsDepth

OptionsDepth focuses on SPX and VIX. Its DepthView heatmap shows market maker exposure across strikes and expirations, with gamma, delta, vanna (VEX) and charm as selectable metrics. Positioning is built from exchange participant-tagged data, and top plans update intraday every minute.

**Known for:** Participant-tagged SPX positioning, charm projection, vanna in a strike-by-expiration heatmap.

### QuantData

QuantData lists VEX alongside GEX, DEX and CHEX, across strikes and expirations. Its Interval Map shows how exposure builds and decays through the day, and the platform pairs exposure with real-time options flow and dark pool data.

**Known for:** A broad Greeks exposure suite, including VEX, across stocks, ETFs and indexes.

### VolSignals

VolSignals combines expert commentary with a self-serve tool. VS Pro offers daily guidance on SPX and VIX volatility and dealer positioning, and VS3D is a web app with market maker positioning by strike and expiration and gamma, charm and vanna views, updated live intraday.

**Known for:** Institutional-style volatility analysis, education, and index-focused positioning tools.

### TradeEcho DealerEdge

DealerEdge is the dealer exposure module inside TradeEcho, an all-in-one platform. Its heatmap shows GEX by strike and expiration, and it adds vanna (VEX) and charm on the same grid, across indexes, ETFs and stocks.

**Known for:** One subscription for exposure, flow, dark pool, news and AI agents.

💡Core Idea

Showing vanna is only the start. The questions that make it tradeable are where the exposure sits relative to spot, which expirations it comes from, whether volatility is compressing or expanding, and whether it agrees with gamma at the same strikes. Check how each tool helps you answer those.

## Why Traders Choose Skylit

Feature lists converge. These are the things traders tell us they stay for, and the parts of Skylit that go beyond a data feed.

* **Rated 4.9 on Trustpilot and Whop (as of September 2026).** Read the reviews on [Trustpilot](https://www.trustpilot.com/review/skylit.ai) and [Whop](https://whop.com/heatseeker).
* **A Trader Success team on every plan,** with 1:1 Success Sessions on Pro.
* **Daily Live Stages inside the Skylit app,** not on a third-party platform. Hosts share their screens and talk through the market, and a minimized stage keeps playing while you use Heatseeker, Atlas or anything else in Skylit.
* **The Heatseeker framework:** the King Node (the node with the highest absolute GEX, positive or negative), Gatekeepers (prominent nodes between price and the King), Velocity Mode, and Trinity Mode, which shows SPXW, SPY and QQQ side by side by default and lets you change the instruments.
* **Replay:** pick any past date and time and play the Heatseeker board forward, or replay a session on Atlas with the data as it was at each minute.
* **[Tempest](https://www.skylit.ai/modules/tempest) (Pro):** implied volatility and expected-move ranges, stock by stock.
* **Trade from inside the platform:** Nexus (Beta) for paper trading with trade reviews and a leaderboard, and Aethos (Coming in Q4) for futures order execution inside Skylit through your prop firm account, with order flow, the DOM and Level 3 depth on the same screen.
* **API and MCP (Beta):** bring Skylit data into your own tools and AI assistants.

## How Heatseeker Handles VEX

See this in Heatseeker

Heatseeker is built around the dealer microstructure framework, showing GEX and VEX on one board by strike and expiration, with live intraday updates, King Nodes, Trinity Mode and Velocity Mode.

[Try Heatseeker](https://www.skylit.ai/#pricing)

Heatseeker was built with the vol-spot feedback loop as a core design principle. VEX isn't an add-on metric. It sits on the same board as GEX, a switch apart, with the same strike-level resolution, and the King Node and Velocity Mode follow the view you pick. See [VEX trading setups](https://www.skylit.ai/learn/vex-trading) for how traders use it.

**The VEX heatmap** shows positive and negative vanna exposure across every strike on the options surface. Read it alongside the vol regime: the same vanna produces buy flow while IV is compressing and sell flow while it is expanding.

**Trinity Mode** surfaces dealer positioning across SPXW, SPY and QQQ side by side by default, and you can change the instruments. These instruments share underlying price but carry distinct options distributions. When vanna structure aligns across all three, the signal is cleaner. When they diverge, Trinity Mode shows that divergence before it shows up in price.

**Velocity Mode** tracks the rate of change in dealer positioning in real time. For VEX specifically, it shows whether a vanna exposure cluster is accumulating (increasing dealer urgency) or unwinding (positioning being rolled or expired off). A growing vanna node reads differently than a stable one.

**GEX/VEX alignment** is read by switching the same board between GEX and VEX, and on Pro, Atlas can plot GEX, VEX or GEX+VEX levels on the chart. This is where the analysis gets most useful: identifying strikes where both forces flip simultaneously, and identifying gamma support levels that are being quietly undermined by cross-expiry vanna on the back end.

**The tenor breakdown** comes from the board itself: columns are expirations, so you can see front-end and back-end exposure separately. Before entering a multi-day position, the question isn't just where GEX sits. It's whether the underlying VEX structure can hold through a vol expansion event. That question requires the breakdown. An aggregate number can't answer it.

Heatseeker updates live through the session.

The data behind Heatseeker isn't raw exchange data repackaged with a heatmap overlay. Skylit's exposure readings are proprietary, built from years of research into dealer microstructure and how dealers actually position and hedge.

Tools are only as good as the experience of using them. Heatseeker is designed for traders who need to make fast decisions, not for analysts with unlimited time to configure dashboards. The board stars the King Node, right-clicking a cell names its role (King, Pika, Barney), and you can set approach and tap alerts straight from the board.

Skylit doesn't just hand you a tool and leave you to figure it out. Every plan includes Skylit's dedicated Trader Success team and daily Live Stages, and Pro adds 1:1 Success Sessions.

Read verified trader reviews at [whop.com/heatseeker](https://whop.com/heatseeker) and [trustpilot.com/review/skylit.ai](https://www.trustpilot.com/review/skylit.ai).

## Frequently Asked Questions

### What is vanna exposure (VEX) and why does it matter?

Vanna exposure (VEX) is the aggregate vanna across all open options positions at a given strike. Vanna measures how a dealer's delta changes when implied volatility moves, so VEX quantifies the total stock-buying or stock-selling that dealers produce as IV rises or falls. It's the primary driver of the catalyst-free grinds and sudden rug-pulls that gamma alone can't explain. The quiet upside in low-VIX tape isn't random, it's positive VEX working. Most rug-pulls on vol spikes aren't random either. For the full mechanics, see the guide on [vanna exposure](https://www.skylit.ai/learn/vanna-exposure).

### Do any trading tools show vanna exposure?

Yes, several do. Heatseeker, QuantData, Unusual Whales, BullFlow, OptionsDepth, VolSignals' VS3D and TradeEcho's DealerEdge all include vanna exposure in some form, and SpotGamma documents a vanna model chart. They differ in coverage (index-only or stocks too), in whether vanna is shown by strike and expiration, and in how often the data updates. Heatseeker shows VEX at every strike and expiration on the same board as GEX, with the King Node, Velocity Mode and Trinity Mode.

### How does Heatseeker compare to SpotGamma for vanna analysis?

SpotGamma is known for strong research and education, and its tools center on gamma, delta and charm, with a vanna model chart for major indexes and ETFs. Heatseeker shows VEX as a full strike-by-expiration board, the same way it shows GEX, with the King Node, Velocity Mode and Trinity Mode following whichever view you pick. If you want to read vanna strike by strike and expiration by expiration, that is what Heatseeker's VEX view is built for.

### Why is vanna more important than gamma for multi-day trades?

Gamma dominates in the 0-5 DTE window where gamma per dollar of notional is largest and dealer rebalancing is fastest. Beyond five days, gamma becomes modest while vanna becomes the dominant dealer hedging force. A support level that holds perfectly through same-day gamma dynamics can break the next session if large negative back-end VEX sits below spot and a vol expansion event triggers the sell flow. Multi-day trades are effectively bets on the vol regime as much as on price direction, and the vol-driven force shaping that regime is vanna, not gamma. See [VEX trading setups](https://www.skylit.ai/learn/vex-trading) for the full scenario matrix.

### What's the difference between GEX and VEX alignment vs. divergence?

When GEX and VEX are both positive or both negative at a given strike, dealer flows from both hedging dimensions point in the same direction. Price behavior becomes more predictable and moves tend to be cleaner. When they diverge, one force is buying while the other is selling, and the tape gets choppy and difficult to read. The highest-conviction setups come from [GEX and VEX alignment](https://www.skylit.ai/learn/gex-vex-alignment) at a key strike, especially when both flip sign simultaneously as price clears that level.

### Start Trading Smarter

See these concepts in action with Skylit's dealer exposure tools.

[Get access](https://www.skylit.ai/#pricing)[Try Heatseeker](https://www.skylit.ai/#pricing)
