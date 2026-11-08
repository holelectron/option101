<!-- Machine translation; review against original. Source: https://www.skylit.ai/learn/theta -->

> **번역 안내:** 이 문서는 자동 번역 초안입니다. 수치·수식·거래 판단은 [영어 원문](theta.md)을 확인하세요.

# Theta Decay: 모든 선택권에 침묵하는 세금

# Theta Decay: 모든 선택권에 침묵하는 세금

greeks·7 분 읽기

사이트 맵

## Theta는 무엇입니까?

**(이태)** 패스를 전달하는 각 일의 옵션의 값에 변화를 측정, 다른 모든 동일을 보유. 긴 옵션 위치를 유지의 relentless 비용입니다 : 시장이 이동하거나하지 여부를 달력으로 지불 할 것입니다.

Theta는 항상 옵션 구매자 및 옵션 판매자에 대 한 긍정적입니다. 매일 긴 옵션 연령, 그것은 그것을 판매 딜러에 그 값의 작은 부분을 surrenders.

ELI5

Theta는 주차 미터입니다. 동전을 먹이는 순간, 시계 시작. 당신은 앉을 수 있고 당신의 무역을 기다리는 것은 떨어져 지불하기 위하여, 그러나 매 시간의 순전히 당신 다른 분기를 요합니다. 시간과 미터가 만료되기 때문에 옵션을 사용합니다.

## Dealer vs. 플레이어 관점

| 제품정보 | 테타 Behavior |
| --- | --- |
| **Dealer (짧은 옵션)** | Harvests theta 매일 언제 delta-hedged |
| **플레이어 (긴 옵션)** | 책임과 방향 레버리지를 임대하는 Pays theta |

Dealers는 선택성을 판매하고 delta-hedge는 지속적으로 방향성 중립을 유지하기 위해. 이렇게, 그들은 체계적으로 이익으로 시간의 통행을, 깨닫는 불쾌한 volatility가 판매된 밑에 체재합니다. 플레이어는 반대쪽을 가지고: 그들은 큰, 빠른 움직임에 노출을 위해 교환에 있는 매일 theta 비용을 받아들입니다.

## Theta가 가장 큰 곳

Theta decays 가장 빠른 가까운 **현금 (ATM)**, **퀵메뉴** 옵션. ATM 옵션의 extrinsic 값은 완전히 시간 값입니다. 만료 접근으로, 그 시간 값은 0에 도달해야합니다. 당신이 expiry에 더 가까이, 가파른 떨림 매일.

- **ATM 옵션:** 최대 theta, 최대 일일 감압
- **딥 ITM / OTM 옵션:** 더 낮은 절대적인 theta; 화상에 더 적은 시간 가치
- **공급 능력:** Theta는 최종 일에서 급격히 가속
- **공급 능력:** Theta는 느리고 달러의 관점에서 겸손

높은 불쾌한 휘발성 팽창 옵션 프리미엄 및 그들과 함께, theta의 절대 달러 값. vol 상승 할 때, 딜러는 하루에 더 많은 theta를 수집합니다. vol가 낙하될 때, 우수한 압축 및 theta는 구매자를 위해 쉽게 요합니다.

## Theta의 관계 다른 그리스

Theta의 통행은 상호 작용합니다 [옵션 greeks](https://www.skylit.ai/learn/options-greeks) 시간에 합성하는 방법에서.

### 테타와 매력

시간 패스로, 델타 드립. 이 drift, 호출 **[인기 있는](https://www.skylit.ai/learn/charm)**, 시간에 따라 delta의 변화의 비율입니다. ATM 옵션의 경우, 매력은 델타를 0.50 (calls) 또는 -0.50 (puts)를 0.50 (puts)로 끌어냅니다. 딜러는 가격이 이동하지 않을 때 델타 헤지를 반송합니다.

### Theta와 색깔

[Gamma 노출](https://www.skylit.ai/learn/gamma-exposure) 또한 시간과 변화. gamma가 시간으로 변경되는 비율은 호출됩니다. **색상 (∂/∂t)**. 탐험의 가까이에, gamma 스파이크는 ATM 선택권을 위해 날카롭게 하고 그 때 expiry에 0에 붕괴합니다. 색상은 그 전환 속도를 측정합니다. 플레이어 임대, 아주 좋은 것은 가격입니다, expiration 접근법으로 더 집중됩니다.

회사소개

Theta, 매력 및 색상은 시간 - 데카 클러스터를 형성합니다. Theta는 값 배수를 측정합니다. 매력은 델타가 배수로 이동하는 방법을 측정합니다. 색은 감마가 어떻게 진화하는지 측정합니다. 모든 세 가지 이해는 expiration에 위치 관리에 필수적입니다.

## Vol Regime 효과 에 Theta

**화산이 상승할 때:** Implied 휘발성 팽창 옵션 프리미엄. Dealers는 더 높은 절대적인 theta를 모으고, 또한 더 큰 감마 노출을 직면합니다. 상승시키는 상쇄는 큰 깨달은 움직임의 높게 위험은 감마 헤지를 표백했습니다.

**화산이 떨어질 때:** 우수한 압축. 구매자를 위한 Theta 비용 쉽게. 판매자는 달러 조건에서 하루에 덜 수집하지만, 환경은 더 안정적이고 감마 헤지 유지가 저렴합니다.

## Pinning와 Theta 정렬

매일 가격 피닝은 특정 파업 근처의 큰 옵션 포지셔닝 집중이 발생할 수 있습니다. 그 공격에 대한 옵션 expiring Zero theta expiration, 그러나 실제 힘은 딜러의 Hedging flows management their gamma and delta 노출 가까운.

긍정적 [gamma 노출](https://www.skylit.ai/learn/gamma-exposure) (+GEX) 및 긍정적인 vanna 노출 (+VEX) 정렬, 딜러는 가격 움직임을 반대하는 방식으로 헤지, 핀 타격 주위에 안정성을 강화. 그런 날, theta decay는 구조상 상인을 가진 연주회에서 깨달은 휘발성을 억압하기 위하여 작동합니다.

Heatseeker에서 이것을 보십시오

theta decay 및 GEX 정렬이 Heatseeker와 함께 매일 핀닝 영역을 만듭니다.

[Heatseeker 사용](https://www.skylit.ai/#pricing)

## 자주 묻는 질문

### Theta decay는 무엇입니까?

Theta는 다른 모든 동등한 것을 전달하는 각 일마다 옵션의 값에 변화를 측정합니다. 그것은 항상 옵션 구매자 및 옵션 판매자에 대 한 긍정적입니다. 매일 긴 옵션 연령, 시장 이동 여부에 관계없이 나머지 extrinsic 값의 일부를 surrenders. Theta decays는 at-the-money, short-dated options, 전체 프리미엄은 expiry에서 0에 도달해야하는 extrinsic 값입니다.

### 어떻게 theta는 옵션 판매자 대 구매자에 영향을합니까?

옵션 판매자, 일반적으로 딜러, 수확 theta 매일 그들이 delta-hedged 및 실현 된 휘발성 그들은 판매 된 임베디드 volatility 남아. Option 구매자는 convexity 및 방향 레버리지 옵션을 제공합니다. 구매자는 매일 비용을 극복하기 위해 빠르고, 큰 움직임을 필요로 합니다; 판매인은 여전히와 시간 통행에서 이익을. 높은 불쾌한 휘발성은 절대 프리미엄을 팽창시킵니다. 즉, 딜러는 하루에 더 많은 시타를 수집하지만, 더 큰 감마 노출을 Tradeoff로 직면합니다.

### 옵션 pinning 및 theta 원인은 무엇입니까?

옵션 핀은 가격 변동이 크게 파열될 때입니다. 그것은 핀을 만드는 데 직접 theta하지 않습니다; 그것은 그 옵션으로 gamma 및 delta 노출을 관리하는 딜러입니다 0 extrinsic 값. 긍정적 인 GEX와 긍정적 인 vanna 노출이 파업에 맞을 때, 딜러 헤지스는 어떤 움직임을 반대, 안정성 강화. Theta decay는 구조적인 압력으로 콘서트에서 작동하며, 폭발적인 접근법으로 실현된 변동성을 억제하고, 그 공격의 옵션은 나머지 시간 값을 잃습니다.

### Smarter 거래 시작

Skylit의 딜러 노출 도구를 사용하여 이러한 개념을보십시오.

[접속하다](https://www.skylit.ai/#pricing)[Heatseeker 사용](https://www.skylit.ai/#pricing)
