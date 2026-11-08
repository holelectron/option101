<!-- Source: https://www.skylit.ai/learn/reading-dark-pool-prints -->

# Reading Dark Pool Prints: The Tape and the Levels

# Reading Dark Pool Prints: The Tape and the Levels

flowseeker·9 min read

flowseekeratlasdark-poolinstitutional-flow

## The First Thing You Need to Unlearn

Here's the belief that ruins most people's relationship with dark pool data before it even starts: *"A big dark pool print means institutions are buying here."*

It doesn't. A dark pool print tells you that a large block of stock changed hands off-exchange at a specific price. It does **not** tell you who was the buyer, who was the seller, or which side was the aggressor. There is no direction attached to it. A $2 billion print is not "a $2 billion buy" — it's a $2 billion *transaction*, and somebody was on each side of it.

This matters because a whole cottage industry exists to sell you the opposite story. "Massive dark pool buying detected!" is a great headline and a terrible description of the data. Once you internalize that a print is direction-less, you stop trying to read tea leaves and start using dark pool data for what it's actually good at: showing you **where** large size transacted, and **how much** conviction (measured in dollars) was behind it.

This article covers the two places dark pool prints show up in the terminal — the **Dark Feed** in Flowseeker and the **dark pool overlay** on Atlas — and how to read each one honestly.

⚠️Warning

No dark pool print carries a side. If a tool tells you a specific dark pool print was "bullish" or "a buy," it's inventing information that doesn't exist in the data. Treat that as a red flag about the tool, not a signal about the stock.

## What a Dark Pool Print Actually Is

A dark pool print is an **off-exchange equity trade** — a block of shares that traded away from the public exchanges and was reported afterward. The terminal shows you a small, honest set of fields for each one:

| Field | What it tells you |
| --- | --- |
| **Time** | When the print was reported. |
| **Ticker** | The stock that traded. |
| **Price** | The exact price the block transacted at. |
| **Size** | How many shares. |
| **Notional** | Size × price — the dollar value of the block. This is the headline number. |
| **% AvgVol** | The print's size as a percentage of the stock's average daily volume. |
| **Sector** | The GICS sector the ticker belongs to, for context. |

That's it. No bid/ask. No "side." No sweep tag, no flow score, no greeks. Equity block prints simply don't carry that information, so the terminal doesn't pretend they do.

So what *can* you read from a print?

* **Notional = conviction scale.** A $50M block and a $2B block are different events. The dollar size is the closest thing you have to a measure of how much somebody cared.
* **Price = a level that mattered.** Someone moved real size at that exact price. That price level now has meaning — it's a spot where large participants were willing to transact.
* **Ticker and sector = where the big money is active.** A cluster of large prints in one name or one sector tells you attention is concentrated there.

What you *cannot* read: who's bullish, who's bearish, or what happens next. The print is evidence that something large happened — not a prediction.

## The Tape: Dark Feed in Flowseeker

The **Dark Feed** lives right next to the Live Feed in Flowseeker, and if you've used the Live Feed it'll feel immediately familiar — it's the same tape-reading experience, but for off-exchange equity blocks instead of options trades.

What you see is a live, scrolling table of prints with the columns above. A few things worth knowing:

* **It's a whale tape by default.** The feed defaults to a **$1,000,000 notional minimum**, so you're looking at blocks, not the full off-exchange firehose. That's a deliberate stance: the small prints are noise for most purposes, and the point of the feed is to surface size. You can lower the floor in the filters if you want everything.
* **Notional is styled to pop.** The Notional column is highlighted so the biggest blocks catch your eye as you scan — the same way the feed is built to make large size impossible to miss.
* **Filters that matter.** A date (and optional time-of-day) range, notional min/max, size min/max, share-price min/max, and sector filters. Set a date range in the past and the feed serves you that history instead of the live stream.
* **The familiar workflow.** Saved tabs (each with its own filters and column layout), ticker search with `!TICKER` to exclude a name, a results cap, pause/resume — when paused, new prints queue up and a counter shows how many are waiting, then flush in when you resume — plus shareable URLs and CSV/image export.

How you actually use it: scan for unusually large notionals, note *which tickers and sectors* are printing size, and treat those prices as levels to watch — not as directional signals.

💡Core Idea

The Dark Feed answers "where is large off-exchange size transacting right now?" It does not answer "what direction is it going?" Keep those two questions separate and the feed becomes a lot more useful — and a lot less misleading.

## The Levels: Dark Pool Overlay on Atlas

The same prints show up in a completely different shape on Atlas. Turn on the **Dark Pool** overlay in the chart settings and the largest prints for that symbol render as **horizontal dashed lines** drawn across the price chart, each labeled with its notional and date — something like `DP $2.2B · 5/15`.

This is the spatial view of the same data. Where the feed is a time-ordered list of events, the chart turns the biggest blocks into **price levels** sitting right on top of the candles.

Two controls shape what you see:

* **Top N** — how many of the largest prints to draw (1, 2, 3, or 5). This keeps the chart clean; you're only looking at the heaviest blocks, not every print.
* **Lookback** — how far back to search for those top prints (30, 45, 90, or 180 days).

A few details that keep you honest about what the lines mean:

* Each line is **one real print** at its **exact transaction price** — not a volume-weighted average, not a price band, not "accumulated volume at this level." It's a single block that happened.
* The **date is in the label**, not on the time axis. The line spans the whole chart horizontally because it represents a *price*, not a moment. Two big blocks at similar prices are told apart by the date in their labels.
* It's **equities only** — the overlay is skipped on futures symbols.

Why draw them as levels at all? Because a price where someone transacted enormous size is a natural place for the market to react. These lines often behave like soft support or resistance — not because of magic, but because that price proved it could absorb real size once already.

## Putting the Two Together

The feed and the chart answer different questions, and they're strongest used in sequence:

* **The Dark Feed tells you what's happening now.** A fresh, large block just printed in a name you care about.
* **The Atlas overlay tells you where size already transacted.** The biggest historical blocks, sitting as levels on the chart.

A simple workflow: spot a large print in the Dark Feed, pull that ticker up on Atlas, and see where the print sits relative to the existing dark pool levels and the current price. Is it printing right at an old block level (a price the market keeps coming back to), or in fresh territory?

And then the step that ties dark pool into the rest of the terminal: check those levels against the **GEX/VEX nodes** on the same Atlas chart. A dark pool level that lines up with a dealer positioning node is far more interesting than one sitting in structural no-man's-land. The dark pool print tells you size transacted there; the dealer map tells you what happens mechanically if price returns. That's confluence — and it's the same principle that makes the [flow subgraph on Atlas](https://www.skylit.ai/learn/reading-flow-on-atlas) worth combining with the heatmap rather than reading in isolation.

See this in Flowseeker

The Dark Feed streams large off-exchange blocks as they report, and the Atlas dark pool overlay turns the biggest ones into levels on your chart. Same prints, two views — neither one will ever lie to you about direction.

[Try Flowseeker](https://app.skylit.ai/flow/live?utm_source=skylit_landing&utm_medium=website&sl_relay=1)

## Frequently Asked Questions

### Does a dark pool print mean someone is buying?

No. A print is a transaction — there's a buyer and a seller on every one, and the data doesn't tell you which side was the aggressor or which side initiated. A large print means large size changed hands at that price, nothing more. Anyone presenting a single dark pool print as "buying" or "selling" is adding a story the data doesn't support.

### Why is there no flow score, sweep tag, or sentiment on dark pool prints?

Because off-exchange equity prints don't carry the information those labels would require. There's no bid/ask context, no side, and no options structure to classify. Rather than fabricate a score, the terminal shows you only what's real: price, size, notional, % of average volume, ticker, time, sector. The honesty is the point.

### Why does the Dark Feed default to a $1M minimum?

To keep it a whale tape rather than a firehose. The vast majority of off-exchange prints are small and uninteresting for spotting institutional-scale activity, so the default floor filters them out and lets the genuinely large blocks stand out. If you want to see everything, lower the notional minimum in the filters.

### Why does the Atlas overlay only show a handful of prints?

The overlay is designed to surface the *largest* blocks as levels, not to plot every print (which would bury the chart). You choose how many with the Top N control (up to 5) and how far back to look with the Lookback control. The goal is a small number of meaningful levels, not a cluttered chart.

### Are the dark pool lines on Atlas support and resistance levels?

They often act that way, but think of them as *evidence*, not guarantees. A price where a huge block transacted is a level the market has already proven it will trade size at, which is why price frequently reacts there. Treat a dark pool line like any other level: more useful when it lines up with other structure (a GEX/VEX node, a prior high/low, a round number) than on its own.

### Is the Dark Feed the same data as the dark pool lines on Atlas?

Yes — both come from the same set of off-exchange prints. The Dark Feed shows them as a time-ordered tape of everything matching your filters; the Atlas overlay picks out the largest few and draws them as horizontal price levels on a single symbol's chart. Same prints, two different ways of looking at them.

### Start Trading Smarter

See these concepts in action with Skylit's dealer exposure tools.

[Get access](https://www.skylit.ai/#pricing)[Try Heatseeker](https://www.skylit.ai/#pricing)
