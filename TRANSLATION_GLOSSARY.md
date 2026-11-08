# option101 · 금융·옵션 번역 용어집 (검증판 v2)

> 검증일: 2026-11-08 · 범위: Skylit Learn 45개 문서의 한국어 번역 기준  
> **출처 등급:** **[표준]** OCC/OIC·CME·KRX의 정의와 대조 · **[해석]** 금융시장 분석에서 쓰는 일반적 해석 · **[Skylit]** 해당 서비스의 명명·모델·서술  
> 이 문서는 **한국어 번역 표준**이지, 딜러 포지셔닝 모델의 정확성이나 투자 수익을 인증하는 문서가 아닙니다.

## 1. 옵션 계약·가격·거래 기본 용어

| 영어 원문 | 권장 한국어 | 의미·번역상 주의 | 구분 |
| --- | --- | --- | --- |
| Option / Call / Put | 옵션 / 콜옵션 / 풋옵션 | 콜은 매수 권리, 풋은 매도 권리 | 표준 |
| Underlying / Underlying Asset | 기초자산 | 주식·지수·선물 등 옵션 가격의 기초 | 표준 |
| Spot / Spot Price | 현물 가격 / 현재 기초자산 가격 | ‘반점’ 금지; 지수 옵션에서는 현 지수 수준일 수 있음 | 표준 |
| Strike / Strike Price | 행사가(격) | ‘파업’ 금지 | 표준 |
| Expiration / Expiry | 만기 / 만기일 | 만기와 최종거래일·결제일은 구분 | 표준 |
| DTE (Days to Expiration) | 잔존 만기일(DTE) | 거래일/달력일 계산 관례 확인 | 표준 |
| 0DTE | 당일 만기 옵션(0DTE) | 만기 당일 거래되는 옵션 | 표준 |
| Premium | 옵션 프리미엄(옵션 가격) | 계약당 프리미엄과 주당 호가 단위 구분 | 표준 |
| Intrinsic Value | 내재가치 | 콜 max(S−K,0), 풋 max(K−S,0) | 표준 |
| Extrinsic / Time Value | 외재가치 / 시간가치 | 프리미엄 중 내재가치를 초과하는 부분 | 표준 |
| At-the-Money (ATM) | 등가격(ATM) | 행사가와 현물가격이 거의 같음 | 표준 |
| In-the-Money (ITM) | 내가격(ITM) | 콜: S>K, 풋: S<K | 표준 |
| Out-of-the-Money (OTM) | 외가격(OTM) | 콜: S<K, 풋: S>K | 표준 |
| Moneyness | 가격상태(ITM·ATM·OTM) / 머니니스 | 공식/기술 문맥에서 ‘머니니스’ 병기 | 표준 |
| Option Chain | 옵션 체인(행사가·만기별 호가표) | ‘사슬’ 금지 | 표준 |
| Contract Multiplier | 계약승수 | 계약 1개가 나타내는 기초자산 수량, 상품별 상이 | 표준 |
| Exercise | 권리행사 | 옵션 보유자가 권리 사용 | 표준 |
| Assignment | 배정(옵션 매도자의 이행 의무 확정) | ‘할당’보다 옵션 문맥상 배정 권장 | 표준 |
| Early Exercise | 조기 권리행사 | 미국형 옵션 등에 해당 | 표준 |
| American-style / European-style | 미국형 / 유럽형 옵션 | 권리행사 가능 시점의 차이; 거래 지역 아님 | 표준 |
| Physical / Cash Settlement | 실물인수도 / 현금결제 | 상품별 계약 명세 확인 | 표준 |
| Open Interest (OI) | 미결제약정(OI) | 현재 열려 있는 계약 수; 거래량과 다름 | 표준 |
| Volume | 거래량 | 특정 기간 체결된 계약 수 | 표준 |
| Bid / Ask | 매수호가 / 매도호가 | 거래 상대의 호가 관점 | 표준 |
| Bid–Ask Spread | 매수·매도 호가 스프레드 | 거래비용과 유동성 평가에 사용 | 표준 |
| Liquidity | 유동성 | 거래량뿐 아니라 스프레드·시장충격 고려 | 표준 |
| Slippage | 슬리피지(체결 가격 차이) | 기대가격과 실제 체결가격 차이 | 표준 |
| Break-even Point | 손익분기점 | 만기 기준인지 시점별 이론가격 기준인지 구분 | 표준 |
| Margin | 증거금 | 초기·유지증거금 등 상품별 상이 | 표준 |
| Notional Exposure | 명목 익스포저(명목 노출액) | 실제 델타 헤지 수량과 다름 | 표준 |

## 2. 표준 옵션 그릭스

| 영어 원문 | 권장 한국어 | 정의·단위 주의 | 구분 |
| --- | --- | --- | --- |
| Options Greeks | 옵션 그릭스(위험 민감도 지표) | ‘그리스인들’ 금지 | 표준 |
| Delta (Δ) | 델타(Δ) | 기초자산 가격 변화에 대한 옵션 가치의 1차 민감도 | 표준 |
| Gamma (Γ) | 감마(Γ) | 기초자산 가격에 대한 델타의 변화율; 기호 Γ 그대로 | 표준 |
| Vega (ν, 통상 Vega) | 베가(Vega) | IV 변화에 대한 옵션 가치의 민감도; 보통 **IV 1%포인트** 기준으로 표시하지만 벤더별 단위 확인 | 표준 |
| Theta (Θ) | 세타(Theta) | 시간 경과에 따른 옵션 가치 변화; 보통 하루 기준 | 표준 |
| Rho (ρ) | 로(Rho, 금리 민감도) | 금리 변화에 따른 옵션 가치 민감도 | 표준 |
| Vanna | 바나(Vanna) | IV 변화에 따른 델타의 변화율 = 가격 변화에 따른 베가 변화율(관례·단위 확인) | 표준 |
| Charm / Delta Decay | 참(Charm) / 델타의 시간 변화 | ‘매력’ 금지; **잔존시간 감소 vs 경과시간**의 부호 관례 확인 | 표준 |
| Vomma / Volga | 봄마(Vomma·Volga) | IV 변화에 따른 베가 변화율; 변동성 곡률 | 표준 |
| Speed | 스피드(Speed) | 가격 변화에 따른 감마의 변화율 | 표준 |
| Color | 컬러(Color) | 시간에 따른 감마 변화율; 시간 부호 관례 확인 | 표준 |
| Zomma | 좀마(Zomma) | IV 변화에 대한 감마 민감도 | 표준 |
| Vera | 베라(Vera) | IV 변화에 대한 로(Rho) 민감도 | 표준 |
| Veta | 베타가 아닌 **베타(Veta)** 또는 **베가의 시간 변화율(Veta)** | Vega decay; 표기 시 영문 Veta 병기해 베타(Beta)와 구별 | 표준 |
| Ultima | 울티마(Ultima) | IV 변화에 따른 봄마의 변화율; 고차 미분 표기 확인 | 표준/모델 |
| Long / Short Delta | 롱 델타 / 숏 델타 | 포지션 총델타의 부호 | 해석 |
| Long / Short Gamma | 롱 감마 / 숏 감마 | ‘긴/짧은 감마’ 금지 | 해석 |
| Delta-neutral | 델타 중립 | 다른 그릭스의 위험까지 0이라는 뜻은 아님 | 해석 |
| Dynamic Delta Hedging | 동적 델타 헤징 | 변화하는 델타에 맞춰 주식·선물을 재조정 | 해석 |
| Cross-Greek | 교차 그릭스 | 두 위험 변수 사이의 민감도 | 해석 |
| Convexity | 볼록성(컨벡서티) | 가격·변동성 중 어느 차원의 곡률인지 설명 | 해석 |

### 수학 기호와 변화 단위 규칙

- **가격 S, 행사가 K, 시간 T, 변동성 σ**의 의미를 표기하고, 원문의 `Γ`, `Δ`, `Θ`, `ν`, `ρ`, `±`, `−`를 유지합니다.
- IV의 **20% → 21%**는 **1%포인트 상승**이지 **1% 상대 상승**이 아닙니다. Vega는 플랫폼·교재에 따라 단위 정의가 다를 수 있으므로 수치를 임의 변환하지 않습니다.
- **감마(Gamma)**와 **GEX(개별 감마를 포지션·계약승수 등으로 집계한 노출량)**를 같은 지표로 번역하지 않습니다.
- 그릭스는 다른 입력변수를 고정한 **국소적 이론 민감도**입니다. 모델값을 확정적인 실현 가격 변화로 쓰지 않습니다.
- **ATM 델타가 반드시 ±0.50인 것은 아닙니다.** 만기·배당·이자율·모델에 따라 달라질 수 있으므로 ‘대체로 ~부근’으로 설명합니다.

## 3. 변동성·딜러 헤징·시장 구조

| 영어 원문 | 권장 한국어 | 주의·적용 문맥 | 구분 |
| --- | --- | --- | --- |
| Implied Volatility (IV) | 내재변동성(IV) | 옵션 가격에서 모델로 역산한 변동성 | 표준 |
| Historical Volatility (HV) | 과거변동성 | 과거 관측 구간에 기반한 추정치 | 표준 |
| Realized Volatility (RV) | 실현변동성 | 특정 기간 실제 수익률의 변동성 | 표준 |
| Volatility Crush / IV Crush | 내재변동성 급락(IV 크러시) | 이벤트 전후 자주 쓰이는 표현 | 해석 |
| Volatility Skew | 변동성 스큐(행사가별 IV 편차) | 동일 만기의 행사가별 IV 차이 | 표준 |
| Volatility Smile / Smirk | 변동성 스마일 / 스머크 | 곡선 모양에 따른 표현 | 표준 |
| Volatility Surface | 변동성 표면 | 행사가와 만기별 IV 구조 | 표준 |
| Term Structure | 기간구조(만기구조) | 만기별 IV 차이 | 표준 |
| VIX | VIX(미국 주식시장 변동성지수) | 주가 방향을 알려주는 지표 아님 | 표준 |
| Market Maker / Dealer | 마켓 메이커 / 딜러 | ‘시장 제작자’ 금지; 딜러 목적·포지션 단정 금지 | 표준 |
| Dealer Positioning | 딜러 포지셔닝 | 직접 공개된 전체 순포지션이 아닌 **모델 기반 추정**일 수 있음 | 해석 |
| Dealer Gamma Exposure (Dealer GEX) | 딜러 감마 익스포저(딜러 GEX) | 포지션 방향 추정 및 집계 관례 확인 | 모델 |
| Gamma Exposure (GEX) | 감마 익스포저(GEX) | 감마 자체와 구별; 계산 단위·부호 관례 확인 | 모델 |
| Vanna Exposure (VEX) | 바나 익스포저(VEX) | 집계·부호·딜러 매매 방향이 플랫폼별로 다를 수 있음 | 모델 |
| Positive / Negative GEX | 양의 / 음의 GEX | **GEX의 부호 ≠ 상승 / 하락 전망** | 모델 |
| Gamma Flip / Zero Gamma | 감마 플립 / 감마 중립 전환 지점 | 총GEX 추정 부호가 바뀌는 가격대; 정확한 방향 예측 아님 | 모델 |
| Gamma Wall / Put Wall / Call Wall | 감마 집중 구간 / 풋 월 / 콜 월 | 노출·OI의 집중 구간을 가리키는 시장 용어; 공식 지지·저항 아님 | 해석 |
| Long Gamma Hedging | 롱 감마 헤징 | 다른 조건이 같으면 하락 시 매수·상승 시 매도 경향 | 해석 |
| Short Gamma Hedging | 숏 감마 헤징 | 다른 조건이 같으면 하락 시 매도·상승 시 매수 경향 | 해석 |
| Contrarian / Pro-cyclical | 역추세 / 추세추종형(순응적) | ‘프로 사이클론’ 금지 | 해석 |
| Mean Reversion | 평균회귀 | ‘의미를 되돌림’ 금지 | 해석 |
| Feedback Loop | 피드백 루프(되먹임 구조) | 옵션 헤지와 현물가격의 상호작용 | 해석 |
| Liquidity Vacuum | 유동성 공백 | 갑작스러운 가격 이동을 뜻할 때 | 해석 |
| Pinning | 가격 고정(핀) 현상 | 특정 행사가 부근 정체 가능성, 보장 아님 | 해석 |
| Hedge Exhaustion | 추가 헤지 수요의 소진 | 헤지 불가능이 아니라 **증분 헤지 수요 감소** | 해석 |
| Order Flow / Options Flow | 주문 흐름 / 옵션 거래 흐름(옵션 플로우) | 매수·매도 *의도*를 체결만으로 확정하지 않음 | 해석 |
| Dark Pool Prints | 다크풀 체결 내역 | 체결 정보만으로 순매수 방향 단정 금지 | 해석 |
| Unusual Options Activity | 이례적 옵션 거래 | 대량 거래 ≠ 무조건 신규 방향성 베팅 | 해석 |
| Dealer Inventory | 딜러 보유 포지션(재고) | 체결과 현재 순잔고 구분 | 해석 |
| Notional vs Delta-Adjusted Exposure | 명목 익스포저 / 델타 조정 익스포저 | 다른 지표를 섞지 않음 | 모델 |
| Risk Reversal | 리스크 리버설 | 전략 또는 동일 델타 풋/콜 IV·가격 차이, 문맥에 따라 구분 | 표준/해석 |

### 딜러 GEX·VEX 번역의 필수 주의 문구

> GEX·VEX 지표는 옵션 민감도와 포지션 자료를 결합한 **분석 모델의 결과**입니다. 시장 전체 딜러의 실제 포지션 방향이 직접 관측된다는 뜻이 아니며, 사용하는 데이터·계산식·부호 관례에 따라 추정 결과가 달라집니다. 양의 GEX를 ‘무조건 지지’, 음의 GEX를 ‘무조건 급락’으로 옮기지 않습니다.

## 4. 전략·위험 관리·실행

| 영어 | 권장 한국어 | 주의 | 구분 |
| --- | --- | --- | --- |
| Covered Call | 커버드 콜 | 주식 보유 + 콜 매도 | 표준 |
| Cash-secured Put | 현금 담보 풋 매도 | 담보·배정 의무 설명 | 표준 |
| Debit / Credit Spread | 데빗(순지급) / 크레딧(순수취) 스프레드 | 처음 등장 시 지급·수취 설명 | 표준 |
| Vertical / Calendar / Diagonal Spread | 수직 / 캘린더 / 대각 스프레드 | 행사가·만기 차이 명시 | 표준 |
| Straddle / Strangle | 스트래들 / 스트랭글 | 기초 전략 명칭 보존 | 표준 |
| Iron Condor / Butterfly | 아이언 콘도르 / 버터플라이 | 다리(legs) 구조 설명 | 표준 |
| Bullish / Bearish | 강세 / 약세(상승 / 하락 관점) | 방향과 포지션 종류 구분 | 표준 |
| Payoff / P&L | 만기 손익구조 / 손익(P&L) | 만기 payoff와 보유 중 평가손익 구분 | 표준 |
| Maximum Loss / Drawdown | 최대손실 / 낙폭(드로다운) | 전략별 손실 한도와 과거 자산곡선 구분 | 해석 |
| Position Sizing | 포지션 규모 조절 | 거래 단위·최대손실 기준 | 해석 |
| Stop-loss / Take-profit | 손절 / 익절 | 실제 보장되는 체결가 아님 | 해석 |
| Slippage / Execution Cost | 슬리피지 / 체결 비용 | 스프레드·수수료 포함 여부 확인 | 표준 |
| Backtest / Look-ahead Bias | 백테스트 / 미래정보 편향 | 체결·수수료·데이터 시점 검증 | 해석 |
| Win Rate / Expectancy | 승률 / 기대손익 | 승률이 높아도 기대손익 음수 가능 | 해석 |

## 5. Skylit 제품·비유·특정 패턴 표현

| 영어 | 권장 한국어 | 출처·의미 |
| --- | --- | --- |
| Heatseeker / Flowseeker | Heatseeker / Flowseeker | 제품명 그대로 보존 |
| Pika Node / Barney Node | 피카 노드 / 바니 노드 | Skylit의 양·음 GEX 노드 명명; 화면 색만으로 부호 결정하지 않음 |
| King Node | 킹 노드 | Skylit에서 **GEX 절댓값이 최대**인 노드 |
| Gatekeeper | 게이트키퍼 | 해당 문서에서 역할 설명; 보편적인 표준 금융 용어로 단정하지 않음 |
| Floor / Ceiling | 하단 지지 구간 / 상단 저항 구간 | 제품 기능에 따른 맥락 확인 |
| Rug / Reverse Rug | 러그 / 리버스 러그 | Heatseeker 패턴명; 처음에 쉬운 설명 병기 |
| Pika Cloud / Beach Ball | 피카 클라우드 / 비치볼 | 고유 패턴·비유; 자체 모델 명명 |
| Velocity Mode / Trinity Mode | Velocity Mode / Trinity Mode | UI 기능 이름 원문 보존 |
| ELI5 | 쉽게 이해하기 | 원문의 비유 유지 |
| Core Idea | 핵심 개념 | 원문의 논리와 조건 유지 |
| Thesis / Confirmation | 매매 가설 / 확인(검증) | ‘논문’ 금지 |
| Buy the Dip / Sell the Rip | 하락 시 매수 / 상승 시 매도 | 직역 및 무조건적 추천 표현 금지 |

## 6. 번역 규칙 및 검증 체크리스트

1. **완역**: 제목, 장·절·본문·비유·표·목록·FAQ·경고·원문 URL을 누락하거나 임의 요약하지 않습니다.
2. **자연스러움**: 영어 어순을 그대로 따르지 않습니다. 금융 학습서에 맞는 정확하고 읽기 쉬운 한국어 설명체를 사용합니다.
3. **첫 등장 원어 병기**: 상대적으로 생소한 전문 용어는 ‘한글 표기(영어, 약어)’로 제시한 뒤 동일 표현을 사용합니다.
4. **수치 불변**: 계약승수, 가격·변동성 단위, +/- 부호, 기호·수식·조건문을 보존합니다. 특히 IV의 %와 %p를 구분합니다.
5. **표준 정의 vs 제품 분석**: OCC/OIC·CME의 옵션 정의와 Skylit의 추정·패턴을 구분합니다. 원문의 주장을 사실로 강화하지 않습니다.
6. **딜러 행위의 불확실성**: ‘반드시 매수’, ‘확정적인 저항’보다 ‘~하는 경향’, ‘~일 수 있음’을 문맥에 맞게 사용합니다.
7. **링크·Markdown 보존**: URL·앵커·코드·표의 행/열을 확인합니다. 번역 소스의 영어 원문 링크는 VitePress에서는 영문 경로로 연결합니다.
8. **이상 발견 시 메모**: 원문에 모순·단위 불일치·설명이 과도한 부분은 조용히 고쳐 쓰지 않고 ‘번역 검토 메모’를 남깁니다.
9. **보존 규칙**: 영어 `.md`, 원본 `.html`, 한국어 `.ko.md`를 구분하고, 검수한 문서의 자동 덮어쓰기를 막습니다.

## 7. 실제 검색·대조 출처

| 기관 / 문서 | 검증한 내용 | URL |
| --- | --- | --- |
| OCC / OIC — Understanding Options Greeks | 주요 그릭스의 이론적 민감도와 한계 | https://prd-web.optionseducation.org/advancedconcepts/understanding-options-greeks |
| OCC / OIC — Options Glossary | 계약·행사가·포지션·고차 그릭스·전략 | https://prd-web.optionseducation.org/referencelibrary/optionsglossary |
| OCC / OIC — Vanna/Vomma/Vera/Veta | 교차 그릭스의 정의 | https://www.optionseducation.org/referencelibrary/optionsglossary?filter=v |
| OCC / OIC — Charm | 델타의 시간 변화 | https://www.optionseducation.org/referencelibrary/optionsglossary?filter=C |
| OCC / OIC — Options Pricing | 내재가치·시간가치와 옵션 프리미엄 | https://www.optionseducation.org/optionsoverview/options-pricing |
| OCC / OIC — Exercise & Assignment | 행사·배정 및 조기 행사 위험 | https://www.optionseducation.org/referencelibrary/faq/options-assignment |
| CME Group — Options Vega | IV와 베가의 구분, 변동성 포인트 예시 | https://www.cmegroup.com/education/courses/option-greeks/options-vega-the-greeks |
| OCC / OIC — Technical Information | 과거변동성·IV·스큐의 설명 | https://www.optionseducation.org/referencelibrary/faq/technical-information |
| OCC / OIC — Options Skew | 같은 만기 내 행사가별 IV 차이 | https://prd-web.optionseducation.org/news/volatility-skew-and-options-an-overview-1 |
| 한국거래소 KIND 공시의 용어 설명 | 델타·감마·베가·세타·로의 한국어 표기 | https://kind.krx.co.kr/external/2016/07/21/000452/20160721001222/10001.htm |
| KRX 파생상품 시장 상품 명세 | 상품별 계약승수·결제방식이 다를 수 있음 | https://global.krx.co.kr/contents/GLB/02/0201/0201040210/GLB0201040210.jsp |

## 8. 검수 완료 문서와 다음 번역 기준

- [Options Greeks](docs/skylit/greeks/options-greeks.ko.md)
- [Gamma Exposure](docs/skylit/greeks/gamma-exposure.ko.md)
- [Dealer Positioning](docs/skylit/heatseeker/dealer-positioning.ko.md)

위 세 문서의 **자연스러운 설명 문체**를 기준으로 삼되, 정의·부호·단위의 불일치가 있다면 본 검증판 용어집을 우선합니다. 원문·번역문 간 차이를 별도 점검하고 자동 번역 도구로 덮어쓰지 않습니다.
