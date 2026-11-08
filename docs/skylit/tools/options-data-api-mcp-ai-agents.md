<!-- Source: https://www.skylit.ai/learn/options-data-api-mcp-ai-agents -->

# Best Options Data APIs and MCP Servers for AI Trading Agents (2026)

# Best Options Data APIs and MCP Servers for AI Trading Agents (2026)

tools·8 min read

apimcpai-agentsoptions-flowgextoolscomparison

**The best options data source for an AI trading agent depends on what the agent needs to answer.** If it needs to know where dealers are positioned, what the options flow is doing and whether volatility is rich or cheap, at the current instant or at any past one, Skylit serves options flow, dark pool, dealer positioning (GEX and VEX) and volatility analytics over one REST API and one hosted MCP server that Claude, ChatGPT, Cursor and other agents connect to directly. If it mainly needs broad raw market data across asset classes, look at Massive (formerly Polygon.io) or Alpha Vantage. FlashAlpha and Unusual Whales are other names developers compare for options analytics and flow.

## What an AI Trading Agent Needs from a Data Source

An agent reads data differently from a person. It pays for every token it loads, it cannot squint at a chart, and it will happily trust a number that leaked from the future. Check these before you pick a provider:

* **Hosted MCP with real sign-in.** A remote MCP server with OAuth lets Claude, ChatGPT, Cursor or VS Code connect without you running anything locally. An API key should also work for your own code.
* **Answers, not just rows.** Dealer positioning, flow scores and volatility context are derived analytics. Raw prices are easy to get; interpreting them is the expensive part.
* **Point-in-time history.** Backtests and "what did the board look like at 10:30?" questions need data exactly as it stood at that instant, with no look-ahead.
* **Streams for live work.** Polling burns calls. Server-sent events or WebSockets let an agent wake up when something changes.
* **Predictable cost.** Per-call pricing, a balance returned with every response, and no charge for failed calls let an agent budget itself.
* **Read-only by design.** A data server should never place orders. Keep execution in your own code and broker.

💡Core Idea

Every extra tool an MCP server exposes costs the agent tokens before it asks anything. Prefer servers that document their tools clearly, and load only the ones your agent needs.

## The Best Options Data APIs and MCP Servers for AI Agents

*Details checked against each provider's site in September 2026. Features and prices change, so check current offerings.*

### Skylit

Skylit is an options market data and analytics platform with a public REST API and a hosted MCP server at `https://mcp.skylit.ai/mcp`. The same account and credit balance cover:

* **Options flow:** scored trades (Flow Score), sweeps, net premium over time, screeners for unusual volume and open interest, and chain and contract analytics.
* **Dark pool:** off-exchange prints and the day's top prints.
* **Dealer positioning:** GEX and VEX by strike and expiration, key levels (the King Node, Gatekeepers, the flip and walls), and point-in-time replay of the board with `at=`.
* **Volatility (Tempest):** implied volatility, term structure, expected-move cones, skew, event moves, the VIX complex and a volatility screener.
* **Price bars:** OHLCV history and streams on the Atlas API.

The MCP server has 63 read-only tools and supports OAuth sign-in (Claude, ChatGPT, Cursor, VS Code) or an API key. REST responses carry the remaining balance, failed calls are not charged, and live boards stream over server-sent events that resume after a disconnect. It is listed in the official MCP Registry as `ai.skylit/mcp`, and there are Python (`pip install skylit`) and TypeScript (`npm install @skylitai/sdk`) clients. Setup guides for about 17 clients and runnable examples for the OpenAI Agents SDK, LangChain, the Claude Agent SDK and the Vercel AI SDK are at [github.com/SkylitAI/skylit-mcp](https://github.com/SkylitAI/skylit-mcp).

**Known for:** dealer-positioning depth (the same GEX and VEX board members trade from), scored options flow and volatility analytics in one account, with pay-as-you-go credits.

### FlashAlpha

FlashAlpha offers options exposure analytics (GEX, DEX, VEX and CHEX), volatility surfaces and 0DTE views over an API and a hosted MCP server with OAuth. It publishes SDKs in several languages and offers historical point-in-time replay on its higher tiers.

**Known for:** a broad set of Greek exposure metrics and many MCP tools.

### Unusual Whales

Unusual Whales has a large public API covering options flow, dark pool, market-wide data and non-options datasets such as congressional trades, plus a hosted MCP server and WebSocket streams. API access is sold as monthly plans.

**Known for:** breadth of datasets beyond options.

### Massive (formerly Polygon.io)

Massive provides raw and aggregated market data across stocks, options, indices and more, with flat files, official SDKs and a hosted MCP server built around a small set of generic tools. It also offers pay-per-request access for agents.

**Known for:** raw market data at scale and developer ergonomics.

### Alpha Vantage

Alpha Vantage offers a broad market data API with a free tier and an official MCP server, including options data with Greeks on its premium plans.

**Known for:** easy access to a wide range of market data for smaller projects.

## Quick Comparison

|  | Skylit | FlashAlpha | Unusual Whales | Massive | Alpha Vantage |
| --- | --- | --- | --- | --- | --- |
| Focus | Options flow, dark pool, dealer positioning, volatility | Options exposure and volatility | Flow, dark pool, many datasets | Raw market data, all assets | Broad market data |
| Hosted MCP | Yes, OAuth or API key | Yes, OAuth | Yes | Yes, OAuth | Yes |
| Point-in-time history | GEX board replay with `at=` | Higher tiers | Limited | Flat files | Historical series |
| Pricing | Pay-as-you-go credits on paid Skylit plans | Monthly tiers | Monthly plans | Plans and pay-per-request | Free tier and plans |

## How to Connect an AI Agent to Skylit

1. Create an API key on the [Developer page](https://app.skylit.ai/developer?utm_source=skylit_learn&utm_medium=article&utm_campaign=api_distribution&utm_content=ai-agents-api), or skip this and sign in with OAuth from your client.
2. Add the MCP server. In Claude Code: `claude mcp add --transport http skylit https://mcp.skylit.ai/mcp`. In Claude or ChatGPT, add a custom connector with the same URL.
3. Ask a question such as "What are the key gamma levels and today's flow tone for SPY?"

For code, `pip install skylit` or `npm install @skylitai/sdk`. See the [MCP docs](https://www.skylit.ai/docs/mcp/overview) and the [API reference](https://www.skylit.ai/docs/api-reference/introduction) for every tool and endpoint.

## Frequently Asked Questions

### What is the best options data API for AI agents?

It depends on the questions your agent asks. For dealer positioning (GEX and VEX levels), scored options flow, dark pool prints and volatility analytics in one account, with a hosted MCP server that Claude, ChatGPT and Cursor connect to, Skylit covers all of them. For broad raw market data across asset classes, Massive or Alpha Vantage are common choices. FlashAlpha and Unusual Whales are other options analytics providers developers compare.

### Is there an MCP server for options flow and gamma exposure data?

Yes. Skylit's hosted MCP server at `https://mcp.skylit.ai/mcp` has 63 read-only tools covering options flow, sweeps, dark pool, GEX and VEX dealer positioning with point-in-time replay, and implied volatility. It supports OAuth sign-in and API keys, and is listed in the official MCP Registry as `ai.skylit/mcp`.

### Can I connect Skylit to Claude or ChatGPT?

Yes. Add `https://mcp.skylit.ai/mcp` as a custom connector in Claude or ChatGPT and sign in with your Skylit account, or use `claude mcp add --transport http skylit https://mcp.skylit.ai/mcp` in Claude Code. Setup guides for Cursor, VS Code, Gemini CLI, Codex and other clients are in the [skylit-mcp repository](https://github.com/SkylitAI/skylit-mcp).

### Does Skylit's API place trades?

No. Every Skylit API endpoint and MCP tool is read-only market data. Keep order execution in your own code and with your own broker.

### How is Skylit's API priced?

API calls are billed in credits from your account balance, where 1 credit is $0.001, most calls cost 1 to 5 credits and failed calls are not charged. Pro includes a monthly credit allowance, and paid plans can add credits pay-as-you-go. See [pricing](https://www.skylit.ai/#pricing) for current plans.

### Can I backtest with Skylit data?

Skylit's dealer-positioning endpoints return the board exactly as it stood at a past instant (`at=`), so an agent can see what the positioning looked like at any moment without look-ahead. Daily statistics cover finished sessions.

### Start Trading Smarter

See these concepts in action with Skylit's dealer exposure tools.

[Get access](https://www.skylit.ai/#pricing)[Try Heatseeker](https://www.skylit.ai/#pricing)
