<!-- Machine translation; review against original. Source: https://www.skylit.ai/learn/options-data-api-mcp-ai-agents -->

> **번역 안내:** 이 문서는 자동 번역 초안입니다. 수치·수식·거래 판단은 [영어 원문](options-data-api-mcp-ai-agents.md)을 확인하세요.

# AI 거래 에이전트를위한 최고의 옵션 데이터 API 및 MCP 서버 (2026)

# AI 거래 에이전트를위한 최고의 옵션 데이터 API 및 MCP 서버 (2026)

도구·8 분 읽기

apimcpai-agentsoptions-flowgextoolscomparison

**AI 무역 대리인을 위한 제일 선택권 자료 근원은 대리인이 대답하는 무슨에 달려 있습니다.** 딜러가 위치하는 것을 알아야 할 경우, 옵션 흐름이 수행되고 휘발성이 부유하거나 저렴한 경우, 현재 즉시 또는 과거에, Skylit은 옵션 흐름, 어두운 풀, 딜러 포지셔닝 (GEX 및 VEX) 및 1 REST API에 대한 휘발성 분석 및 Claude, ChatGPT, Cursor 및 기타 에이전트가 직접 연결하는 MCP 서버를 호스팅합니다. 주로 자산 클래스 전반에 걸쳐 광범위한 원료 시장 데이터를 필요로한다면, Massive (이전 Polygon.io) 또는 Alpha Vantage를 살펴보십시오. FlashAlpha 및 Unusual Whales는 다른 이름 개발자가 옵션 분석 및 흐름을 비교합니다.

## AI Trading Agent가 데이터 소스에서 필요로 하는 것

에이전트는 다른 사람에서 데이터를 읽습니다. 그것은 모든 토큰에 대한 지불로드, 그것은 차트에 스쿼트 할 수 없습니다, 그리고 그것은 미래에서 누출 된 번호를 신뢰합니다. 공급자를 선택하기 전에 이러한 확인:

- **MCP를 실제 서명으로 호스팅했습니다.** OAuth와 원격 MCP 서버는 Claude, ChatGPT, Cursor 또는 VS Code를 로컬로 실행하지 않고 연결합니다. API 키는 또한 자신의 코드를 위해 작동해야합니다.
- **답변, 그냥 행하지.** Dealer 포지셔닝, 흐름 점수 및 변동 상황은 분석입니다. 익지않는 가격은 얻게 쉽습니다; 해석은 비싼 부분입니다.
- **Point-in-time 역사.** Backtests and "what did the board look like 10:30?" 질문은 정확히 그 즉시에 서 있기 때문에 데이터가 필요하지 않습니다.
- **라이브 작업을위한 스트림.** 오염 화상 통화. Server-sent 이벤트 또는 WebSockets는 에이전트가 무언가가 변경 될 때 일어나도록 합니다.
- **예상 비용.** Per-call 가격, 균형은 모든 응답으로 반환, 실패 통화에 대한 수수료는 에이전트 예산 자체를하자.
- **디자인에 의해 읽기 전용.** 데이터 서버는 주문할 수 없습니다. 자신의 코드와 브로커에서 실행을 유지.

회사소개

모든 추가 도구 MCP 서버는 모든 것을 요청하기 전에 에이전트 토큰을 노출합니다. Prefer 서버는 도구가 명확하게 문서화하고 에이전트가 필요로하는 것을로드합니다.

## AI Agents에 대한 최고의 옵션 데이터 API 및 MCP 서버

*9 월 2026의 각 공급자의 사이트에 대해 확인 된 세부 사항. 특징과 가격 변화, 그래서 현재 제안을 검사합니다.*

### 링크 메뉴

Skylit는 공공 REST API 및 호스트 MCP 서버와 함께 시장 데이터 및 분석 플랫폼입니다. `https://mcp.skylit.ai/mcp`. 동일한 계정 및 신용 균형 덮개:

- **옵션 흐름:** 점수 거래 (Flow Score), 스윕, 순 프리미엄 시간, 특이한 볼륨 및 열린 관심, 체인 및 계약 분석을위한 시나리오.
- **어두운 수영장:** 오프 교환 인쇄 및 일의 최고 인쇄.
- **Dealer 위치:** GEX 및 VEX는 파업 및 만료, 키 레벨 (킹 노드, 게이트키, 플립 및 벽) 및 보드의 포인트 인 시간 재생 `at=`.
- **휘발성 (Tempest):** 불쾌한 휘발성, 기간 구조, 예상되는 모이는 콘, 꼬치, 사건 움직임, VIX 복잡한 및 휘발성 선별기.
- **가격 막대기:** Atlas API의 OHLCV 역사와 스트림.

MCP 서버에는 63개의 읽기 전용 도구가 있고 OAuth sign-in (Claude, ChatGPT, Cursor, VS Code) 또는 API 열쇠를 지원합니다. REST 응답은 나머지 잔액을 수행, 실패 통화는 충전되지 않으며, 연결 후 재시작하는 Server-sent 이벤트를 통해 라이브 보드 스트림. 공식 MCP Registry에 나열되어 있습니다. `ai.skylit/mcp`, 그리고 파이썬이 있다 (`pip install skylit`) 및 타입 스크립트 (`npm install @skylitai/sdk`) 클라이언트. OpenAI Agents SDK, LangChain, Claude Agent SDK 및 Vercel AI SDK를 위한 17개의 클라이언트 및 실행 가능한 예제를 위한 설정 가이드 [github.com/SkylitAI/스키라이트 mcp](https://github.com/SkylitAI/skylit-mcp).

**다음을 알고:** 딜러 배치 깊이 (같은 GEX 및 VEX 보드 회원 거래에서), pay-as-you-go 신용과 하나의 계정에서 득점 옵션 흐름과 변동성 분석.

### 플래시Alpha

FlashAlpha는 API에 대한 옵션 노출 분석 (GEX, DEX, VEX 및 CHEX), 휘발성 표면 및 0DTE 전망 및 OAuth와 함께 호스팅 된 MCP 서버를 제공합니다. 그것은 여러 언어로 SDK를 게시하고 더 높은 계층에 역사적인 Point-in-time replay를 제공합니다.

**다음을 알고:** 그리스 노출 미터 및 많은 MCP 도구의 넓은 세트.

### 비정상적인 Whales

비정상적인 Whales에는 큰 공공 API 덮음 선택권 교류, 어두운 수영장, 시장 넓은 자료 및 congressional 무역과 같은 비 선택권 자료 세트, 플러스 호스팅된 MCP 서버 및 WebSocket 시내가 있습니다. API 액세스는 월간 계획으로 판매됩니다.

**다음을 알고:** 옵션보다 datasets의 빵.

### 대규모 (이전 Polygon.io)

Massive는 Stocks, options, indices 등을 통해 원가 및 집계 된 시장 데이터를 제공합니다. 플랫 파일, 공식 SDK 및 주최 된 MCP 서버는 일반적인 도구의 작은 세트를 구축했습니다. 그것은 또한 에이전트에 대 한 pay-per-request 액세스를 제공합니다.

**다음을 알고:** Scale 및 Developer ergonomics의 원료 시장 데이터.

### 알파 Vantage

Alpha Vantage는 프리미엄 요금제에서 그리스어를 사용하는 옵션 데이터를 포함한 무료 계층 및 공식 MCP 서버를 갖춘 광범위한 시장 데이터 API를 제공합니다.

**다음을 알고:** 다양한 시장 데이터에 쉽게 액세스 할 수 있습니다.

## 빠른 비교

|  | 링크 메뉴 | 플래시Alpha | 비정상적인 Whales | 뚱 베어 | 알파 Vantage |
| --- | --- | --- | --- | --- | --- |
| 주요 특징 | 옵션 흐름, 어두운 풀, 딜러 위치, 휘발성 | 옵션 노출 및 휘발성 | 교류, 어두운 수영장, 많은 datasets | 원시 시장 데이터, 모든 자산 | Broad 시장 자료 |
| MCP 호스팅 | 예, OAuth 또는 API 키 | 예, OAuth | 이름 \* | 예, OAuth | 이름 \* |
| Point-in-time 역사 | GEX 보드 재생 `at=` | 높은 층 | 가격 : | 플랫 파일 | 역사 시리즈 |
| 제품정보 | 유료 Skylit 계획에 Pay-as-you-go 크레딧 | 월간 계층 | 월간 계획 | 계획 및 지불-per-request | 무료 계층과 계획 |

## Skylit에 AI Agent를 연결하는 방법

1. API 키 만들기 [개발자 페이지](https://app.skylit.ai/developer?utm_source=skylit_learn&utm_medium=article&utm_campaign=api_distribution&utm_content=ai-agents-api), 또는이를 건너 귀하의 클라이언트에서 OAuth와 서명.
2. MCP 서버 추가. Claude 부호에서: `claude mcp add --transport http skylit https://mcp.skylit.ai/mcp`. Claude 또는 ChatGPT에서는, 동일한 URL을 가진 주문 연결관을 추가하십시오.
3. "키 감마 수준과 오늘 SPY의 흐름 톤은 무엇입니까?"와 같은 질문을합니까?

코드의 경우, `pip install skylit` 또는 `npm install @skylitai/sdk`. 참조 [MCP 문서](https://www.skylit.ai/docs/mcp/overview) 그리고 [API 참조](https://www.skylit.ai/docs/api-reference/introduction) 모든 도구 및 엔드포인트를 위해.

## 자주 묻는 질문

### AI 에이전트를위한 최고의 옵션 데이터 API는 무엇입니까?

그것은 당신의 대리인에게 질문에 달려 있습니다. 딜러 위치 (GEX 및 VEX 레벨), 득점 옵션 흐름, 어두운 풀 프린트 및 변동성 분석, 클랜드, ChatGPT 및 커서가 연결되는 호스팅 MCP 서버와 함께, Skylit은 그들 모두를 다룹니다. 자산 클래스, 대규모 또는 Alpha Vantage의 광범위한 원시 시장 데이터는 일반적인 선택 사항입니다. FlashAlpha 및 Unusual Whales는 다른 옵션 분석 공급자 개발자 비교입니다.

### 옵션 흐름과 감마 노출 데이터를 위한 MCP 서버가 있습니까?

예. Skylit의 MCP 서버 호스팅 `https://mcp.skylit.ai/mcp` 63 개의 읽기 전용 도구 커버 옵션 흐름, 스윕, 어두운 풀, GEX 및 VEX 딜러가 포인트 인 시간 재생, 그리고 불쾌한 휘발성. OAuth Sign-in 및 API 키를 지원하며 공식 MCP Registry에 나열되어 있습니다. `ai.skylit/mcp`.

### Skylit을 Claude 또는 ChatGPT에 연결할 수 있습니까?

예. 기타 `https://mcp.skylit.ai/mcp` Claude 또는 ChatGPT의 사용자 정의 커넥터로 Skylit 계정으로 로그인하거나 사용 `claude mcp add --transport http skylit https://mcp.skylit.ai/mcp` Claude 코드. Cursor, VS Code, Gemini CLI, Codex 및 기타 클라이언트에 대한 설정 가이드 [skylit-mcp 저장소](https://github.com/SkylitAI/skylit-mcp).

### Skylit의 API 장소 거래는?

이름 \* 모든 Skylit API 엔드포인트 및 MCP 도구는 읽기 전용 시장 데이터입니다. 자신의 코드에서 주문 실행을 유지하고 자신의 브로커와 함께.

### Skylit의 API는 어떻게 가격?

API 통화는 계정 잔액에서 청구되며, 1 크레딧은 $ 0.001이며 대부분의 통화는 1 ~ 5 크레딧이며 통화가 청구되지 않습니다. Pro는 월간 신용 수당을 포함, 지불 계획은 신용을 추가 할 수 있습니다. pay-as-you-go. 이름 \* [가격 :](https://www.skylit.ai/#pricing) 현재 계획.

### Skylit 데이터로 백업할 수 있나요?

Skylit의 딜러 위치 엔드 포인트는 과거의 순간에 서 정확히 보드를 반환 (`at=`), 그래서 대리인은 보기 ahead 없이 어떤 순간든지에 보이는 것을 볼 수 있습니다. 일일 통계 커버 완료 세션.

### Smarter 거래 시작

Skylit의 딜러 노출 도구를 사용하여 이러한 개념을보십시오.

[접속하다](https://www.skylit.ai/#pricing)[Heatseeker 사용](https://www.skylit.ai/#pricing)
