<!-- Source: https://www.skylit.ai/learn/reading-flow-on-atlas -->

# Reading Flow on Atlas: How the Bars Work, Every Setting Explained, and Why There's No 'Best Configuration'

# Reading Flow on Atlas: How the Bars Work, Every Setting Explained, and Why There's No 'Best Configuration'

flowseeker·15 min read

flowseekeratlasoptions-flowinstitutional-flowdealer-positioning

## The Most-Asked Question, and Why It's the Wrong One

If you've spent any time around flow analysis, you've seen the question — and probably asked it yourself: *"What flow settings do you use?"* I'm going to argue, in the rest of this article, that it's the wrong question to be asking in the first place.

There's no preset that prints alpha. No magic combination of toggles that turns the flow subgraph into a buy signal. People asking for "the best settings" are looking for a recipe, and flow doesn't work that way — the mindset itself is what's getting in the way.

Each setting on the Flow popover is a **lens**, not an ingredient. You don't combine lenses into a permanent configuration — you rotate through them, looking for what survives across multiple views. And then, critically, you anchor whatever survives to the GEX/VEX nodes on the same chart, because flow without dealer positioning context is just half a thesis.

This article does three things:

1. Explains exactly what the flow bars on Atlas are showing — because most users get this wrong on day one.
2. Walks through every setting in the flow filter popover, what it does, and what it reveals.
3. Lays out the right way to use them: confluence across lenses, plus structural cross-check on the heatmap.

If you've been treating flow settings as a configuration problem, this article reframes them as an investigation tool.

## What the Flow Bars Actually Show

Before any settings discussion, the bars themselves. The flow subgraph is a second pane that sits underneath your price chart on Atlas, time-aligned to the same candle interval. When the toggle is off (the default), it doesn't render. When you turn it on, two stacked histogram series appear:

* **Calls plot upward.** Positive values, one bar per candle bucket.
* **Puts plot downward.** Negative values, mirrored below the zero line.

The single most important thing to understand: **these are premium dollars, not contract counts and not share volume.** A bar showing $4M of calls means $4M of call premium was paid in that bucket. One $4M sweep dwarfs forty $100k retail orders, and that's deliberately the point — the chart is weighted by the size of the money behind each print, not the number of clicks.

The bars are clipped to the candle time range, so the flow pane never extends past the price data. Hovering over any bucket pops a crosshair tooltip showing **Calls / Puts / Net** for that interval — Net being call premium minus put premium. Net is what tells you whether the bucket leaned bullish or bearish, and by how much.

💡Core Idea

"Premium, not volume" is the thing newcomers miss most often. A bucket with low contract count but huge premium means *someone with conviction paid up* — those are the prints that move price. A bucket with high contract count but small premium is mostly noise — retail one-lots, scalpers, hedges.

### Click a Bar to See Who Drove It

Click any flow bar — and only on the flow pane itself; clicks on the candle pane do nothing — and a sidebar opens on the right. **FLOW BUCKET**, the time window in your chart timezone, total trade count for the interval, three stat tiles for **Net / Calls / Puts**, and then the section that matters: **Top contracts.**

The top-contracts list shows the specific options that drove the bucket. Each row has the strike, C or P, expiration date, days to expiration, premium paid, and percentage of the bucket's total. If three contracts account for 80% of the bucket's premium, that's a concentrated positional bet. If the premium is spread across thirty contracts, that's program flow or rotation. The drilldown is what turns "the bar is green" into "five sweeps of the same OTM weekly are doing all the work."

Click the same bar again to close the sidebar. Escape works. The X works. Clicking outside the chart works. The sidebar is a quick lookup, not something you live in.

One important detail: the same Flow filters that drive the histogram are passed into the drilldown fetch. If you have Sweep Only on, the sidebar only counts sweep prints — so the totals always match the bar you clicked. This matters because it means filtering changes what the drilldown shows, which is itself a useful investigation tool.

## Every Flow Setting, Explained

The Flow toggle lives in the chart Settings panel. Turning it on adds the second pane and, by default, *no filters are applied* — every flow print contributes. The cog icon next to the Flow toggle opens the filter popover, where the actual lenses live.

| Setting | What it does | When you'd reach for it |
| --- | --- | --- |
| **Single Leg Only** | Excludes prints that are part of a multi-leg strategy (spreads, collars, condors). Only standalone directional trades contribute. | You want clean directional conviction, not spread legs that net out economically and just look directional in isolation. |
| **Sweep Only** | Only sweep-classified prints contribute. The bars **shrink** to the sweep portion — they don't get scaled up. | You want urgency: institutions paying up across exchanges to fill *now*, rather than working an order patiently. |
| **OTM Only** | Excludes ITM and ATM strikes. Only out-of-the-money options contribute. | You want speculative directional bets, not deep-ITM proxies for stock or pure hedging activity. |
| **Ask Side Only** | Only prints executed at or above the ask. | You want aggressive opening flow — buyers crossing the spread to get filled, not closing or passive fills. |
| **DTE Min / Max** | Filters by days to expiration on each contract. | Cut out 0DTE noise; isolate directional weeklies; isolate long-dated structural conviction; etc. |
| **Min Flow Score %** | Only contracts whose absolute Flow Score exceeds the threshold. | Keep only prints that Flow Score ranks as more directional. Flow Score is a ranking aid, not a forecast. |

A few of these need a closer look, because the way they reshape the bars is not always intuitive.

### "Sweep Only" Is Compositional, Not Magnitude

Most users assume turning on Sweep Only makes the bars *bigger* — bigger sweeps, bigger bars. It's the opposite. Sweep Only changes which trades enter each bucket. Non-sweep prints are simply removed. So a bucket that was $4M with everything contributing might become $400k with Sweep Only on, because only $400k of that bucket's premium was actually executed as sweeps.

The right way to read it: turn on Sweep Only and look at how much of the original bar survives. If most of it survives, the original lean was urgent flow. If the bar collapses to a fraction, the original print was patient capital — institutions working an order over time, not trying to grab it before the move. Both are useful information; they're just different information.

### "Ask Side Only" Isolates the Aggressive Side

A trade printed *at the ask* (or above it) means the buyer paid up to get filled. A trade *at the bid* means the seller hit the bid to get out. Mid-prints could be either. Ask Side Only removes everything except the most aggressive end of the spectrum — buyers who weren't willing to wait.

Stack Ask Side Only with Sweep Only and you're looking at the most aggressive opening institutional capital in the bucket. That's a high-quality lens; very little of what survives there is junk.

### "Min Flow Score %" Is the Composite Threshold

Flow Score is Flowseeker's directional score for each print, from -100 (bearish) to +100 (bullish). It ranks how directional a print looks; it is not a measure of conviction or a forecast. Setting the Min Flow Score filter to, say, 70% means only contracts whose absolute Flow Score is above 70% feed the bars.

If you don't have an opinion yet on what's "noisy" vs. "interesting," leave this off. Once you've used Flowseeker for a while and you've calibrated to what scores look like in real conditions, this becomes a fast way to clean up the subgraph in tickers with heavy flow.

### "DTE Min / Max" Is About Trade Type

A bucket dominated by 0DTE flow tells you something very different from one dominated by 30DTE flow. 0DTE is largely intraday speculation and gamma scalping; longer-dated flow is more often directional positioning that has to play out over days or weeks. Setting a DTE minimum of, say, 7 strips out the 0DTE froth and shows you what *positioning* — not gambling — is doing.

Setting a maximum is rarer but useful for the inverse: if you're trying to see what 0DTE traders are doing, set Max DTE to 1 and the noise from longer-dated flow disappears.

## Why "What Settings Do You Use?" Is the Wrong Question

The reason there's no "best settings" answer is that **filters are subtractive.** They don't add insight. They remove things so you can see what's left. Different filters reveal different things. There is no single configuration where everything important is visible at once — you'd just be back to the unfiltered view.

A trader who runs only Sweep Only will miss slow institutional accumulation that paints the bucket green over an hour. A trader who runs only OTM Only will miss the deep-ITM directional bet that printed at 9:31 ET. Both of those trades can be the trade of the day, depending on the day, and no single filter setup catches both.

The right mental model: **pick a question, pick the lens that answers it. Then pick another question, pick another lens, and see if both answers point the same direction.** That's what flow analysis is. It's not configuration; it's iteration.

🎯ELI5

Lens stacking is like polarized sunglasses. You don't ask "what's the best polarization angle?" You rotate them until what you want to see pops. Then you rotate them again to confirm it wasn't just glare. The angle that revealed the fish at noon doesn't help at sunset, and that's fine — you just rotate.

## Building Confluence Across Lenses

This is the methodology. Same chart, same bucket, same bar, multiple lenses. Each lens is a vote.

1. **Start unfiltered.** Establish the baseline. Is the bucket green or red? How big? Is the lean concentrated in one bucket or spread across the session? This is your "what does the unfiltered tape look like" reading.
2. **Flip on Sweep Only.** Does the directional lean survive? If yes, urgency is real — institutions weren't willing to wait. If the bucket collapses, the original lean was patient capital, which is interesting information but a different trade thesis.
3. **Flip on Ask Side Only (with Sweep Only on).** Same direction? Now you're looking at the most aggressive, opening institutional flow in the bucket. If the bar still leans the same way, that's a strong vote.
4. **Tighten DTE.** Set Min DTE to 7. Does the conviction concentrate in weeklies and longer (positioning), or did most of it disappear (0DTE intraday speculation)? Both are valid signals; they just describe different participants.
5. **Open the drilldown sidebar.** Click into the bucket. Are the top contracts concentrated in 2-3 strikes (positional bet) or spread across twenty contracts (program flow)? Concentration is conviction.
6. **Toggle filters off and on quickly.** This is how you can tell what's *driving* a bucket. If turning on OTM Only barely changes the bar, the bucket was mostly OTM already. If it collapses, the bar was carried by ITM positioning.

Each layer that survives is a vote. Three or four lenses pointing the same way is what you're hunting for. One lens pointing somewhere and three contradicting it is the signal you almost-took-a-bad-trade and the system caught it for you.

## The Layer Almost Everyone Misses: Combine Flow With Heatmap Nodes

Here's the single highest-leverage thing about flow analysis on Atlas, and the reason the flow subgraph lives on the same chart as the GEX/VEX overlay rather than in its own page: **flow tells you what institutions are doing. The heatmap tells you what dealers will be forced to do in response to price moving.** Same print, different structural context, opposite outcomes.

Walk through it. Imagine you've found a high-confluence flow bucket — the lean survives Sweep Only, survives Ask Side Only, the drilldown shows three strikes 2-3% out of the money concentrating most of the premium, and the contracts are weeklies. Strong setup. Now look at where those strikes sit on the GEX/VEX overlay on the same chart.

**Case A: The strikes are sitting in a –GEX zone above current price.** Dealers are short gamma at those strikes. If price grinds up to that zone, the dealer hedge *amplifies* the move — they have to buy more underlying as price climbs. The flow says institutions are pressing long. The structural map says "if they're right, the move accelerates." That's the trade.

**Case B: Identical flow, but the strikes sit at a +GEX wall.** Dealers are long gamma at those strikes. If price approaches, the dealer hedge *absorbs* the move — they sell into rallies, dampening upside. The flow still says institutions are pressing long. But the structural map says "even if they're directionally right, the dealer hedge will pin the move into the level." That's *not* the same trade, even though the flow looks identical.

This is what people who say "I don't get why flow doesn't work" are missing. Flow alone is half the thesis. Same print, opposite structural context, opposite outcome.

🧠TL;DR

This is why Atlas exists as a single workspace instead of two separate tools. The flow pane and the GEX/VEX overlay are designed to be read in the same eye scan, on the same chart, against the same price. If you find yourself flipping between Flowseeker and Heatseeker as separate tabs to make this cross-check, you're working harder than you need to.

For a deeper treatment of *why* dealer positioning at a strike determines whether forced hedging amplifies or absorbs a move, see the [Dealer Positioning](https://www.skylit.ai/learn/dealer-positioning) and [Gamma Exposure (GEX)](https://www.skylit.ai/learn/gamma-exposure) articles. The argument here is that those structural concepts and the flow bars belong together — and the chart is the place that lets you do it.

## A Reference Checklist (Not a Settings Preset)

Before taking a trade off a flow bucket on Atlas, the checks that matter:

1. Does the directional lean survive **Sweep Only**?
2. Does it also survive **Ask Side Only**?
3. Does the **drilldown** show 2–3 dominant strikes, or noise spread across the chain?
4. Where do those dominant strikes sit on the **GEX/VEX overlay**? At a wall, in an air pocket, in a –GEX zone?
5. Does the **price chart itself** support the thesis — trend, level, structure?

Five checks, not a settings preset. Anyone who tells you they have one configuration that does all this work for them is selling you something.

See this in Flowseeker

The flow subgraph is built into Atlas so you can read flow and dealer positioning on the same chart, in the same eye scan. Open Atlas, enable Flow, and start rotating lenses.

[Try Flowseeker](https://app.skylit.ai/flow/live?utm_source=skylit_landing&utm_medium=website&sl_relay=1)

## Frequently Asked Questions

### What's the actual best flow filter setup?

There isn't one. Different filters reveal different things, and any single configuration only catches a subset of the trades worth taking. The right approach is to rotate through filters, look for what survives across multiple lenses, and combine that with where the contracts sit on the GEX/VEX overlay. This article exists specifically to push back on the configuration-mindset; please go re-read the "Why 'What Settings Do You Use?' Is the Wrong Question" section.

### Why did my flow bars get smaller when I turned on Sweep Only?

Because Sweep Only is *compositional*, not magnitude. It removes non-sweep prints from each bucket — the bars get *purified*, not magnified. If a bucket goes from $4M unfiltered to $400k with Sweep Only on, that means only $400k of that bucket's premium was actually executed as sweeps. The remaining $3.6M was patient flow worked over the interval, which is a different (still useful) signal.

### Are the flow bars showing options volume or premium?

Premium dollars. One bar represents the total call premium (up) or put premium (down) that printed during that candle's interval. A bar can be very tall with a small contract count if a single big-money print landed in the bucket, and shorter than expected with a high contract count if most of the activity was small prints. Premium-weighted is the design choice, because the prints that move price are the ones with money behind them.

### Why are my flow bars empty after turning on filters?

Filter combinations can null out a bucket — every print in that interval gets excluded by at least one filter. If this is happening across the whole session, your filters are likely too tight. Loosen them one at a time until the baseline reappears, then tighten back from there. The drilldown sidebar also won't open on a bucket that has no qualifying prints.

### Do my flow filter settings persist across sessions?

Yes. Your chart settings — including the Flow toggle and the filter popover values — are saved locally and restored next time you open Atlas. You don't have to reconfigure the lenses every session. (If you want to start fresh, the popover has individual controls for each filter; there's no global "reset filters" button.)

### How do the flow bars on Atlas relate to the Live Feed?

Same data, different resolution. The Live Feed shows individual prints in tape order — every trade as it happens, one row at a time. Atlas aggregates those same prints into time buckets aligned to your chart interval. So Live Feed is the microscope; Atlas is the time-series view. Use Live Feed when you want to read tape character; use Atlas when you want to see how flow stacks against price structure and dealer positioning.

### Does the drilldown sidebar use the same filters as the bars?

Yes. The same filters that drive the histogram are passed into the drilldown fetch, so the bucket totals always match the bar you clicked. This is intentional — if you have Sweep Only on, the "Top contracts" list only shows contracts with sweep prints in that bucket. Toggle a filter, and both the bar and the drilldown re-aggregate together.

### Should I always trust a high-confluence bucket?

No — that's the whole point of the structural cross-check. A bucket can survive every flow lens you throw at it and still be a bad trade if the contracts sit at a +GEX wall that absorbs the move. Or if price structure (the candles, levels, trend) doesn't support the direction. Confluence across flow lenses is necessary; combining that confluence with dealer positioning context is what makes it sufficient. The flow subgraph by itself is a hypothesis. The chart and the heatmap together are what confirm or reject it.

### Start Trading Smarter

See these concepts in action with Skylit's dealer exposure tools.

[Get access](https://www.skylit.ai/#pricing)[Try Heatseeker](https://www.skylit.ai/#pricing)
