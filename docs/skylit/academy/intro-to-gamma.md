<!-- Source: https://www.skylit.ai/learn/intro-to-gamma -->

# Intro to Gamma: Pika Nodes, Barney Nodes, and the Absolute Value Rule

# Intro to Gamma: Pika Nodes, Barney Nodes, and the Absolute Value Rule

academy·10 min read

gammagexheatseekerdealer-positioning

## Dealers Can't Take Sides

Market makers don't speculate. Their job is to be the other side of whatever trade you want to do, collect the spread, and hedge away the risk they just took on. They don't care which direction the market goes. They care about staying neutral.

When a dealer sells you a call option, they're now short that call. If the underlying rallies, the call gains value and the dealer loses. To offset that, they buy shares of the underlying. Now if the underlying rallies, their long stock position makes money to offset the short call loss. They're neutral. They've hedged.

This hedging isn't optional and it doesn't stop. Every time the underlying moves, the delta of those options changes, and the dealer has to adjust their hedge. This continuous, mechanical rebalancing is what drives the structural effects you see on a chart. Understanding whether that hedging is working for you or against you starts with understanding gamma.

## Positive Gamma: The Friction Layer

When dealers are **net long gamma**, shown as yellow Pika nodes on Heatseeker, their hedging works against the market's direction. This is counterintuitive at first, but the mechanics are straightforward.

Say customers are short puts. Dealers, as the counterparty, are long those puts, which means they're long gamma on the put side. As price falls toward those puts, the dealer's delta exposure grows. To stay neutral, they have to buy stock. They're buying into weakness. That buying slows the decline, creates support, and pushes price back up.

Same thing happens on the upside. If price rallies away from those put strikes, the puts go further out of the money, delta shrinks, and the dealer needs to sell stock to rebalance. They're selling into strength. That selling creates resistance and slows the rally.

Positive gamma environments mean dealers are constantly acting as a counter-force to whatever the market is doing. They buy dips. They sell rips. The result is that price tends to mean-revert, volatility gets suppressed, and the market chops around in a range. If you've ever watched a stock just grind sideways for days and couldn't figure out why it wouldn't move, positive gamma pinning near that level is often the answer.

🎯ELI5

Positive gamma is friction. Like a car's brake pads, it doesn't stop movement entirely, but it resists it. Every push in one direction gets pushed back against by dealer hedging. The harder the market tries to move, the more hedge pressure builds in the opposite direction. That's why +GEX environments feel sticky and slow.

## Negative Gamma: The Accelerant

When dealers are **net short gamma**, shown as purple Barney nodes on Heatseeker, their hedging runs with the market's direction. The mechanics flip completely.

Say dealers have sold calls to customers. They're short those calls, which means they're short gamma. As price rises toward those call strikes, the calls go more in the money. The dealer's short call exposure grows. To stay neutral, they have to buy more stock. They're buying into strength. That buying adds momentum to the rally.

When price falls away from those strikes, the calls go out of the money, delta shrinks, and the dealer has to sell stock to rebalance. They're selling into weakness. That selling adds fuel to the decline.

In negative gamma territory, dealer hedging is pro-cyclical. Rising prices force dealers to buy, which pushes prices higher, which forces dealers to buy more. Falling prices force dealers to sell, which pushes prices lower, which forces dealers to sell more. Every move begets a larger move. Volatility accelerates. Price overshoots. You get air pockets, fast directional moves that look like nothing's slowing them down, because mechanically, nothing is.

🎯ELI5

Negative gamma is fuel. Same car, but now instead of brakes, you've got nitrous. Every small price move triggers dealer hedging that amplifies the move further. The market doesn't just move, it runs. If you've seen a stock gap through a "support level" like it wasn't there, you were probably watching price move through a negative gamma zone with no friction to slow it down.

## The Core Pattern

| Condition | Dealer Hedge | Market Behavior |
| --- | --- | --- |
| **+GEX (Positive Gamma)** | Buys dips, sells rips | Volatility dampening, mean reversion, range, chop |
| **-GEX (Negative Gamma)** | Buys rallies, sells declines | Volatility amplification, acceleration, overshoots |

Interactive visuals and video walkthroughs available in Skylit Academy

Get access to annotated chart examples, live Heatseeker map screenshots, and step-by-step video breakdowns with a Skylit Initiate subscription or above.

[Explore Skylit Academy](https://www.skylit.ai/#pricing)

This is the foundation. Positive gamma creates friction. Negative gamma creates fuel. Every structural effect you'll learn about in [gamma exposure](https://www.skylit.ai/learn/gamma-exposure) and [reading Heatseeker](https://www.skylit.ai/learn/reading-heatseeker) traces back to this mechanic.

## The Absolute Value Rule

Here's a rule that trips up a lot of traders early on: when it comes to structural influence, **magnitude matters more than color**.

A yellow Pika node with $2 billion in exposure has more structural weight than a purple Barney node with $200 million. Yes, they have opposite effects, but the larger node is going to dominate. Its hedging flows are an order of magnitude larger. Price is going to feel that $2B node hard.

💡Core Idea

The Absolute Value Rule: size determines influence, regardless of sign. When you're looking at the heatmap, don't filter by color first. Look at the largest nodes across the whole structure, then assess whether they're positive or negative. A massive positive gamma node sitting at your level is structurally more important than a small negative node nearby, even though they have opposite mechanical effects. The bigger node wins.

This matters practically when you're reading the heatmap. You might see a negative gamma zone between two massive positive gamma nodes. The negative zone might look like fuel for a breakout. But if those flanking positive nodes are 10x the size of the negative cluster, the friction from those nodes is going to overpower the fuel. Price is likely to stall at the positive node below and the positive node above, not blast through both of them.

The heatmap is a map of forces. You need to assess the magnitude of each force, not just its direction.

## Why This Shows Up on Charts

None of this is abstract. It shows up directly in price action, which is exactly why the [charts-first](https://www.skylit.ai/learn/charts-first) workflow exists. The structural effects of gamma manifest as identifiable patterns on the chart.

In positive gamma zones, you see tight ranges, frequent retests of the same levels, low volatility days where the range is 0.3% and price just drifts. The dealer buying dips and selling rips creates visible support and resistance at the exposure levels. If you know where the big positive gamma nodes are, you can often predict the boundaries of the coming range before it forms.

In negative gamma zones, you see explosive moves, failed breakouts that accelerate instead of reverting, gaps through levels that should have held. When price enters a negative gamma cluster, the dealer hedging amplifies whatever momentum is already present. A 1% move becomes 2%, and a 2% move becomes 4%.

The transition between the two regimes is where some of the most tradeable setups occur. When price crosses from a large positive gamma zone into negative gamma territory, the dynamics shift instantly. The friction disappears and fuel takes over. Knowing that transition point in advance, before price gets there, gives you a significant edge on entry timing and target selection.

See this in Heatseeker

See positive and negative gamma nodes color-coded in real-time across every strike and expiration. Identify friction zones, fuel zones, and the transitions between them before price gets there.

[Try Heatseeker](https://www.skylit.ai/#pricing)

## Building on This Foundation

Gamma is the starting point. Once you understand why positive gamma creates friction and negative gamma creates fuel, everything else in dealer positioning mechanics makes more sense.

The strength of any node depends on how close spot price is to it, which direction it's approaching from, and how much of the original exposure is still live versus already hedged out. Those dynamics get covered in detail in [gamma exposure](https://www.skylit.ai/learn/gamma-exposure). The practical side of reading these levels in real-time, knowing which nodes are live and which are stale, is in [reading Heatseeker](https://www.skylit.ai/learn/reading-heatseeker).

Start here though. Get the friction-versus-fuel distinction locked in. It's the lens through which everything else in gamma mechanics gets interpreted.

## Related Reading

* [Charts First](https://www.skylit.ai/learn/charts-first): why chart structure has to come before exposure data, and how to use both together
* [Reading Heatseeker](https://www.skylit.ai/learn/reading-heatseeker): how to interpret the heatmap once you understand what gamma nodes actually represent
* [Gamma Exposure](https://www.skylit.ai/learn/gamma-exposure): the full mechanics of GEX, king nodes, and how exposure levels shift over time

## Frequently Asked Questions

### What are Pika and Barney nodes on Heatseeker?

Pika nodes are yellow and represent positive gamma exposure. Barney nodes are purple and represent negative gamma exposure. Pika nodes create friction because dealers hedge by buying dips and selling rips, which suppresses volatility and creates range-bound behavior. Barney nodes create fuel because dealers hedge pro-cyclically, buying into rallies and selling into declines, which amplifies moves in whatever direction price is already going.

### What is the Absolute Value Rule in GEX trading?

The Absolute Value Rule states that magnitude determines structural influence, regardless of whether a node is positive or negative. A yellow Pika node with $2 billion in exposure has more structural weight than a purple Barney node with $200 million, even though they have opposite mechanical effects. When reading the heatmap, you look at the largest nodes first and assess their sign second. The bigger node wins.

### What is the difference between positive and negative gamma on Heatseeker?

Positive gamma creates friction. Dealers in a positive gamma environment buy dips and sell rips, acting as a counterforce to whatever the market is doing. The result is suppressed volatility, mean reversion, and range-bound chop. Negative gamma creates fuel. Dealers in a negative gamma environment buy rallies and sell declines, amplifying momentum in the existing direction. The result is accelerating moves, volatility expansion, and overshoots past levels that would have held in a positive gamma environment.

### Start Trading Smarter

See these concepts in action with Skylit's dealer exposure tools.

[Get access](https://www.skylit.ai/#pricing)[Try Heatseeker](https://www.skylit.ai/#pricing)
