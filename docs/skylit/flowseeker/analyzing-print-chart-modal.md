<!-- Source: https://www.skylit.ai/learn/analyzing-print-chart-modal -->

# Analyzing a Print with the Chart Modal

# Analyzing a Print with the Chart Modal

flowseeker·17 min read

flowseekeroptions-flowchart-analysisinstitutional-flow

## What the Chart Modal Is For

The Live Feed and the Scanner show you *what happened*. The chart modal is where you decide whether what happened *matters*.

Every print on the tape is a hypothesis. *"This $2M call sweep on TSLA at $260 means an institution is positioning bullishly into earnings"* is a hypothesis, not a fact. It might be right. It might be a hedge against an existing short position. It might be one leg of a complex spread that, on its own, looks bullish but as a structure is neutral. The chart modal is the surface where you confirm or reject that hypothesis before deciding whether to act on it.

This article assumes you've already read the [Introduction to Flowseeker](https://www.skylit.ai/learn/intro-to-flowseeker) and [Navigating Flowseeker](https://www.skylit.ai/learn/navigating-flowseeker) articles. Those covered *what* the chart modal is and where to find it. This one covers *how to use it analytically* — what each of the five views actually tells you, the order to look at them when investigating a print, and how to read the signals each one surfaces.

🧠TL;DR

The chart modal opens on **Net Premium** by default in the right pane (desktop). That's a deliberate choice — Net Premium is the view that most quickly tells you whether a print fits the broader institutional flow context, or contradicts it. Always glance at it first.

## Five Views, Five Questions

Each view answers a different question about the print you're investigating. Knowing which view answers what saves you from staring at all five hoping a pattern emerges.

| View | The question it answers |
| --- | --- |
| **Contract Flow** | How has this specific contract traded — and was it unusually busy? |
| **Underlying (Vol)** | Did option activity in this name match what the stock was doing? |
| **Underlying ($)** | Was real institutional dollar flow rotating into this name today? |
| **Net Premium** | Is institutional money flowing the same direction as this print, or against it? |
| **Strike Distribution** | Is the activity concentrated at this strike, or scattered across the chain? |

The rest of this article walks through each view in detail. Then a workflow section ties them together, then a worked example shows the method end-to-end, then an investigation checklist you can keep handy.

## Contract Flow: What This Specific Contract Has Been Doing

The Contract Flow chart is the **left pane on desktop** (always — it doesn't switch with the right-pane dropdown) and one of the tab options on mobile. It's the only view in the modal that's about the option contract itself, not the underlying stock.

**What you actually see on this chart isn't OHLC price candles.** It's a stacked volume bar chart — each bar represents the volume in that time bucket, split into segments by where in the bid-ask spread the volume hit:

* **No-side** at the bottom (gray) — volume that couldn't be cleanly classified
* **Ask** above that — volume that hit at or above the ask (aggressive buying)
* **Mid** above that — volume that cleared between the bid and ask
* **Bid** at the top — volume that hit at or below the bid (aggressive selling)

The contract's actual price information lives in the **Avg Fill** line (a VWAP) plotted on the right axis. The bars tell you *how much and how aggressive*; the line tells you *at what price*.

That's a meaningful design choice: the Contract Flow chart is fundamentally a **volume and aggressiveness chart**, not a price chart. The question "did the contract go up or down" matters less here than "did the volume skew aggressive to one side, and how did the average fill drift over time."

### What to read

* **Stack composition over time.** A bar that's mostly ask volume is a window where buyers were lifting offers. Mostly bid volume is a window where sellers were hitting bids. Mostly mid is patient two-sided activity.
* **The shape of the day.** Was the aggressive volume concentrated in one window (often around the print you're investigating)? Or distributed across the session? A single concentrated burst with high ask volume followed by quiet is a different signal than the same total volume distributed evenly.
* **The Avg Fill line.** If the line is rising over the day, the contract has been getting more expensive — buyers were paying up. If it's flat despite high volume, you've got two-sided liquidity matching at consistent prices. If it's falling, sellers were getting filled lower and lower.

### Toggles that matter

Three toggles change what's shown:

* **Avg Fill** (on by default) — the VWAP line. Turn off to see just the volume bars.
* **IV** (off by default) — overlays implied volatility as a line. **This is one of the most powerful confirmation toggles in the modal.** If a print is bullish (someone's buying calls) and IV is *expanding* through the day, the market is pricing in more movement — that's confirmation. If IV is *contracting* despite bullish volume, the bid-ask spreads are tightening and the directional thesis loses some weight. Always check IV when investigating a directional print.
* **RVOL** (off by default; desktop only) — adds a background rectangle showing the contract's *average* volume baseline. The bars sit on top of this background. The hover tooltip then shows an `Nx` ratio — `2.0x` means today's volume is twice the average for that contract at that time. **RVOL is the fastest way to answer "is this contract unusually active right now."** If RVOL is below 1, today's activity is below normal — a print that looked huge on the tape might just be normal flow for this contract.

You can also toggle individual stack segments (Bid / Mid / Ask) on or off if you want to focus on, say, only ask-side volume.

🧠TL;DR

For investigating any directional print, the workflow is: turn on **IV** and **RVOL**, look at the bar around the print, check whether the stack is ask-skewed (bullish print confirmation) or bid-skewed (selling), check whether RVOL > 1 (contract is unusually busy), and check whether the IV line is rising (vol expanding alongside the directional bet). If all three line up, you've got contract-level confirmation. If they don't, your hypothesis just got weaker.

### Time intervals

Two dropdowns control the timeframe and bar size: **interval** (1D / 2D / 3D / 7D / 14D / 30D / 45D / 60D / 90D / 120D / 180D / 360D) and **bucket** (1min through 1week, with valid combinations enforced — e.g. 1D allows 1/5/10min, 360D forces 1w).

For investigating a fresh print, **1D / 5min** (the default) is usually right. Use longer intervals when you want to see how the contract has been trading over multiple days — useful when you're checking whether a print is part of a multi-day pattern or an out-of-nowhere event.

### Selecting a bar

Click any bar on the contract chart. A green outline appears around it. The footer auto-switches to **Flow Orders** and (on desktop) scrolls down to the table — you'll see the individual prints inside that bar. The footer is covered later, but this is the bridge between "I see a busy bar" and "show me the actual trades that made it busy."

## Underlying (Vol): Did the Option Activity Match the Stock?

The Underlying (Vol) chart switches focus from the contract to the **whole ticker**. It plots:

* **Stacked bars** of option volume across all contracts: put volume on the bottom, call volume stacked on top
* **The stock price** as a line on the right axis (toggleable)

This is a "did the option flow agree with the stock price action" view.

### What to read

* **Imbalance.** A green stock day with strongly call-skewed volume = options flow confirmed the move. The same green stock day with put-dominant volume = something's off. Either institutions are hedging into strength (defensive) or someone's positioning for a reversal.
* **Sequence.** Did the option volume *lead* or *follow* the price move? Volume building before a stock breakout is meaningfully different from volume that piled in after the move.
* **Total participation.** A stock making new highs on muted option activity is a different signal than the same move accompanied by 3x normal option volume.

### Toggles

* **Price** — turn the stock line on or off. Most people leave it on.
* **RVOL** (desktop only) — same concept as Contract Flow's RVOL, but here the background compares to the **underlying ticker's typical option volume across the entire chain**, not the specific contract's. Useful for spotting days when the whole name is unusually busy in options, regardless of which contract you drilled into.
* **Interval / bucket** — same dropdowns as Contract Flow, with the same defaults.

Underlying (Vol) is best read **alongside Underlying ($)**, since the two answer slightly different questions.

## Underlying ($): Where the Real Money Was

This view is structurally the same as Underlying (Vol) but the bars show **dollar premium** instead of contract count. Put premium on the bottom, call premium on top, stock price line overlaid.

The reason this matters: **contract count and dollar premium often tell different stories**. A thousand $0.10 OTM puts is $10,000 in premium — a retail-sized hedge in a small name. A hundred $5.00 ATM calls is $50,000 — institutional positioning. Both look the same on a vol-only view; they look very different on a $-only view.

### When to use Vol vs $

* **Vol** = participation breadth. Are *many* people trading this name today?
* **$** = institutional weight. Is *real money* being committed?

When the two views agree (high vol AND high premium on the same side), you've got broad institutional consensus. When they diverge — e.g., elevated put volume but the put *premium* stays muted — you're often looking at lots of small protective hedges rather than a real bearish thesis. That distinction matters a lot for whether to chase a print.

💡Core Idea

A common mistake is to look only at volume. Volume tells you "lots of people did this" but not "lots of money did this." Premium is almost always the more relevant question for tracking institutional behavior. When you only have time for one of these two views, pick **Underlying ($)**.

## Net Premium: The Most Analytically Rich View in the Modal

This is the view to spend the most time on. Net Premium is where the print you're investigating gets compared against the broader institutional flow context for that ticker over a horizon you choose.

### What's on the chart

Two filled areas plotted from a per-bar response:

* **NCP** (green, ask-side theme) — net call premium per bar
* **NPP** (red, bid-side theme) — net put premium per bar

Plus an optional **stock price** line on the right axis (toggleable on desktop).

A summary row above the chart shows the totals over the selected interval: **Net**, **NCP**, **NPP**, plus a **Net Sentiment** bar that splits the activity into bullish vs bearish.

### What "bullish" and "bearish" actually mean here

Many flow tools throw around words like "bullish flow" without defining them. The Net Sentiment bar in this view has a specific definition you can see derived in the UI:

* **Bullish** = call premium *bought* (hit at the ask) + put premium *sold* (hit at the bid)
* **Bearish** = call premium *sold* (hit at the bid) + put premium *bought* (hit at the ask)

That's an intent-aware count. Buying calls and selling puts both express a long view. Selling calls and buying puts both express a short view. The Net Sentiment bar reflects the proportion of those two stacks in the chosen interval.

### The interval dropdown

A single dropdown sets the lookback: **1D / 2D / 3D / 7D / 14D / 30D / 45D / 60D / 90D / 120D / 180D / 360D**.

Each interval answers a different question:

| Interval | What you learn |
| --- | --- |
| **1D** | Is today's flow consistent? Is the print you're investigating in line with the day's overall direction? |
| **2D – 7D** | Is the print part of a short-term trend, or a one-day blip? |
| **14D – 30D** | Is institutional money positioning long or short over the recent regime? |
| **60D – 360D** | What's the dominant longer-term flow stance for this ticker? Useful for separating "transient print" from "ongoing campaign." |

For most fresh-print investigations, the 5–7D view is the sweet spot: long enough to show context, short enough to be relevant to today's print.

### The divergence pattern

The single most useful thing this view shows you is **divergence between price and net premium**. There's no automatic detection — you read the lines yourself. Watch for:

* **Price up, NCP falling / NPP rising** → institutional money is quietly positioning bearish even as the stock grinds higher. Often precedes reversals.
* **Price down, NPP falling / NCP rising** → stealth buying into weakness. The stock looks broken but premium is rotating bullish.
* **Price up, NCP up steadily** → the move is being confirmed by aggressive call buying. No divergence; the trend has institutional backing.
* **Price flat, NCP and NPP both surging** → big two-sided positioning, possibly ahead of an event (earnings, FDA, Fed). High option activity without directional consensus.

A bullish print on the live feed *is* meaningful when Net Premium for that ticker has been bullishly trending all week. The same print is much *less* meaningful (potentially a hedge or noise) when Net Premium has been bearishly trending — you're seeing one ask-side print against the backdrop of a sustained bid-side flow.

🎯ELI5

Think of Net Premium as the *prevailing wind* and the print you're investigating as a *single sail*. A sail aligned with the wind moves fast. A sail perpendicular to the wind goes nowhere. You're trying to figure out which one this print is — and Net Premium is the wind direction.

## Strike Distribution: Where the Activity Concentrates

This view shows **horizontal stacked bars by strike** for the entire chain on the day. Each strike's bar has a call premium segment and a put premium segment. The strikes are sorted high to low (highest strike at top). A dashed gold line marks the current spot price.

### What to read

* **Concentration vs. scatter.** Does activity pile into 1–3 specific strikes (consensus), or spread evenly across 10+ strikes (no consensus)? Concentration is a stronger signal — institutions don't accidentally pile into the same strike. Scatter is often retail noise plus market-making rebalancing.
* **Calls vs puts at the same strike.** Both are shown stacked at each strike. A strike with a big call segment and a tiny put segment is being positioned bullishly. A strike with both legs roughly equal is more often a hedging or spread structure than a directional bet.
* **Position relative to spot.** A heavy concentration at strikes well above spot (for calls) implies institutional money is reaching for upside. Heavy concentration at strikes well below spot (for puts) implies real downside positioning. Concentration at strikes near spot is often hedging.

### 1D vs 1W toggle

* **1D** — today's strike distribution only.
* **1W** — the current trading week (Monday through today). Useful for seeing whether today's concentration is part of a multi-day build at that strike, or out of nowhere.

A strike that's been accumulating premium over the full week is a much stronger structural signal than one that just lit up today.

### Per-expiration drill-down

Click any strike. An **Expiration Distribution Panel** opens showing how that strike's activity breaks down across expirations: Call Premium total, Put Premium total, Top Expiry, and horizontal bars per expiration. This separates "all today's flow at this strike was 0DTE noise" from "this strike has been getting positioned across multiple expirations all week."

### Toggles (desktop)

* **Calls** / **Puts** — show or hide either segment if you want to focus on one
* **Spot** — show or hide the gold spot reference line

## The Footer: Flow Orders and Vol/OI History

Below all five views is a footer that toggles between two tables.

### Vol/OI History (default)

Shows **14 trading days** of history for the contract. Columns include Date, Volume, OI, OI change %, Close price, Average fill (VWAP), a Bid/Ask execution bar, and Total Premium. On desktop you also get a 30-min volume sparkline, the day's IV, Sweep %, Multi %, and that day's % of total ticker volume.

This is the table to read when you need to ask: *"is what's happening today actually unusual for this contract?"* A 5,000-volume day looks impressive in isolation, but if the prior 13 trading days have averaged 7,000, today is below normal. That changes the meaning of the print you're investigating.

The Vol/OI History table is **not** filtered by candle selection — you always see the full 14-day window.

### Flow Orders (when a candle is selected)

Click a bar on the Contract Flow or Underlying chart. The footer switches to Flow Orders and lists the individual prints inside that bar. Columns include Date/Time, Contract, DTE, Price, Size, Vol, Premium, Side, Spread (with the bid-ask visualization), Prev IV / IV / Next IV, Stock price, OI. Sweeps are flagged with a gold Waves icon next to the time.

This is the bridge between "the bar around the print I'm investigating was very active" and "show me the actual trades that made it active." Use it to verify that the print you're investigating is one of the trades in the bar (often it is — the bar is large *because* of your print plus surrounding activity).

The **Expand Trades** button on a selected candle promotes this further: it opens a brand-new Live Feed tab filtered to that contract and time window, so you can see all those prints in the full Live Feed UX with all the columns and right-click actions you're used to.

## The Investigation Workflow

When investigating a fresh print, run through the modal in this order. Each step has a question and a fast read.

1. **Net Premium (start here, 5–7D interval).** Has institutional money been flowing bullishly or bearishly in this ticker over the past week? Is the print consistent with the prevailing wind, or against it? *If against and the divergence is strong, your hypothesis is on shaky ground before you've even looked at the contract.*
2. **Underlying ($).** Did real dollar premium rotate into this name today, on the same side as the print? *If the day's option activity is bid-skewed in puts but you're investigating a call print, that's a contradiction worth understanding.*
3. **Contract Flow (with IV and RVOL on).** Is *this specific contract* unusually busy (RVOL > 1)? Is its bar around the print ask-skewed (consistent with bullish intent)? Is IV expanding or contracting? *This is contract-level confirmation.*
4. **Strike Distribution (1W).** Is the print landing at a strike that's been accumulating premium all week, or is it the only meaningful activity at that level? Click into the strike and check the per-expiration breakdown. *Concentration is structural; scatter is noise.*
5. **Vol/OI History (footer).** Is today's volume on this contract unusual against the 14-day baseline? *If today is below average and the print still looked huge, the print is even more significant — it's standing out against quiet days.*
6. **Cross-check with Heatseeker.** Open the Heatseeker map for the same ticker. Does the strike where the print landed sit on a –GEX zone (dealers short gamma → forced hedge amplifies the move) or a +GEX wall (dealers long gamma → forced hedge absorbs the move)? *Same print, different structural outcome. This is the step that turns "interesting institutional positioning" into "trade with structural fuel" or "interesting print to skip."*

If steps 1–5 line up coherently and step 6 shows structural fuel, you've got an actionable hypothesis. If any step contradicts the others, the hypothesis weakens. Multiple contradictions and you skip — that's the win. The chart modal's job isn't to show you trades worth taking; it's to show you which ones *aren't*.

## Worked Example

Here's the workflow applied to a hypothetical print. The numbers are illustrative.

**The print on the live feed:**

> 11:14 AM ET — TSLA 260C, 17 DTE, sweep, $1.85M premium, side: Ask, Flow Score +75, Spread bar pinned at the ask, V/OI: 1.4

A Flow Score of +75 with $1.85M premium on a sweep at the ask is loud. But that's the hypothesis, not the conclusion. Open the chart modal.

**Step 1 — Net Premium, 7D interval.**
The NCP line (green) has been steadily rising for the past week. NPP (red) is flat. The stock price line shows TSLA up ~6% over the same period. Net Sentiment for the period reads strongly bullish. *No divergence. Institutional flow has been bullish all week, and today's print fits that pattern. Hypothesis: still alive.*

**Step 2 — Underlying ($).**
Today's bars show heavy call premium on the upper stack, much smaller put premium on the bottom. The stock price line is up ~2.5% on the day. Real dollars rotated into TSLA calls today, in size, on the same side as the print. *Hypothesis: confirmed at the day level.*

**Step 3 — Contract Flow, IV and RVOL on.**
The 11:14 AM bar is the largest of the day, and the stack is 80% ask volume. RVOL hover shows `3.2x` — this contract is trading at three times its typical volume for that time of day. The IV line has been rising through the day, accelerating around the print. The Avg Fill line is up. *Hypothesis: confirmed at the contract level. This is exactly the kind of pattern an institution opening a directional bet leaves on the chart.*

**Step 4 — Strike Distribution, 1W view.**
The $260 strike has the largest call premium bar on the chart. Click into it. The per-expiration panel shows the activity is concentrated in the front two expirations (today's $260C is the 17DTE; the next one out has a smaller but meaningful position). *Hypothesis: this isn't an isolated print; the $260 strike has been a positioning target all week.*

**Step 5 — Vol/OI History.**
Today's volume is the highest of the past 14 trading days for the $260C contract. OI grew yesterday and the day before. *Hypothesis: confirmed against the contract's own baseline. This is genuinely unusual activity.*

**Step 6 — Heatseeker cross-check.**
Open Heatseeker for TSLA. The $260 level shows a –GEX zone with no significant +GEX wall above it until $268. Dealers are short gamma in the path between $260 and $268. *Hypothesis: confirmed structurally. If TSLA pushes through $260, dealer hedging will amplify the move toward $268.*

Six steps, all aligned, structural fuel present. This is the kind of print that justifies action. If steps 1, 3, or 6 had contradicted, you'd have walked away.

The point isn't that every investigation produces a "yes" — it's that the workflow forces you to ask each question and weight the answer. Most prints, run through this method, will tell you to skip. The ones that survive all six steps are the few that actually deserve attention.

## Investigation Checklist

For when you want a fast reference. Pin this to your workspace and run through it for any print you're seriously investigating.

1. **Net Premium (5–7D)** — Is institutional flow in this ticker on the same side as the print? Look for divergence between price and NCP/NPP.
2. **Underlying ($)** — Did real dollar premium rotate the same direction as the print today? Compare against the Vol view if anything looks odd.
3. **Contract Flow (IV + RVOL on)** — Is the contract unusually busy (RVOL > 1)? Is the bar around the print stack-skewed in the right direction? Is IV expanding alongside the move?
4. **Strike Distribution (1W)** — Is the strike a focus of the week's activity, or an isolated print? Click in for the per-expiration breakdown.
5. **Vol/OI History** — Is today's contract activity unusual against the 14-day baseline?
6. **Heatseeker cross-check** — Does the strike sit on a –GEX zone (structural fuel) or a +GEX wall (absorption)?

If steps 1–5 align coherently and step 6 shows fuel, the print earns more attention. Multiple contradictions → skip and move on to the next print on the tape. The discipline of running this loop, not the speed of any one investigation, is what separates analytical flow reading from chasing tape.

See this in Flowseeker

Flowseeker's chart modal lets you investigate any print across five integrated views — Contract Flow, Underlying volume, Underlying premium, Net Premium, and Strike Distribution — and cross-reference dealer positioning in the same terminal.

[Try Flowseeker](https://app.skylit.ai/flow/live?utm_source=skylit_landing&utm_medium=website&sl_relay=1)

For the foundational concepts this article assumes, see the [Introduction to Flowseeker](https://www.skylit.ai/learn/intro-to-flowseeker) and [Navigating Flowseeker](https://www.skylit.ai/learn/navigating-flowseeker) articles. For the dealer-positioning context that the cross-check step relies on, see the [Dealer Positioning](https://www.skylit.ai/learn/dealer-positioning) and [Reading Heatseeker](https://www.skylit.ai/learn/reading-heatseeker) guides.

## Frequently Asked Questions

### What's the difference between NCP and NPP on the Net Premium chart?

**NCP** is *net call premium* per bar — the call dollar flow, with bid-side and ask-side activity netted. **NPP** is *net put premium* per bar, computed the same way for puts. They're plotted as filled areas (NCP green, NPP red) so you can see at a glance which side is dominating in any given window. The summary above the chart aggregates these into **Net** (overall total), **NCP** (calls), **NPP** (puts), and a **Net Sentiment** bar that splits activity into bullish (calls bought + puts sold) versus bearish (calls sold + puts bought).

### Why does Strike Distribution show calls and puts at the same strike?

Both are real activity at that strike. A bar at the $260 strike with a meaningful call segment *and* a meaningful put segment usually means a spread structure (vertical, straddle, etc.) is being built at that level — institutions often pair calls and puts at the same strike for strategic reasons. Reading the segments together is more useful than reading them in isolation: a strike that's call-dominant is being positioned directionally; a strike that's roughly balanced is being positioned for volatility or being hedged.

### When should I use 1D vs 5D vs 30D on the Net Premium chart?

It depends on what question you're asking. **1D** for "is today's flow consistent within itself" (intraday context for a fresh print). **5–7D** for "is this print part of a recent trend or an outlier" (the most common investigation interval). **14–30D** for "what's the regime been over the recent positioning window" (when you want to know the ticker's current institutional stance). **60D+** for "is there a longer-term campaign happening here" (rare but useful for high-conviction names). For most fresh-print investigations, 5–7D is the sweet spot.

### Why doesn't the Contract Flow chart show sweep or multi-leg markers on the bars?

The Contract Flow chart's bars are aggregate volume buckets — a single bar can contain dozens of prints, so per-trade markers wouldn't fit cleanly on the chart itself. To see whether sweeps are inside a particular bar, **click the bar** to switch the footer to Flow Orders. The Flow Orders table shows each individual print inside that bar, with sweep flagged via a gold Waves icon next to the time. That's where the per-trade classification lives.

### What does "Refresh" actually do, and when should I use it?

The Refresh button at the top of the modal re-pulls the chart data and **clears any candle selection** you had. Use it when the underlying flow is moving fast and you want to see the latest bars without closing and reopening the modal. There's a short cooldown so rapid clicks don't stack. Note that the Vol/OI History table doesn't refresh on the same button — that's a daily-resolution table that doesn't change intraday.

### Start Trading Smarter

See these concepts in action with Skylit's dealer exposure tools.

[Get access](https://www.skylit.ai/#pricing)[Try Heatseeker](https://www.skylit.ai/#pricing)
