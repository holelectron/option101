# option101 금융·옵션 번역 용어집

Skylit 원문의 의미·비유·표를 살리면서 자연스러운 한국어로 번역하기 위한 기준입니다.

| English | 한국어 권장 | 주의 |
|---|---|---|
| Options Greeks | 옵션 그릭스 | ‘그리스인들’ 금지 |
| Underlying / Spot | 기초자산 / 현물 가격 | Spot을 ‘반점’으로 번역하지 않음 |
| Strike / Expiration | 행사가 / 만기 | Strike를 ‘파업’으로 번역하지 않음 |
| 0DTE / DTE | 당일 만기 옵션 / 잔존 만기일 | 최초 언급 시 설명 |
| Delta (Δ) | 델타(Δ) | 부호 보존 |
| Gamma (Γ) | 감마(Γ) | 기호 Γ 보존 |
| Gamma Exposure (GEX) | 감마 익스포저(GEX) | 일반 감마와 딜러 GEX 구분 |
| Dealer Positioning | 딜러 포지셔닝 | 모델 기반 추정값 |
| Vega / Theta | 베가 / 세타 | 시간·변동성 민감도 |
| Vanna / VEX | 바나 / 바나 익스포저(VEX) | 델타-IV 교차 민감도 |
| Charm / Vomma | 참 / 봄마 | ‘매력’ 금지 |
| Implied / Realized Volatility | 내재변동성 / 실현변동성 | 명확히 구분 |
| Open Interest (OI) | 미결제약정(OI) | 거래량과 구분 |
| Market Maker / Dealer | 마켓 메이커 / 딜러 | ‘시장 제작자’ 금지 |
| Delta Hedging | 델타 헤징 | 위험 중립화를 위한 거래 |
| Long / Short Gamma | 롱 감마 / 숏 감마 | ‘긴/짧은 감마’ 금지 |
| Positive / Negative GEX | 양의 GEX / 음의 GEX | 방향성 상승·하락 신호와 다름 |
| Contrarian / Pro-cyclical | 역추세 / 추세추종형 | 헤지 방향을 명확히 |
| Mean Reversion | 평균회귀 | 금융 문맥 |
| Pinning | 가격 고정(핀) 현상 | 확정적 표현 금지 |
| Support / Resistance | 지지 / 저항 | 가격 구조 |
| Pika / Barney / King Node | 피카 / 바니 / 킹 노드 | 제품 고유 용어 |
| Hedge Exhaustion | 헤지 수요의 소진 | 추가 헤지 수요 감소라는 뜻 |
| ATM / ITM / OTM | 등가격 / 내가격 / 외가격 | 약어 병기 |
| Buy dips / Sell rips | 하락 시 매수 / 상승 시 매도 | 직역 금지 |
| ELI5 / Core Idea | 쉽게 이해하기 / 핵심 개념 | 원문의 비유 유지 |

## 번역 원칙

1. 제목, 장·절, 본문 논리, 수치, 부호, 공식, 표, 링크, 비유와 주의사항을 보존합니다.
2. 긴 영어 문장은 의미를 유지하면서 자연스러운 한국어 설명체로 다듬습니다.
3. 딜러 포지셔닝은 직접 관측되는 사실이 아니라 모델을 통한 추정임을 구분합니다.
4. 원문을 강화하거나 투자 성과를 보장하는 확정적 표현을 추가하지 않습니다.
5. 원문 자체의 불일치가 있으면 짧은 번역 검토 메모로 알립니다.
6. 영어 .md, 한국어 .ko.md, 원문 HTML은 서로 다른 파일로 보존합니다.

## 번역 스타일 기준

- [Options Greeks](docs/skylit/greeks/options-greeks.ko.md)
- [Gamma Exposure](docs/skylit/greeks/gamma-exposure.ko.md)
- [Dealer Positioning](docs/skylit/heatseeker/dealer-positioning.ko.md)

위 세 문서는 보호 대상이며 자동 번역이 덮어쓰지 않습니다.