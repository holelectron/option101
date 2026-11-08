<!-- Source: https://www.skylit.ai/learn/tempest-volatility-accuracy -->

# How accurate is Tempest? Two years of volatility readings, checked

# How accurate is Tempest? Two years of volatility readings, checked

tools·10 min read

tempestvolatilityimplied-volatilityresearch

**We checked two years of Skylit Tempest's volatility readings against what stocks actually did next.** On ordinary (non-earnings) days from July 2024 to September 2026, about 3 in 4 next-day closes landed inside Tempest's ±1σ expected move and about 96 in 100 inside ±2σ, across 313 liquid US stocks and ETFs. Tempest's 30-day implied volatility, SVX30, tracked the next month's realized volatility far more closely than trailing volatility did. Extreme readings tended to revert, and implied volatility usually ran above the volatility that followed. Every result held on a later period and on 2,400+ additional names. All of it is about the *size* of moves, not their direction.

This note sets out what we measured, how, and where the limits are.

## Summary of findings

Each result below held in all three samples described in [the data](https://www.skylit.ai#the-data).

| Question | Result |
| --- | --- |
| Does the expected-move cone contain next-day closes as often as it should? | 74–77% inside ±1σ and about 96% inside ±2σ on 313 names (about 74% and 95% on 2,400+ other names). Slightly conservative at 1σ, on target at 2σ |
| Are the tails honest? | Moves beyond 3× the expected move were about 3× as frequent as normal math implies |
| Does SVX30 anticipate next month's volatility better than trailing volatility? | Within-stock correlation of about 0.34–0.41, against about 0.0–0.14 for trailing 20-day realized volatility |
| Do extreme readings revert? | Top-10% readings were lower 20 sessions later about 80% of the time (typical day: 50–58%). Bottom-10% readings were higher about 70–80% of the time. Much of the top-10% effect is earnings |
| Does implied usually exceed what follows? | Implied was above next-month realized 60–64% of the time, with a median gap of 2.5–3.6 vol points |

## The data

**Tempest readings.** Tempest reads each stock's options and records its readings at every close: SVX (the Skylit Volatility Index, stated as a yearly percentage), the expected move in dollars and percent, and where SVX sits in the stock's own past-year range. Readings are stored point-in-time: each one uses only what was known at that close, so it can be checked against what happened later. For dates before Tempest launched, readings were computed the same way from the option quotes available on each date.

**Outcomes.** What stocks actually did comes from exchange closing prices on the regular NYSE trading calendar. Realized volatility is measured from those closes.

**Samples.** Three sets of data, each checked separately:

| Sample | Names | Dates | Role |
| --- | --- | --- | --- |
| Earlier period | 313 liquid US stocks and ETFs | Jul 2024–Nov 2025 | Where each pattern was first found |
| Later period | The same 313 names | Nov 2025–Sep 2026 | Confirmation on later dates |
| Additional names | 2,400+ other US-listed names | Dec 2025–Sep 2026 | Confirmation on names never used to find a pattern |

Only clean readings count: names with enough actively quoted options to give a reliable reading. Days where a company reported earnings are left out of the cone results below. Moves around reports behave differently and are measured separately.

## 1. Does the expected-move cone hold?

Tempest's expected move is a 1σ (one standard deviation) move: the range options are pricing for a stock by the next close. A textbook normal distribution puts about 68% of outcomes inside ±1σ and about 95% inside ±2σ. A well-calibrated cone should land near those shares; far more closes inside would mean the cone is too wide, and far fewer would mean it is too narrow.

Share of next-day closes inside Tempest's expected move

Non-earnings days. Whiskers show the 95% confidence range; the dashed line is what a normal distribution implies.

Inside ±1σ0%25%50%75%100%76.5%313 names'24–'2574.2%313 names'25–'2673.9%2,400+ names'25–'26Normal68.27%Inside ±2σ0%25%50%75%100%96.0%313 names'24–'2595.9%313 names'25–'2695.3%2,400+ names'25–'26Normal95.45%

Non-earnings days. 313 names: 88,490 name-days (Jul 2024–Nov 2025) and 61,303 (Nov 2025–Sep 2026). 2,400+ names: 245,745 name-days (Dec 2025–Sep 2026).

* **At ±1σ, the cone ran slightly wide.** 74–77% of next-day closes landed inside it on the 313 names, and about 74% on the 2,400+ other names, against about 68% for a normal distribution. Part of that is the shape of daily moves: most days are quieter than a bell curve implies and a few are far larger, which puts more closes inside ±1σ even when the expected move is sized right overall. Part is consistent with options carrying a premium over the moves that follow (see [section 5](https://www.skylit.ai#5-implied-vs-realized)).
* **At ±2σ, it was on target.** About 96% landed inside on the 313 names and about 95% on the other names, in line with the normal distribution's 95%.

In plain terms: Tempest's ±1σ band is a slightly conservative yardstick, and its ±2σ band has contained closes about as often as the textbook says it should.

| Sample | Inside ±1σ (95% range) | Inside ±2σ (95% range) | Name-days |
| --- | --- | --- | --- |
| 313 names, Jul 2024–Nov 2025 | 76.5% (74.9–78.0%) | 96.0% (95.2–96.6%) | 88,490 |
| 313 names, Nov 2025–Sep 2026 | 74.2% (72.6–75.8%) | 95.9% (95.2–96.4%) | 61,303 |
| 2,400+ names, Dec 2025–Sep 2026 | 73.9% (72.2–75.8%) | 95.3% (94.7–95.8%) | 245,745 |

## 2. Are the tails honest?

A cone can look right in the middle and still understate the extremes. Real stocks have more very large days than a bell curve implies, and a reading that pretends otherwise is the dangerous kind.

Share of name-days that moved more than 3× the expected move

Non-earnings days. Whiskers show the 95% confidence range; the dashed line is what a normal distribution implies.

0.0%0.4%0.8%1.2%0.9%313 namesJul '24–Nov '250.7%313 namesNov '25–Sep '260.9%2,400+ namesDec '25–Sep '26Normal0.27%

Non-earnings days, same samples as above. Whiskers show 95% confidence ranges.

Moves beyond 3× the expected move happened on 0.7–0.9% of name-days, about 1 in 110 to 1 in 140, against 0.27% for a normal distribution. That is **about 3× as often as normal math implies**. Tempest's expected move describes a typical day well; it does not make the rare, very large day disappear, and it should not be read as a ceiling.

## 3. Does SVX30 anticipate next month's volatility?

A common shortcut for "how much will this stock move next month" is to look at how much it moved last month. We compared that shortcut, trailing 20-day realized volatility, with Tempest's SVX30 as guides to the realized volatility over the following 21 trading days.

We measured this **within each stock**: for each name, we asked whether its readings rose and fell with its own later volatility. That removes the obvious fact that some stocks are always more volatile than others, which would flatter any measure.

How closely each reading tracked the next month's realized volatility

Within-stock correlation; higher is closer. It measures the size of moves, not their direction.

* Tempest SVX30 (30-day implied)
* Trailing 20-day realized

0.00.20.40.410.14313 namesJul '24–Nov '250.400.01313 namesNov '25–Sep '260.34−0.022,400+ namesDec '25–Sep '26

Within-stock correlation between each reading and realized volatility over the next 21 trading days. Higher means the reading tracked later volatility more closely.

* **SVX30 tracked the next month's realized volatility far more closely.** Its within-stock correlation was about 0.34–0.41 in all three samples; trailing 20-day volatility's was about 0.0–0.14.
* **SVX30 was also the closer of the two about 60% of the time**, measured day by day.

Two caveats matter here:

* **This is about volatility, not direction.** A higher SVX30 pointed to bigger moves in either direction. It says nothing about whether the stock went up or down.
* **Part of the gap comes from the earnings calendar.** Options know when a company reports; trailing volatility does not. With earnings windows removed, SVX30 was still the closer of the two 53–57% of the time, a smaller but consistent margin. Its within-stock correlation stayed well ahead of trailing volatility's on the later period and the 2,400+ names, but the two were close on the earlier period.

## 4. Do extreme readings revert?

Tempest ranks each stock's SVX30 against up to its own past year (at least 60 sessions), as a percentile. For the 2,400+ additional names, whose history starts in December 2025, that is a shorter window, so their results cover March–September 2026. We grouped readings into ten bands, from the lowest 10% of a stock's own range to the highest, and asked how often SVX30 was lower 20 trading days later.

Share of days 30-day IV was lower 20 sessions later

By where SVX30 sat in the stock's own past-year range, in ten bands from lowest to highest. The dashed line is the share across all days.

* Bottom and top 10%
* Middle bands

313 names · Jul '24–Nov '250%50%100%18%86%All days 49%LowestHighest313 names · Nov '25–Sep '2623%79%All days 50%LowestHighest2,400+ names · Dec '25–Sep '2632%80%All days 58%LowestHighest

Each panel is one sample. Bars run from the lowest 10% of a stock's own past-year range (left) to the highest 10% (right).

* **Top-10% readings were lower 20 sessions later about 80% of the time** (79–86% across the samples), against 50–58% on a typical day.
* **Bottom-10% readings were higher 20 sessions later about 70–80% of the time** (69–82%).
* The pattern is gradual rather than a cliff: the higher the band, the more often IV was lower a month on.
* **Much of the top-10% effect is earnings.** About two-thirds of top-10% readings on the 313 names came shortly before an earnings report, and implied volatility usually falls once the report is out. Without a report in the following month, top-10% readings were lower 20 sessions later about 50–65% of the time: still more often than similar days (about 30–45%), but well short of 80%.

This describes **implied volatility itself**. It does not mean options at a top-10% reading were mispriced, or that the stock moved less than priced. High implied volatility tended to ease; whether the premium was worth selling is a separate question this study does not answer.

## 5. Implied vs realized

Across the samples, **implied volatility (SVX30) was above the realized volatility of the next month 60–64% of the time**, with a **median gap of 2.5–3.6 vol points** (the difference between two yearly volatility readings; SVX 32 against 30 is a 2-point gap).

| Sample | Implied above next-month realized | Median gap |
| --- | --- | --- |
| 313 names, Jul 2024–Nov 2025 | 64% | +3.6 vol points |
| 313 names, Nov 2025–Sep 2026 | 64% | +3.3 vol points |
| 2,400+ names, Dec 2025–Sep 2026 | 60% | +2.5 vol points |

We quote the median and the typical share on purpose. The *average* gap is not reliable: a few months of sudden, large moves, when realized volatility far exceeds what was priced, swing it enough that it is not statistically distinguishable from zero. On a typical month, options priced a little more movement than stocks delivered. In the occasional shock month, they priced far less.

This is consistent with the ±1σ cone running slightly wide in [section 1](https://www.skylit.ai#1-does-the-expected-move-cone-hold).

## How we tested it

The goal was to find out what holds up, not to find something to say. The method was set to make chance findings unlikely to survive.

* **Weekend-adjusted SVX30.** The implied-against-realized and percentile results use Tempest's weekend-adjusted SVX30 reading.
* **Point-in-time only.** Every test uses readings exactly as they stood at a close and outcomes from the following sessions only. A reading at Monday's close is judged on Tuesday onward, never on Monday.
* **Exchange closing prices.** Outcomes are measured on regular-session closing prices, on the NYSE trading calendar.
* **Found once, confirmed twice.** Each idea was first tested on the earlier period. It only counted if it passed there after adjusting for the number of ideas tested at once, and then held in the same direction, at conventional statistical significance, on *both* the later period and the 2,400+ additional names.
* **Honest confidence ranges.** Ranges come from resampling whole blocks of trading days rather than single name-days, because stocks move together: one volatile week across 300 names is one week of evidence, not 300 independent observations.
* **Everything we tried is counted.** We ran 75 tests in all, on the cone and its tails, implied against realized volatility, SVX30 against trailing volatility, percentile reversion, term structure, skew, the call and put premium balance, large moves, quiet "coiled" stretches, earnings reactions, and how implied volatility moves with price.

⚠️Warning

Nothing here measures trading results. This study did not test buying or selling options, so it says nothing about profit or loss, and none of these readings is a signal to trade.

## Limits of this study

* **About two years of history.** That is roughly 25 independent 21-day windows, enough to see consistent patterns, not enough to rule out a very different market regime.
* **Overlapping dates.** The later period and the additional names cover similar calendar dates, so they are not independent in time.
* **Survivors.** The 313 names were fixed when the history was built, so companies that were later delisted are missing. That likely makes the tails look slightly *better* than they were.
* **Earnings days are excluded** from the cone results.
* **Descriptive, not a guarantee.** These are measurements of the past. We plan to re-run them as more history accumulates and to publish updates here.

## How to use this when you read Tempest

* **Treat the ±1σ expected move as a slightly conservative yardstick** for a typical day, and the ±2σ band as the range that has held about 95% of the time.
* **Never treat the cone as a ceiling.** Moves beyond 3× the expected move have happened about 3× as often as textbook math says.
* **Read SVX30 as the market's estimate of how much a stock will move,** not which way. Check for a scheduled event before reading a high SVX as unusual.
* **Expect extremes to ease,** but remember that describes implied volatility, not whether options were mispriced.

See how each reading works in the [Tempest field guide](https://www.skylit.ai/docs/guides/tempest), or read more about Tempest on its [product page](https://www.skylit.ai/modules/tempest). For the Greek behind implied volatility, see [Vega](https://www.skylit.ai/learn/vega).

*Historical, descriptive statistics from Skylit Tempest readings and exchange closing prices. Past behavior does not guarantee future results. Not investment advice.* Research by Skylit, Inc. Tempest is available to Skylit Pro members.

## Frequently asked questions

### How accurate is Skylit Tempest's expected move?

On non-earnings days from July 2024 to September 2026, 74–77% of next-day closes landed inside Tempest's ±1σ expected move and about 96% inside ±2σ, across 313 liquid US stocks and ETFs. On 2,400+ additional names (December 2025 to September 2026) the figures were about 74% and 95%. A normal distribution would put about 68% inside ±1σ and 95% inside ±2σ, so the cone was slightly conservative at 1σ and on target at 2σ.

### Does Tempest predict which way a stock will move?

No. Tempest measures how much movement options are pricing, not direction. In this study, none of its readings showed a reliable edge on price direction.

### Is SVX30 a better guide to next month's volatility than recent volatility?

In this study, yes. Within each stock, SVX30's correlation with the next month's realized volatility was about 0.34–0.41, against about 0.0–0.14 for trailing 20-day realized volatility. Part of that comes from options knowing the earnings calendar, and it is about the size of moves, not their direction.

### Do options usually price more movement than stocks deliver?

Usually, by a little. Tempest's 30-day implied volatility was above the next month's realized volatility 60–64% of the time, with a median gap of 2.5–3.6 vol points. The average gap is not reliable, because occasional shock months, when stocks move far more than priced, swing it.

### Why are earnings days excluded?

Price moves around earnings reports behave differently from ordinary days, so they are measured separately. The cone results in this note cover non-earnings days only.

### Can I check Tempest's accuracy myself?

Every Tempest reading is stored point-in-time, so its accuracy can be checked against what happened afterwards. In the app, the expected-move cones on Atlas can be replayed and pinned to see how a past cone played out.

### Start Trading Smarter

See these concepts in action with Skylit's dealer exposure tools.

[Get access](https://www.skylit.ai/#pricing)[Try Heatseeker](https://www.skylit.ai/#pricing)
