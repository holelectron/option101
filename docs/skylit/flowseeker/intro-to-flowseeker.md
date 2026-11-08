<!-- Source: https://www.skylit.ai/learn/intro-to-flowseeker -->

# Introduction to Flowseeker: Real-Time Institutional Flow

# Introduction to Flowseeker: Real-Time Institutional Flow

flowseeker·13 min read

flowseekeroptions-flowinstitutional-flowdealer-positioning

## What Is Flowseeker

Flowseeker is a real-time institutional options flow scanner built into the Skylit Terminal. It captures every options trade across all U.S. exchanges as it happens and answers one question: **which trades actually carry conviction, and what's the structural context behind them?**

Every trade is enriched with 20+ columns that tell you not just what happened, but how aggressive it was, how much capital was behind it, and where it sits relative to the broader market. And because Flowseeker lives inside the same terminal as [Heatseeker](https://www.skylit.ai/learn/reading-heatseeker), you can immediately check the dealer positioning at any strike — no manual cross-referencing, no tab-switching to a separate tool. Heatseeker in the terminal starts with Initiate for 63 index and ETF symbols, and Pro covers the full ticker list.

🎯ELI5

Most scanners hand you a phone book and tell you the important calls are in there somewhere. Flowseeker highlights the ones that matter and tells you why.

## The Overview Bar: Read the Room Before You Read the Tape

Before you look at a single trade, the bar across the top of the page tells you what the market is doing in aggregate. Skipping this is a mistake. Individual trades mean different things depending on the environment they're printing into.

| Metric | What It Measures | How to Read It |
| --- | --- | --- |
| **Directional Sentiment** | Single-word session label: Bullish or Bearish, based on whether net institutional capital is flowing into calls or puts | The fastest read on the room. The first thing to glance at. |
| **Net Premium** | Running total: net call premium (NCP) minus net put premium (NPP), where each nets aggressive buying against aggressive selling | Deeply positive = institutional money leaning long. Deeply negative = leaning short. Near zero = balanced or confused. |
| **FIR (Flow Imbalance Ratio)** | How lopsided the flow is | Low FIR = balanced. High FIR = one side is dominating. The size of the imbalance, separate from its direction. |
| **P/C Ratio** | Live put/call ratio | Below 1.0 = calls dominate. Above 1.0 = puts. The classic measure, but live. |
| **RVOL (Relative Volume)** | Today's premium vs. a typical session at the same time of day | 1.5x = activity is 50% elevated. 3.0x = something unusual is happening. Below 1.0 = a quieter session than normal. |

These five numbers don't matter as much in isolation as they do *together*. A deeply negative Net Premium with high FIR is a different tape than a slightly negative Net Premium with low FIR — the first is institutional conviction, the second is noise. RVOL of 1.5 with FIR low is a normally busy day; RVOL of 3.0 with FIR high is the market telling you to pay attention. Read them as a single composite signal, not five separate ones.

🧠TL;DR

Glance at the overview bar before diving into individual prints. If Net Premium is deeply negative, RVOL is elevated, and FIR is high, the market is telling you institutions are aggressively positioned in one direction. Every trade below inherits that context. A bullish sweep against a bearish backdrop is a different trade than a bullish sweep in a bullish session.

## Reading a Trade Row

Each row in the feed is a single options trade — or an aggregated group of related prints. Twenty-two columns. You don't need all of them at once, but knowing what each one means gives you the ability to tighten your lens as you build intuition.

Here's the full set, and why each one matters.

| Column | What It Shows | Why It Matters |
| --- | --- | --- |
| **Date/Time** | When the trade executed. Sweep and multi-leg icons appear here. | Shows when in the session the print hit — useful for spotting clusters around the open, close, or known news catalysts. The icons tell you instantly if it's a sweep or a complex strategy. |
| **Ticker** | Underlying symbol | What's moving. |
| **Strike** | Strike price | Where the bet is placed relative to spot. |
| **C/P** | Call or Put | Direction of the bet. |
| **OTM %** | How far out of the money, as a percentage | A 5% OTM call is a moderate bet. A 20% OTM call is a lottery ticket. This single number tells you how aggressive the positioning is. |
| **Exp** | Expiration date | When the bet expires. |
| **DTE** | Days to expiration | Under 7 DTE is urgent. Over 30 is positioning. DTE shapes everything about how a trade behaves — the Greeks are different, the decay is different, the intent is different. |
| **Fill** | Price per contract | What the trader paid for each contract. |
| **Spread** | Visual bar showing position within the bid-ask | One of the most important columns. Near the ask means aggressive buying. Near the bid means aggressive selling. Middle is ambiguous. This is how you read intent, not just activity. |
| **Side** | Bid, Mid, or Ask | Text label for the same thing the Spread bar shows visually. |
| **Flow Score** | Directional conviction, –100 to +100 | A proprietary Skylit score that condenses the print into a single directional lean. High positive means strongly bullish, high negative means aggressively bearish, near zero means ambiguous or hedged. Covered in depth in a separate article. |
| **Contract Ratio** | Bid/ask aggressiveness at the contract level | Measures how the contract-level pricing reflects buyer vs seller pressure. |
| **Size** | Number of contracts | Size alone is misleading — 1,000 contracts in SPY is background noise, 1,000 contracts in a small-cap is a freight train. Always read size alongside premium and ticker. |
| **Prem** | Total dollar premium (Fill × Size × 100) | The actual capital committed. Premium is almost always a better measure of conviction than contract count. |
| **Vol** | Today's volume for this contract | High volume on a single strike/expiry means institutional interest is building at that level. |
| **OI** | Open interest (prior day's close) | How many contracts were already open. Baseline for context. |
| **ΔOI** | Change in open interest | Positive ΔOI means new positions opening. Negative means positions closing. This tells you whether the flow is creating new risk or unwinding old risk. |
| **Spot** | Underlying price at time of execution | Where the stock was when the trade hit. |
| **IV** | Implied volatility | Higher IV means the market is pricing in more movement. IV expanding on one side (calls or puts) can confirm directional intent. |
| **V/OI** | Volume ÷ Open Interest | Above 1.0 means more contracts traded today than existed yesterday. That usually means new positioning, not rolling or closing. |
| **Strategy** | Detected multi-leg structure | Vertical spread, straddle, iron condor, etc. Blank for single-leg trades. |
| **Earnings** | Days to next earnings | Trades placed 1–3 days before earnings carry fundamentally different intent than trades placed in quiet periods. |

That's the full picture. But you don't need to process all 22 columns to start reading flow effectively.

💡Core Idea

Start with five columns: **Ticker, Side, Premium, Flow Score, and DTE.** Those five give you a fast read on what's moving, in which direction, with how much capital, and on what time horizon. Add columns as you build intuition. Don't try to read the full 22 on day one.

## Filtering: The Difference Between Signal and Noise

The unfiltered feed shows everything. That's intentional — some traders want the full tape. But if you're looking for actionable institutional prints, you need to filter. The sidebar gives you the tools. The question is which ones to use.

### The Filters That Matter Most

**Premium** is filter number one. The default minimum is $50,000. That's a reasonable starting point, but raising it to $100K or $250K immediately removes most retail noise and leaves you with institutional-sized prints. If you're only going to set one filter, this is the one.

**Equity Type** lets you toggle Stocks, ETFs, and Indices independently. ETF flow (SPY, QQQ, IWM) is structurally different from single-name flow. It reflects macro positioning, hedging, and index rebalancing rather than single-stock conviction. If you trade individual names, turning off ETFs and Indices removes a lot of noise.

**Sweeps Only** isolates intermarket sweep orders — trades that cleared liquidity across multiple exchanges simultaneously. A sweep signals urgency. The buyer or seller is lifting every available offer across venues rather than waiting for fills. That's a qualitatively different kind of intent than a patient limit fill.

**Flow Score** lets you set a minimum or maximum, or toggle absolute value mode to catch strong conviction in either direction. Setting |Flow Score| > 50 keeps only the higher-conviction prints.

### Filters for Context

**Days to Expiry** focuses on specific time horizons. Under 7 DTE catches urgent, near-term bets. Over 30 DTE catches positioning plays. The intent behind a trade changes dramatically with its time horizon.

**Days to Earnings** filters by proximity to earnings. A $500K call sweep placed 2 days before earnings is a different trade than the same sweep placed 40 days out. The toggle lets you calculate this relative to today or relative to the trade date — useful when reviewing historical flow.

**Sector & Industry** lets you select sectors (Technology, Healthcare, Energy, etc.) and drill into industries within them. When institutional money rotates, it doesn't move ticker by ticker — it moves by sector. This filter makes rotation visible.

**Side** filters by execution side: Bid (aggressive sells), Mid, or Ask (aggressive buys). Filtering to Ask-only in a bearish session can surface contrarian institutional buying that the overview bar masks.

🎯ELI5

Filters are a funnel. Start wide — $100K premium minimum and stocks only. That might give you 200 trades per session. Add sweeps only and it drops to 30. Add a minimum Flow Score and it drops to 10. The goal isn't zero — it's getting to the 10–20 prints per session where the structural case is worth evaluating. You can always widen the funnel if you're missing something.

## Clicking a Trade: Going Deeper

The feed shows you what happened. Clicking a row shows you the context around it.

**Contract Chart** — the price history of that specific option. Did the contract run after the print? Did it fade? This is the most direct measure of whether the trade "worked."

**Underlying Chart** — the stock or ETF price chart with the trade overlaid. Shows you where the stock was when the print hit and what happened next. Useful for understanding whether the flow led price, confirmed it, or diverged from it.

**Net Premium Chart** — cumulative net premium for that ticker over selectable timeframes (1 day, 2 days, 5 days, etc.). This is where you see the bigger picture. If institutional flow has been consistently bullish for three days and a large bearish print surfaces, that print might be a hedge against the existing position, not a directional reversal. Context like this prevents you from overreacting to isolated prints.

Divergences are especially important here. Price rising while net premium falls means institutional money is quietly exiting or hedging even as the stock grinds higher. That divergence often precedes a reversal. The net premium chart makes it visible.

**Strike Distribution** — a visual breakdown of where options activity is concentrated by strike. If volume is clustered tightly at two or three strikes, that concentration tells you something about where the market expects action. If it's spread across 20 strikes, there's no institutional consensus.

Right-clicking any row gives you quick actions: filter to matching trades (same ticker, same expiry), filter out a noisy ticker, or track the trade for follow-up.

## First Steps

If you're opening Flowseeker for the first time, don't try to use everything at once. Here's a setup that works:

1. **Set premium minimum to $100,000.** This removes the vast majority of retail noise immediately. You're looking at institutional prints only.
2. **Select Stocks only.** ETF and index flow behaves differently and can be overwhelming when you're learning the feed. Add them back once you're comfortable.
3. **Watch Side and Flow Score first.** Side tells you direction. Flow Score tells you conviction. Together, they're the fastest read on whether a print matters.
4. **Click trades that stand out.** Open the chart modal. Check the net premium trend. See if the trade aligns with price action or diverges from it. Start building a feel for which prints lead to follow-through and which ones don't.
5. **Cross-reference with Heatseeker.** This is the step that separates Flowseeker from every other scanner. When you spot a high-conviction print, switch to the Heatseeker map for that ticker. If the sweep landed at a –GEX zone where dealers are short gamma, the forced hedge will chase the move — that's fuel. If it landed at a +GEX wall, the dealer flow absorbs it. Same print. Different structural outcome. That context doesn't exist in any standalone flow scanner.

See this in Flowseeker

Flowseeker surfaces real-time institutional options flow with 20+ data columns and live dealer positioning context from Heatseeker — all inside the Skylit Terminal.

[Try Flowseeker](https://app.skylit.ai/flow/live?utm_source=skylit_landing&utm_medium=website&sl_relay=1)

For the conceptual foundation behind reading options flow, start with the [Options Flow Trading](https://www.skylit.ai/learn/options-flow) guide. For understanding why dealer positioning at the strike level determines whether flow amplifies or gets absorbed, see the [Dealer Positioning](https://www.skylit.ai/learn/dealer-positioning) guide.

## Frequently Asked Questions

### Is "Side: Ask" the same as a confirmed buy?

Not quite — but it's the best available signal of intent. The tape doesn't identify a verified buyer or seller. Side is inferred from where in the bid-ask spread the print landed: trades that cleared near the ask suggest aggressive buying pressure, trades near the bid suggest aggressive selling pressure, and mid-spread trades are ambiguous. Treat Side as a strong directional hint with a well-understood basis, not a certainty. It's also why the Spread column (the visual bar showing position within bid-ask) is worth reading alongside Side — the bar makes the confidence of the read obvious at a glance.

### Should I focus on Size or Premium — which one matters more?

Premium, almost always. Size can be misleading: 1,000 contracts at $0.25 is $25,000 in real money, while 500 contracts at $8.00 is $400,000. Premium is the actual capital committed, so it's the better measure of institutional conviction. Size becomes meaningful mainly when you read it alongside Open Interest — a 500-contract trade on a strike with 200 OI is a much bigger deal than a 5,000-contract trade on a strike with 100,000 OI.

### What's the difference between Volume and Open Interest?

Volume is today's trading activity for a specific contract. Open Interest (OI) is the count of positions still open at yesterday's close — contracts that have been traded but not yet closed or expired. Volume resets every day; OI accumulates until positions are closed or expire.

The useful comparison is between the two. When today's volume at a strike exceeds its open interest (V/OI > 1.0), that usually signals new positioning rather than rolling or closing existing trades. Without that context, a high-volume print on a strike with millions of open contracts might just be routine churn.

### What's the difference between V/OI and ΔOI? They sound similar.

They answer different questions.

* **V/OI** is a ratio: today's volume divided by yesterday's open interest. It tells you how much today's activity scales relative to the existing base. V/OI above 1.0 means more contracts traded today than were open yesterday — a strong hint that new positioning is happening.
* **ΔOI** is a day-over-day change: how many more (or fewer) contracts are open at today's close versus yesterday's. It directly tells you whether positions are being opened (positive ΔOI) or closed (negative ΔOI).

A high V/OI with a small positive ΔOI often means lots of intraday churn that mostly netted back out by the close. A high V/OI with a *large* positive ΔOI means real new risk is being put on. Reading them together is much more informative than either alone.

### Why does OTM % matter when the strike and spot are already shown?

OTM % normalizes aggressiveness across tickers. A $5 OTM call on SPY (around $580 spot) is a very different bet than a $5 OTM call on AAPL (around $200 spot), even though both look "$5 out of the money" on paper. Reading OTM % puts every trade on a consistent scale — 1–2% OTM is near-the-money, 5–10% is a moderate directional bet, and 20%+ is a lottery ticket regardless of ticker. This makes it much faster to compare aggressiveness across the feed without having to do the math in your head.

### Start Trading Smarter

See these concepts in action with Skylit's dealer exposure tools.

[Get access](https://www.skylit.ai/#pricing)[Try Heatseeker](https://www.skylit.ai/#pricing)
