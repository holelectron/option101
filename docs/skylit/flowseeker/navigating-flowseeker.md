<!-- Source: https://www.skylit.ai/learn/navigating-flowseeker -->

# Navigating Flowseeker

# Navigating Flowseeker

flowseeker·12 min read

flowseekeroptions-flowterminalui-guide

## The Three Pages

Flowseeker isn't one screen. It has its own sidebar section with eight pages: Live Feed, Dark Feed, Flow Scanner, Flow Compass, Contract Lookup, Company Events, Flow Tracker and Flow Alerts. The [Introduction to Flowseeker](https://www.skylit.ai/learn/intro-to-flowseeker) article covered the live feed in depth; this article covers three of those pages that work closely together. Knowing what each one is for, and how to move between them, is the difference between fighting the UI and using it.

The three pages are:

* **Live Feed** — the real-time tape, one row per print. This is what most people mean when they say "Flowseeker."
* **Flow Scanner** — a contract-level view of the day's activity. Every print for a given contract (ticker + expiration + strike + C/P) is rolled up into a single row with aggregated totals, sentiment breakdowns, and OI dynamics.
* **Flow Tracker** — a persistent list of prints you've bookmarked, with live P/L and close-detection.

They share a common drill-down — the chart modal — and they share the same underlying data. What changes between them is the *unit of analysis*: individual prints vs. aggregated per-contract activity vs. bookmarked follow-up.

🎯ELI5

Live Feed is the tape printing trade by trade. Scanner is the scoreboard showing how each contract's day totals look. Tracker is a notebook of positions you want to remember. Same underlying data, three different ways of seeing it.

## How You Get There

On desktop, these three pages sit in the left sidebar's **FLOWSEEKER** section, alongside the other Flowseeker pages:

* Live Feed (the radio icon)
* Flow Scanner (the magnifying-glass icon)
* Flow Tracker (the radar icon)

On a phone, the Flowseeker bar lists Live Feed, Dark Feed, Flow, Compass, Lookup, Events, Tracker and Alerts.

Accounts with Discord or API access also see **Settings** at the end of the Flowseeker section, for Discord channels, summary sections and API keys. That's out of scope for this article; if you're here to figure out how to read and react to flow, the three pages above are all you need.

🧠TL;DR

If you ever see a small number badge on the Tracker icon, it means one or more of your tracked trades has had a close event detected (partial exit, full exit, expiration). Clicking through clears the badge. More on that in the Tracker section.

## Live Feed: What's There Beyond the Basics

The [Introduction](https://www.skylit.ai/learn/intro-to-flowseeker) walks through the overview bar, the 22 columns in the feed, and the basic filter sidebar. Those are the fundamentals. But the Live Feed page has several features that aren't obvious until someone points them out — and most of them dramatically improve how you work in it once you know they exist.

### Multiple Feed Tabs

You can keep up to **10 named tabs** across the top of the Live Feed. Each tab holds its own filter configuration, its own column layout, its own ticker-scope, and its own flow-highlighting rules. Right-clicking a tab gives you **Rename**, **Duplicate**, and **Delete**.

This is the single most underused feature in Flowseeker. Most people work from the default tab forever. Instead:

* Set up a "Big Tech Only" tab with Ticker scope locked to AAPL, MSFT, NVDA, META, GOOGL.
* Duplicate it, change the tickers, and you've got "Semiconductors" for AMD, INTC, AVGO, TSM.
* Set up a "High Conviction Sweeps" tab with $250K+ premium, Sweeps Only, and |Flow Score| > 60.
* Keep a "Full Firehose" tab with minimal filters for when you want to watch unfiltered tape.

Switching between tabs is instant and your filter state is preserved. Tabs persist across sessions — close the browser and your setup is still there when you come back.

### Ticker-Scope Search at the Top

The search bar at the top of the Live Feed lets you **include or exclude tickers** from the current tab. Type a ticker and press Enter (or comma) to add it to the include list. To **exclude** a ticker, prefix it with `!` — e.g. `!TSLA` to drop all Tesla prints.

Backspace with an empty input pops the most recently added tag. This is separate from the Ticker filter in the sidebar — think of the search bar as the fast, ad-hoc way to focus or de-focus the tape in the moment, without digging into the filter panel.

### Pause, Resume, and Historical Mode

The live feed has a connection indicator at the top-right showing the current state: **LIVE**, **PAUSED**, **CONNECTING**, or **OFFLINE**. Clicking it toggles between Live and Paused.

Pausing freezes the visible feed so you can study a cluster of prints without the tape scrolling out from under you. Incoming trades are held in a buffer while you're paused and merged in when you resume — but the buffer is bounded by your **Results limit** (50 / 100 / 250 / 500), so a long pause during heavy flow can push older buffered trades out before you ever see them. For short pauses, you'll catch up to everything that came in. For long ones, treat resume as *"catch up to roughly the last N prints"*, not *"play back everything I missed."*

You can also switch the feed into **Historical** mode by picking a past trading day. The control changes to a **HISTORICAL** badge instead of the live-connection indicator. Useful for reviewing yesterday's tape — or comparing today's session against a prior one by opening a second tab in historical mode.

### Results Cap and Sort

The **Results** dropdown in the header sets how many rows are shown — **50, 100, 250, or 500**. The **Sort by** dropdown lets you order the feed by **Time**, **Premium**, or **Size**.

One important quirk: when you sort by anything other than Time, Flowseeker applies a size floor — results are restricted to trades with at least **$25K premium or 150+ contracts**. This is intentional. Sorting a raw feed by Premium without a floor would bury most of your session under a single whale print; the floor keeps the non-Time sorts useful across the whole session.

### Columns Panel

Clicking **Columns** opens a panel where you can:

* Toggle individual columns on or off.
* Drag the grip handles to reorder columns.
* Configure **Flow Highlighting** — conditional color-coding rules that highlight rows when specific ratios (like Volume/OI or Size/OI) exceed thresholds you define.

Each of these is per-tab. That's important: your "High Conviction Sweeps" tab can hide columns like OTM % that don't matter for that use case and show a custom Flow Highlighting rule that fires when V/OI > 2.0. Your "Full Firehose" tab can show everything and skip the highlighting. They don't conflict.

### Sharing What You're Looking At

The **Share** button in the header gives you two options: **Copy Image** and **Save Image**. It captures a snapshot of the current feed state — tab name, filters applied, visible rows — as a PNG you can drop into Slack or a Discord message.

This is feed-level sharing. Per-trade sharing to Discord (with the chart and context) lives inside the **chart modal**, covered later in this article.

### Multi-Leg Strategy Modal

When a multi-leg strategy prints (vertical spread, straddle, iron condor, etc.), the affected rows in the feed are tagged with a **Layers icon**. A single leg of a complex trade by itself is hard to read — you're seeing one piece of a structured position, and trying to interpret it as a directional bet will mislead you. Clicking the Layers icon (or the strategy badge on the row) opens a modal that shows the entire strategy in one place:

* The **strategy type** (Vertical Spread, Iron Condor, Strangle, etc.) and **leg count** in the header.
* A **summary** of the trade: Net Premium across all legs, Total Size, the Strike Range, and a Net Sentiment label color-coded bullish, bearish, or neutral.
* A **Strike Structure** diagram positioning each leg by strike on a horizontal axis, with calls and puts visually distinguished. This is the fastest way to recognize the trade's shape — a put credit spread shows up as two puts close together, a strangle as a put low and a call high, an iron condor as four legs in a tight symmetric pattern.
* A **per-leg chart** for every leg, so you can see how each individual contract has traded since the strategy was put on.

The difference is between *"I see one of three legs of a print I don't understand"* and *"I see the full structure of what just got put on, and I can watch each leg's behavior independently."* Escape closes the modal.

### The "Expand Trades" Link Back From a Chart

When you click a row in the Live Feed and open the chart modal, select a candle on the contract chart, and click **Expand Trades**, Flowseeker **creates a new feed tab** filtered down to that candle's ticker, strike, expiration, and time window.

This is a live-feed-only workflow — you get to instantly see every print that made up a specific candle, without reconfiguring filters by hand. If you're trying to understand "what actually drove that spike at 10:47?", this is the fastest path. (The Scanner doesn't have this action — see the next section.)

## Flow Scanner: The Day's Activity, Aggregated by Contract

The Scanner looks superficially like the Live Feed — it has tabs, filters, and a table of rows — but it's a fundamentally different unit of analysis.

In the Live Feed, **every row is a single trade**. A large buyer sweeping 2,000 contracts on SPY $580 calls might produce 3, 5, or even 10 rows on the tape (one per exchange, one per fill). Each row is a print.

In the Scanner, **every row is a single contract**. That same SPY $580 call is one row — and on that one row you see the *aggregate* of everything that happened to it today: total volume, total premium, total trade count, bid/ask breakdown, sentiment scores, OI change since yesterday, sweep percentage, multi-leg percentage. If you want to know *which contracts were active today and how they traded*, the Scanner is the view.

You pick a trading day with the date control at the top, and previous days work the same as today.

That difference in unit cascades into a lot of UI differences:

| Feature | Live Feed | Flow Scanner |
| --- | --- | --- |
| Unit of analysis | One row per print (real-time) | One row per contract (day-aggregated) |
| Max tabs | 10 | 5 |
| Date control | Historical mode picker | Trading-day picker (prev / next / calendar) |
| Filter sidebar | Premium, Equity Type, Sweeps, Flow Score, DTE, Earnings, Sector, Side | Same plus OI Growth, contract/chain sentiment sliders, strike ranges, OTM/ITM/0DTE toggles, OPEX Only |
| Flow Highlighting | Per-tab | Not available |
| Columns customization | Show/hide + drag-reorder | Drag-reorder (sort) |
| Per-row right-click | Track trade, Show matching / Filter out, Add to summary (accounts with Flowseeker sharing) | Add to summary (accounts with Flowseeker sharing) |
| Chart modal "Expand Trades" | Creates a new live tab | Not wired up |
| Share | Image export | Image export |

### What Each Scanner Row Tells You

Because every row aggregates an entire contract's day, the columns on each row are telling you things the Live Feed can't show in a single line:

* **Total premium, total volume, total trade count** — how much real activity hit that contract today, across all prints.
* **Bid / ask execution mix** — what percentage of today's volume hit near the bid vs. near the ask vs. mid-spread. A contract that traded 80% near the ask says something very different than one that traded 60% at the bid.
* **Bull / bear / neutral percentages** — the sentiment breakdown at the contract level and the ticker-chain level.
* **Sweep %, multi-leg %** — what fraction of today's volume came through as sweeps or as legs of a complex strategy.
* **OI change** — the day-over-day change in open interest for that specific contract. This is one of the most important numbers on the Scanner: growing OI + high volume + aggressive bid/ask skew is a much stronger signal than growing volume alone.
* **Stock price, OTM %, IV, DTE** — the positioning context for that contract relative to where the underlying was.

Each row is effectively *a contract's day-long story*, compressed to one line.

### When to Use the Scanner

The Scanner is where you go when the question you're asking is about **contracts**, not about individual prints. Typical uses:

* **Which contracts actually moved today?** Sort by premium or trade count. The top of the list is where the day's money concentrated.
* **Which strikes had real new positioning?** Filter on positive OI change plus high volume. That's where risk is actually being put on, not rolled.
* **Which contracts traded aggressively to one side?** Use the bid-skew and ask-skew filters, or the contract sentiment slider. You'll surface contracts where one side dominated the day.
* **Historical review.** Pick a past date and re-run the same questions. What did unusual activity look like the day before earnings?
* **Structural filters you don't get in the Live Feed.** OI Growth signal, contract and chain sentiment sliders, OPEX Only, strike-range filters — these only exist on the Scanner because they're aggregate concepts that don't apply to a single print.

You won't use the Scanner for real-time reactions — its whole purpose is a day's activity, aggregated at once, and that's not the shape of problem you're solving when the tape is moving.

### Clicking a Scanner Row

Clicking a row in the Scanner opens the **same chart modal** as the Live Feed, with the same five views. Because the row you clicked is an aggregate, the chart modal's **Flow Orders** footer is especially useful here — it expands the aggregate back out into the individual prints that made it up. One thing that *doesn't* work from the Scanner is **Expand Trades** from a candle — that action creates a new Live Feed tab, and the Scanner isn't wired to do that. Everything else (Share to Discord from the modal, switching views, selecting candles, viewing the Strike Distribution) works identically.

## Flow Tracker: Following Prints After the Fact

The Tracker is a persistent list of trades you've chosen to remember. Unlike the Live Feed (ephemeral — rows scroll off) and the Scanner (query-driven — results change as filters change), the Tracker holds onto a specific set of prints across sessions so you can watch what happens to them.

### How Trades Get There

From the Live Feed, there are two ways to track a trade:

1. **Bookmark icon** — click the star on a trade row.
2. **Right-click → Track trade** — from the row context menu.

Both do the same thing: the trade is saved to your account. There's **no manual add** on the Tracker page itself. If you want to track a trade, you do it from the Live Feed at the moment it catches your eye.

🧠TL;DR

Bookmark aggressively. Trades that look interesting when they print are the ones worth checking an hour later, the next morning, at expiration, or right before earnings. The Tracker is where you build that memory. Removing a trade is a single click — there's no cost to bookmarking one that turns out to be noise.

### Two Tabs at the Top: Tracked Flow and Tracked Contracts

When you open the Tracker, there are two tabs at the top:

* **Tracked Flow** — the active one. This is the list of individual prints you've bookmarked. Each row is one specific trade.
* **Tracked Contracts** — contracts you save with the Contract Drilldown bookmark or from a Flow Compass card, tracked by *contract identity* (ticker + strike + expiration + C/P) rather than print-by-print. It shows each contract's current mid and spot.

### What the Tracked Flow View Shows

**On desktop**, the page is a split view:

* **Left**: a scroll-synced table of the trade's saved data at the time you bookmarked it — time, ticker, strike, type, expiration, spot, premium, etc. The fixed reference point for the trade.
* **Right (500px panel)**: **live-updating** fields — **Mid** (current mid price of the contract), **Spot** (current underlying price), **P/L %**, **P/L $**, and **Status**.

These live fields update continuously during market hours, so you can leave the Tracker open and watch your bookmarked prints move in real time.

**On mobile**, the desktop split-view is replaced with a vertical card stack. Each card shows the same fields; you swipe between cards instead of scrolling a table.

### Whale Status and OI Drift

The **Status** pill on each tracked trade isn't just "up" or "down" — Flowseeker infers a status from later trades and the next morning's open interest. It is not read from anyone's account, so it can't tell you who is trading:

* **STILL IN** — the trade is active, no close signal detected.
* **PENDING** — a large opposite-side trade printed today; it is confirmed or retracted when open interest updates the next morning.
* **PARTIAL N%** — the position is N% closed out. The whale is unwinding.
* **EXITED** — the position has been fully closed.
* **EXPIRED** — the contract reached expiration while still open.

These transitions are detected automatically throughout the session — you don't have to watch for them. When a new close is detected, the Tracker badge on the sidebar increments, so you know to check even if the page isn't open.

A secondary **OI Drift** badge on each row shows how much open interest has moved on that specific strike since the bookmark — a fast visual of whether the position sizing is growing, shrinking, or holding.

### Removing a Trade

Hover a row on desktop, or scroll to the top-right of a card on mobile, and you'll see a trash icon. Click it to remove the trade from your tracker. The action is instant and not reversible — but since the trade itself is just a saved reference, you can always re-bookmark the same print from a historical day in the Live Feed if you change your mind.

## The Chart Modal: The Shared Drill-Down

All three pages — Live Feed, Scanner, Tracker — open the same chart modal when you click into a specific trade. This is the deep-dive surface, and understanding its layout saves you a lot of navigation.

### The Five Views

Every chart modal has five views:

| View | What It Shows |
| --- | --- |
| **Contract Flow** | Stacked volume bars (no-side, bid, mid, ask) showing how aggressive the contract's intraday volume has been, with the contract's average fill price (VWAP) plotted on the right axis. Toggleable IV overlay and RVOL baseline. |
| **Underlying (Vol)** | Stock price history with options volume by bar. |
| **Underlying ($)** | Stock price history with options dollar premium by bar. |
| **Net Premium** | Cumulative net premium for that ticker over 1/2/5 day or longer intervals. This is where you read divergences between price and flow. |
| **Strike Distribution** | Bar chart of option activity by strike. 1D or 1W view. Clicking a strike opens a per-expiration breakdown. |

**On desktop**, the modal is a split pane: **Contract Flow is always on the left**, and a dropdown at the top-right of the right panel lets you pick any of the other four views. This means you can look at the contract's own price chart and the ticker-level Net Premium trend side-by-side without switching tabs.

**On mobile**, all five views are exposed as horizontal tabs — no split pane. Tap between them.

### The Footer

Below the charts, the footer has two tables you can switch between:

* **Flow Orders** — the list of individual trades that make up the candles you're viewing.
* **Vol / OI History** — a daily breakdown of volume and open interest for the contract, useful for seeing whether today's activity is outsized against recent history.

When you select a candle on the Contract Flow chart, the **Expand Trades** button at the top of the footer becomes active. On the Live Feed, clicking it creates a new filtered feed tab (as mentioned earlier). On the Scanner and Tracker, the button is there but doesn't open a new tab — it's a live-feed-specific action. Use **Clear Selection** to reset the candle filter back to the full contract.

### Header Actions

The header of the modal has three controls:

* **Refresh** — manually reload the chart data. Has a short cooldown so rapid clicks don't stack.
* **Share to Discord** — sends a PNG of the current chart (plus the trade context) to a configured Discord channel. Some users will see an upgrade prompt here instead; that's role-based.
* **Close (×)** — closes the modal. **Escape** also closes it.

## How the Three Pages Fit Together

A typical Flowseeker session uses all three pages in sequence:

1. **Open the Live Feed.** Read the overview bar. Glance at the tape to understand the session's tone.
2. **Set your filters.** Pick a tab configured for what you're watching today — sweeps only, a specific sector, whatever matters.
3. **Click interesting prints.** Use the chart modal's Net Premium and Strike Distribution views to get context. Use Expand Trades on any candle that looks structurally interesting.
4. **Bookmark what's worth following.** Trades that passed your filters *and* had clean structural context go into the Tracker. Trades that were interesting but didn't pan out stay in the Live Feed and scroll off.
5. **Check the Tracker once an hour or so.** See which of your bookmarked trades are still live, which have started closing out, and which the whale has already exited.
6. **At the end of the session, open the Scanner.** Switch to today's date and ask contract-level questions — which contracts had the most premium, which strikes had the biggest OI growth, which contracts had aggressive ask-side execution all day. The Scanner rolls up what the tape showed as thousands of prints into one line per contract, so patterns that the live tape was too fast to see become obvious.

The Live Feed is for reactive tape reading. The Scanner is for contract-level review. The Tracker is for memory. Using them together is how you build a real flow-reading workflow, rather than just staring at the live tape and hoping something jumps out.

## First Steps

If you've just read the [Introduction to Flowseeker](https://www.skylit.ai/learn/intro-to-flowseeker) and this article, here's what to actually do when you open the terminal:

1. **Go to the Live Feed.** Rename the default tab to something meaningful. Duplicate it once, rename the duplicate — you now have two tabs.
2. **Set different filter configurations on each tab.** Tab 1: broad view ($100K premium, Stocks only). Tab 2: narrow view ($250K premium, Sweeps Only, |Flow Score| > 50).
3. **Open the Columns panel.** Hide columns you don't use and drag the ones you do to the left.
4. **Try the ticker-scope search.** Type `!SPY` and press Enter to drop all SPY prints for the rest of the session. Toggle it back by removing the tag.
5. **Bookmark your first interesting trade.** It's now in the Tracker. Check back in an hour.
6. **After the close, switch to the Scanner.** Pick today's date and sort contracts by premium. The top of the list is where the day's institutional activity concentrated — scan it for contracts with high OI change, aggressive ask-side skew, or sweep percentages above baseline.

Do that for a week and the four-page workflow starts to feel natural rather than fragmented.

See this in Flowseeker

Flowseeker is a real-time institutional options flow scanner built into the Skylit Terminal, with a live feed, a full-day screener, and a persistent tracker for following prints after the fact.

[Try Flowseeker](https://app.skylit.ai/flow/live?utm_source=skylit_landing&utm_medium=website&sl_relay=1)

For the column-by-column breakdown of what you see in each row, see the [Introduction to Flowseeker](https://www.skylit.ai/learn/intro-to-flowseeker). For the conceptual foundation of why options flow matters at all, start with the [Options Flow Trading](https://www.skylit.ai/learn/options-flow) guide. For understanding why dealer positioning at the strike level determines whether flow amplifies or gets absorbed, see the [Dealer Positioning](https://www.skylit.ai/learn/dealer-positioning) guide.

## Frequently Asked Questions

### What's the difference between the Live Feed and the Scanner?

It's the **unit of analysis**. The Live Feed is a real-time tape where every row is a single print — trades appear as they happen and the feed keeps flowing. The Scanner is a contract-level view where every row is one contract (ticker + expiration + strike + C/P) with all of today's activity aggregated — total premium, total volume, bid/ask execution mix, sentiment scores, OI change, sweep percentage, and so on. Live Feed tells you *what just happened*. Scanner tells you *which contracts mattered today and how they traded as a whole*. They share the same underlying data and the same chart modal, but they answer different questions.

### What does "tracking" a trade actually do?

Bookmarking a trade from the Live Feed saves the full print data to your account. The Tracker then keeps the **Mid**, **Spot**, **P/L %**, and **P/L $** fields updated throughout market hours, infers from later trades and open interest whether the position appears to have been exited, and flags status transitions (STILL IN → PARTIAL → EXITED). Your tracked trades persist across sessions, so you can bookmark during one day and check back the next.

### What's the fastest workflow from seeing a print to following it?

Three clicks: bookmark the row in the Live Feed (or right-click → Track trade), then click the Tracker in the sidebar to see it alongside everything else you're watching. If you want the chart context first, click the row to open the chart modal, look at the Net Premium view to confirm it fits the session's flow, then close the modal and bookmark. Two or three extra seconds for a lot more certainty about what you're tracking.

### Start Trading Smarter

See these concepts in action with Skylit's dealer exposure tools.

[Get access](https://www.skylit.ai/#pricing)[Try Heatseeker](https://www.skylit.ai/#pricing)
