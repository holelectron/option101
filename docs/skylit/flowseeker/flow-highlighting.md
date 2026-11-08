<!-- Source: https://www.skylit.ai/learn/flow-highlighting -->

# Flow Highlighting: Color-Coding the Prints That Matter

# Flow Highlighting: Color-Coding the Prints That Matter

flowseeker·12 min read

flowseekeroptions-flowinstitutional-flowlive-feed

## What Flow Highlighting Does

The live feed shows everything that prints. Most of it is noise — routine market-maker rebalancing, retail one-lots, hedges against existing positions, spread legs that look directional in isolation but aren't. Manually scanning the V/OI and Size columns to find the prints that actually represent new institutional positioning is slow, and slow scanning is what you're trying to escape with a flow scanner in the first place.

**Flow Highlighting** is the feature that automates that visual triage. Once configured, Flowseeker color-codes every row in the feed based on whether the trade represents new positioning being put on (loud color), unusual contract activity that probably reflects new positioning (medium color), or routine churn (quiet color). At a glance, you see which prints to investigate without reading any column values.

This article explains the analytical foundation behind the two highlighting rules — the relationship between Size, Volume, and Open Interest — and then how to set up and use the feature effectively. The conceptual section is the heart of the article; once you understand *why* Volume > OI and Size > OI matter, the configuration is mechanical.

This article assumes you've read the [Introduction to Flowseeker](https://www.skylit.ai/learn/intro-to-flowseeker), which explains the basic columns including Size, Volume, OI, and V/OI.

## First, a Refresher: Size, Volume, and Open Interest

These three numbers get casually thrown around in flow articles, but the relationship between them is what makes Flow Highlighting work. Worth getting precise.

### What each one measures

* **Size** is the number of contracts in a *single specific trade*. One print on the tape. Size = 100 means one print of 100 contracts.
* **Volume** is the *total* number of contracts traded today on a specific contract (ticker + strike + expiration + C/P). It's the sum of every print's Size for that contract since the open. Volume is cumulative across the session.
* **Open Interest (OI)** is the number of currently outstanding contracts — positions that have been opened but not yet closed or expired. OI is reported as **yesterday's close**. Today's true OI isn't knowable until the day ends, because every trade during the session can either open new positions, close existing ones, or both, and the exchange only publishes the net change once daily settlement is done.

### How positions actually move

Every trade has a buyer and a seller. Each side is either *opening* a new position or *closing* an existing one. That gives four possible combinations, and the OI change depends on which combination applies:

| Buyer | Seller | OI change |
| --- | --- | --- |
| **Opens** (buy to open, going long) | **Opens** (sell to open, going short) | **+1** — new contract created |
| **Opens** (buy to open, going long) | **Closes** (sell to close, was long) | **0** — position transfers from one party to another |
| **Closes** (buy to close, was short) | **Opens** (sell to open, going short) | **0** — position transfers from one party to another |
| **Closes** (buy to close, was short) | **Closes** (sell to close, was long) | **−1** — contract destroyed |

The tape doesn't tell you which combination any given trade is. We see "X contracts traded" with no information about whether each side was opening or closing.

### Why this matters for reading flow

Volume alone is misleading. A contract can have very high volume from pure churn — buyers and sellers all closing existing positions, with no new institutional money entering. If you only look at Volume in isolation, you can't distinguish *"institutions are aggressively positioning here today"* from *"institutions are quietly exiting positions they put on weeks ago."*

Comparing Volume against OI is what separates those two cases. That's the entire analytical reason Flow Highlighting exists — to surface the prints where positioning is genuinely happening, not just where contracts are changing hands.

## Why Volume > OI Is a Strong Signal

Here's the math, and it's worth walking through carefully because it's the core of the first highlighting rule.

If yesterday's OI was 100, then collectively the longs hold 100 contracts and the shorts hold 100 contracts (every contract has one of each). The maximum number of contracts that could be *closed* today, in total, is 100 — you can't close more contracts than were open. (Strictly: closing trades can only consume what's already in OI.)

So if today's volume reaches 150 on a contract with yesterday's OI of 100, then **at least 50 of those 150 contracts must have been new opens**. There's no way around it mathematically — the closing capacity is capped at 100.

That gives us the threshold:

> **When today's volume exceeds yesterday's open interest, new positioning is provably happening on that contract — even if we can't tell from the tape exactly which trades are the new opens.**

V/OI > 1.0 is the standard way this gets expressed (Volume divided by Open Interest greater than 1). It's been a well-known options-flow signal for a long time. What Flow Highlighting does is show it to you visually, on every row of the feed, instead of making you read the V/OI column on each row.

### What V/OI > 1 doesn't tell you

It doesn't tell you direction (calls or puts, bullish or bearish — that's what other columns and the chart modal are for). It doesn't tell you the *magnitude* of the new positioning — V/OI of 1.05 is just barely over the threshold; V/OI of 5.0 is enormous. The highlighting rule is binary: either Volume > OI fires, or it doesn't. For magnitude, you still need to read the column.

But as a triage signal — "this contract has new positioning today, look closer" vs. "this contract is routine churn, skip" — the rule is exactly what you want.

## Why Size > OI Is an Even Louder Signal

Volume > OI is about the contract's *cumulative* activity for the day. **Size > OI** is about a *single trade*. One print, by itself, larger than yesterday's entire open interest.

This is the loudest signal a single print can give you. Walk through the math: if a single trade's Size exceeds yesterday's OI, then by definition, the trader on the buy side cannot be closing — they couldn't have held more contracts than the entire open interest of the contract. (No single party can hold more than 100% of the OI.) So when Size > OI fires, that trade is essentially *guaranteed* to be opening a new position.

There's a narrow edge case: a trader could open a large position intraday at 10am and close it intraday at 11am. The 11am close trade would also have Size > OI (since OI only updates at end of day). But the 10am opening trade *also* triggered Size > OI when it printed. So either way, the new positioning got flagged on the tape — you just might also see the close. In practice, institutional-size intraday round trips are rare; treat Size > OI as opening positioning.

> **Size > OI = an institution is opening a single position larger than every other open position on this contract combined. Almost always worth investigating.**

This is a much rarer event than Volume > OI. Many contracts will have V/OI > 1 in any given session — it just takes enough cumulative activity. But Size > OI requires a single print large enough to dominate the entire open-interest picture. When it fires, it's a signal worth pausing for.

💡Core Idea

A single Size > OI print also necessarily makes Volume > OI true (one print's Size becomes part of that contract's daily Volume). So in the Flowseeker rendering, Size > OI takes priority — its color overrides Volume > OI's color when both conditions are true. You'll never see a row where both rules' colors compete.

## The Two Highlighting Rules in Practice

Putting it together, Flow Highlighting evaluates each row in the feed against three states and applies one color:

| Condition | Default Color | What the color is telling you |
| --- | --- | --- |
| **Size > OI** | Yellow | A single print on this row is bigger than yesterday's OI. Opening positioning, almost certainly. Loud. |
| **Volume > OI** (and Size ≤ OI) | Purple | Today's cumulative volume on this contract has crossed yesterday's OI. New positioning is happening on this contract; this specific print may or may not be one of the opens. Medium-loud. |
| Neither | White (default) | Routine flow on this contract. No special signal. |

These colors are the defaults; you can change any of them.

## Setting It Up

Flow Highlighting lives in the **Columns panel** in the Live Feed sidebar — not in the main filter sidebar where most filters live. Open the Columns panel (the **Columns** button in the header) and scroll to the bottom. You'll see a **Flow Highlighting** button. Click it.

A modal opens with:

* A **master toggle** at the top — turns the entire feature on or off for the current tab. When on, the button in the Columns panel changes to *"Flow Highlighting — ON"* in purple.
* **Three color pickers**, one per rule: Default, Volume > OI, Size > OI. Each opens a standard color picker; pick whatever you want.
* A **Reset Colors** button at the bottom that puts everything back to the white / purple / yellow defaults but preserves the on/off state.

Two important properties of the configuration:

* **Per-tab.** Each Live Feed tab has its own Flow Highlighting configuration. Turning it on for one tab doesn't affect any other tab. Color choices are per-tab too.
* **Persisted.** Your settings stick across sessions — close the browser, come back tomorrow, your colors are still there.

## Picking Colors That Actually Help

The defaults are reasonable, but the *hierarchy* matters more than the specific colors. The goal is that when you scroll the feed, the prints worth investigating should pop visually without you reading any column values. That requires deliberate contrast between the three states.

A workable approach:

* **Size > OI**: the loudest color you've got. Yellow on dark mode is the default for a reason — it has the highest visual weight against most backgrounds. On light mode, consider orange or a saturated red.
* **Volume > OI**: medium-loud. Purple, magenta, or saturated blue work well — clearly distinct from the Size > OI color, but quieter so the truly significant prints still pop more.
* **Default**: as quiet as you can stand. White or off-white on dark; black or dark gray on light. Don't waste visual budget on routine prints — they're the majority of the feed.

If everything looks loud, nothing looks loud. The point of the default color being quiet is to make the highlighted rows stand out by *contrast*, not by being colorful in absolute terms.

🧠TL;DR

A useful test: scroll your feed for 30 seconds with Flow Highlighting on. If your eye is constantly being pulled to highlighted rows, your colors are working. If your eye drifts evenly across the feed and you have to consciously look for highlights, your default color is too loud or your highlighted colors are too muted. Adjust until the highlights pull your attention.

## Per-Tab Strategy

Because Flow Highlighting is per-tab, you can use different configurations on different tabs depending on what each one is for. A few patterns worth considering:

* **Broad watching tab** (light filtering, wide ticker scope): Flow Highlighting on at full intensity. Both rules doing real triage work for you. This is where the feature pays off most — the feed has a lot of routine flow, and the highlights surface the prints worth looking at.
* **Tightly focused tab** (single ticker or sector, high premium minimum, sweeps only): Highlighting matters less here. Your filters have already done most of the triage, so most rows are noteworthy. You might still keep Size > OI on (the loudest signal) but turn off Volume > OI to reduce visual noise.
* **Tab for a specific name you're watching closely**: keep Size > OI on with a particularly loud color. When something institutional-scale prints in your watched name, you want it impossible to miss.

The point is that the feature is configured to a specific *use case*, not turned on globally and forgotten about. Different tabs serve different purposes; their highlighting should match.

## What to Do When a Highlight Fires

Practical workflow, once a row lights up:

1. **Read the row first.** Premium, Side, DTE, Strike. The basics. Does this print look interesting on its face?
2. **Click the row to open the chart modal.** The chart modal has the analytical depth — Net Premium for context, Strike Distribution for concentration, the contract's own history. Walk it through the [investigation workflow](https://www.skylit.ai/learn/analyzing-print-chart-modal) we covered separately.
3. **Cross-check Heatseeker** for dealer positioning at the strike where the print landed. A Size > OI print at a –GEX zone is structurally very different from the same print at a +GEX wall.

Highlighted ≠ tradeable. The highlight is a *triage signal* — it earns the print a closer look, not an automatic decision. Most highlighted prints, run through the full investigation, will tell you to skip. The few that survive are the ones worth acting on.

See this in Flowseeker

Flow Highlighting is one of Flowseeker's most underused power features — automated visual triage that surfaces opening institutional positioning at a glance, configurable per-tab to match how you read the tape.

[Try Flowseeker](https://app.skylit.ai/flow/live?utm_source=skylit_landing&utm_medium=website&sl_relay=1)

For the column-level explanation of Size, Volume, and OI (and related columns like ΔOI and V/OI), see the [Introduction to Flowseeker](https://www.skylit.ai/learn/intro-to-flowseeker) column reference. For the full investigation workflow on a highlighted print, see [Analyzing a Print with the Chart Modal](https://www.skylit.ai/learn/analyzing-print-chart-modal). For why dealer positioning at a strike determines whether a print's positioning gets amplified or absorbed, see [Dealer Positioning](https://www.skylit.ai/learn/dealer-positioning).

## Frequently Asked Questions

### What happens when a row triggers both Size > OI and Volume > OI?

Size > OI's color wins. The two rules aren't independent: any single trade with Size > OI also makes that contract's daily Volume > OI by definition (one print's Size becomes part of the day's cumulative Volume). Flowseeker's rendering checks Size > OI first, so you'll only ever see the louder signal's color. You won't see rows where both colors compete.

### Why is the default color white when I'm on dark mode?

The defaults (white, purple, yellow) are reasonable starting points, not requirements. White-on-dark works well as a quiet baseline — it sits comfortably as "nothing special" while letting the highlighted colors stand out. If you'd prefer a different baseline (off-white, light gray, an entirely different color), the Default picker is fully configurable. Pick whatever lets the highlighted rows pop the most against your usual background.

### Will my Flow Highlighting settings persist across sessions and tabs?

Yes — settings are saved per-tab and across browser sessions. Configure Flow Highlighting once on each tab, close the browser, come back tomorrow, and your settings are exactly as you left them. Each tab maintains its own configuration independently; turning it on for one tab doesn't affect any other tab.

### Why does every print on a brand-new strike get the Size > OI color?

When a strike has no prior open interest (OI = 0 — typically a strike that just opened up after a price move, or a 0DTE that opened today), every trade satisfies Size > OI by definition (any positive Size exceeds zero). So every print on that strike will fire the loudest highlight. This is technically correct — every print on a brand-new strike *is* opening positioning, since there were no positions to close. But it can briefly flood the feed with the loudest color until OI starts accumulating. Worth knowing so you don't think the feature is broken when you see a fresh strike light up uniformly.

### Can I use Flow Highlighting in the Flow Scanner too?

No — Flow Highlighting is a Live Feed feature only. The Flow Scanner has its own analytical layer (the per-contract aggregations and OI Growth signal in the filter sidebar), but the visual color-coding rules of Flow Highlighting don't carry over. If you want similar surfacing on the Scanner, you'd use its sort and filter controls instead.

### Start Trading Smarter

See these concepts in action with Skylit's dealer exposure tools.

[Get access](https://www.skylit.ai/#pricing)[Try Heatseeker](https://www.skylit.ai/#pricing)
