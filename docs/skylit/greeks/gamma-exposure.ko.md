<!-- Machine translation; review against original. Source: https://www.skylit.ai/learn/gamma-exposure -->

> **번역 안내:** 이 문서는 자동 번역 초안입니다. 수치·수식·거래 판단은 [영어 원문](gamma-exposure.md)을 확인하세요.

# 감마 노출 (GEX) 설명 : 시장의 충격 흡수기

# 감마 노출 (GEX) 설명 : 시장의 충격 흡수기

greeks·12 분 읽기

gammagexdealer 위치heatseeker

## Gamma Exposure 란 무엇입니까?

**Gamma (호텔)** 델타의 변화의 비율을 측정 $1 밑으로 이동. 시장의 평균 회전 또는 가속 여부를 제어합니다.

딜러가 될 때 **긴 감마 (+GEX)**, Heatseeker에 Pika 노드 호출 ( 아카데미의 "노란 노드"), 그들의 헤지는 시장의 움직임에 반대. 그들은 딥을 구입하고 rips을 판매합니다. 그것은 안정성과 의미를 만듭니다.

딜러가 될 때 **짧은 감마 (–GEX)**, Heatseeker에 Barney 노드 호출 ( 아카데미의 "퍼플 노드"), 그들의 헤지 움직임을 추적. 그들은 복각을 판매하고 rips를 사십시오. 그것은 휘발성 증폭.

보드 자체에서 셀 색상은 선택한 팔레트와 노드의 크기를 따르기 때문에 기호가 아니라 숫자와 마이너스 기호를 읽습니다.

ELI5

Gamma는 차의 현탁액입니다: 평온한 조건에서 매끄러운, 그러나 얼음에 불안정한. +GEX에서 충격은 범프를 흡수합니다. –GEX에서, 모든 범프는 코스를 더 던져.

## 어떻게 GEX Affects 시장 Behavior

| (주) | Dealer 헤지 | 시장 Behavior |
| --- | --- | --- |
| **+GEX (롱 Γ)** | 구매 딥, 판매 rips | 안정성은, reversion를 의미합니다 |
| **–GEX (Short Γ)** | 판매 딥, 구매 rips | 휘발성 증폭 |

**위/아래 반점:** +GEX 아래는 지원으로 작동합니다. 점의 위 +GEX는 저항으로 작동합니다. GEX 기호 변경은 극성 플립이며 가장 폭력적인 움직임이 발생합니다. Heatmap의 가장 높은 절대적인 GEX 값을 가진 노드가 호출됩니다. **킹 노드**. 그것은 긍정 또는 부정적인 일 수 있고, 시장 제작자가 가장 큰 노출을 붙들고 어디 가격은 expiration의 가까이에 gravitates를 수시로 gravitates.

## Vol Behavior 과 GEX

변동성 상승 증폭 –GEX 효과. 변동성 하락은 +GEX 핀을 강화합니다. GEX 정의 *주요 특징*. VIX 정의 *뚱 베어*.

회사소개

각 그리스는 딜러가 중립화해야하는 위험의 차원입니다. 군중 노출이 이동할 때, 상인은 반동합니다. 그들의 쐐기는 가격, 휘발성 및 유동성으로 다시 공급합니다.

## Cross-Greek 기계장치

- **딜러가 긴 델타 인 경우 → 그들은 주식을 판매** neutralize에; **짧은 delta → 그들은 주식을 구입**.
- **긴 감마 (+GEX)** 그 사고/판매 행동 **이름 \*** 가격 (stabilizing).
- **짧은 감마 (–GEX)** 그대에게 **프로 사이클론** (채색).

Heatseeker에서 이것을 보십시오

Heatseeker의 감마 노출 히트맵과 함께 모든 파업 및 만료를 통해 라이브 GEX 수준을 시각화합니다.

[Heatseeker 사용](https://www.skylit.ai/#pricing)

## 시간 및 Tenor

- **0DTE:** Gamma와 매력 지배. Vanna는 0 근처에 있습니다. 당일 핀과 휴식 규칙 intraday. 이름 \* [0DTE SPX용 GEX 도구](https://www.skylit.ai/learn/best-gex-tools-0dte-spx) 같은 날 열을 읽을 수 있습니다.
- **1–7 DTE:** 교통 영역. Gamma는 여전히 크지만 Vanna는 문제로 시작합니다.
- **>30 DTE:** Vanna/Vega 세계. IV 경로는 hedging를 통해 가격을 드리프트합니다.

Gamma 가늠자 대략 것과 같이 **1/√T에**. 짧은 차원 선택권에는 폭발성 감마가 있습니다. 긴 차원 옵션은 매우 작습니다.

## 자주 묻는 질문

### 감마 노출 (GEX)은 무엇입니까?

Gamma 노출은 델타의 변화의 비율을 측정 $1 아래 자산에서 이동. 시장 업체의 Hedging 활동이 안정화되거나 가격 이동을 증폭 여부를 결정합니다. 당신은 열지도에 GEX 독서를 볼 때, 당신은 얼마나 많은 기계 구매 또는 판매 압력 상인이 그 수준을 통해 가격 이동으로 적용 할 의무가 있습니다.

### GEX는 재고 가격에 영향을 미칩니까?

긍정적 인 GEX는 딜러가 긴 감마를 의미하므로 헤지는 피난처입니다. 그들은 딥을 구입하고 냄새를 판매하고, 안정성과 그 주변의 재생을 의미합니다. Negative GEX 플립 그 역동적으로. Dealers는 짧은 감마, 그래서 그들의 힌트는 딥을 판매 하 고 립을 구입 하 여 이동을 추적, 휘발성 및 추세를 가속화.

### 긍정적이고 부정적인 GEX의 차이점은 무엇입니까?

Positive GEX 노드(Heatseeker에서 Pika 노드 호출)는 딜러가 가격에 반대하는 파업을 나타냅니다. 즉, 변속 동작을 생성합니다. Negative GEX 노드(called Barney nodes)는 딜러가 pro-cyclical 인 파업을 나타내는 파업을 나타냅니다. 2 사이의 기호 변경은 극성 플립과 가장 폭력적인 가격 움직임이 발생할 수 있습니다.

### 킹 노드는 무엇입니까?

King Node는 전체 히트맵에서 가장 큰 절대적인 GEX 값으로 타격됩니다. 그것은 긍정적인 또는 부정적인 일 수 있습니다, 그래서 항상 안정 수준은 아닙니다. 그것은 시장 제작자가 가장 큰 노출을 잡고 어디 가격은 종종 expiration 근처에서 gravitates를 잡아. Market Maker는 종종 세션에서 늦은 King Node 근처의 핀 가격, GEX 기반 분석에서 가장 많이 사용되는 참조 포인트 중 하나입니다.

### Smarter 거래 시작

Skylit의 딜러 노출 도구를 사용하여 이러한 개념을보십시오.

[접속하다](https://www.skylit.ai/#pricing)[Heatseeker 사용](https://www.skylit.ai/#pricing)
