<!-- Machine translation; review against original. Source: https://www.skylit.ai/learn/charm -->

> **번역 안내:** 이 문서는 자동 번역 초안입니다. 수치·수식·거래 판단은 [영어 원문](charm.md)을 확인하세요.

# 매력: Invisible Drift That Moves Markets

# 매력: Invisible Drift That Moves Markets

greeks·7 분 읽기

비밀번호

## 매력은 무엇입니까?

**인기 있는** 측정 방법 [델타](https://www.skylit.ai/learn/delta) 시간 패스로 변경, 유지 가격 및 불쾌한 변동. 때로는 delta decay라고 불립니다. 상인의 힌트로데스가 통과하는 모든 시간 동안, 심지어 underlying이 이동하지 않을 때.

시간 패스로, [옵션 greeks](https://www.skylit.ai/learn/options-greeks) 이동: out-of-the-money 통화는 expiry 접근으로 델타를 잃습니다. 넣어, delta는 더 적은 부정적인, 0을 향해 드리기. 두 경우, 헤지로 주식 또는 미래를 보유하는 딜러는 그 헤지가 이제 그들이 나르는 데 필요한 델타에 너무 크다.

ELI5

Charm는 느린 throttle를 추가하는 순항 통제입니다. 도로는 변경되지 않습니다, 속도 제한은 변경되지 않습니다, 그러나 자동차는 조용하게 표적을 붙들기 위하여 배경에 있는 힘을 조정합니다. Dealers는 같은 일을하고 있습니다: 그들의 delta 표적으로 주식을 적시기 때문에 incrementally 사는 또는 판매.

## 어떻게 매력 드라이브 Dealer 흐름

| 제품정보 | 채용 정보 |
| --- | --- |
| **딜러 (long call)** | 호출 delta 시간과 수축, 딜러는 긴 재고 힌지를 감소, 하지만 그들은 짧은 전화, 그들은 플랫 북을 유지하기 위해 주식을 구입 |
| **+GEX 정권에 있는 순수한 효력** | 더 높은 delta에 대 한 Dealers rebalance 구매, 높은-exposure 파업으로 느린 상승을 생산 |

이 리밸런싱은 **어떤 가격 이동 없이 어떤 vol 이동 없음**. 매력은 순수하게 시간의 기능입니다. 완전히 평평한, 조용한 테이프에 조차, 딜러의 헤지 필요조건은 표면의 밑에 교대합니다.

Charm는 at-the-money와 expiration에 가까운 선택권을 위해 가장 강합니다. Deep in-the-money or far out-of-the-money options see very little charm because their deltas are already near 1 or 0 each. 긴 차원의 옵션은 매력적인 매력이 있습니다. 감퇴는 너무 느리다.

## 오후 드리프트

매력은 시간 중심이기 때문에 오후에 그것의 효과 집중. 세션 진행으로, 더 많은 시간 가치는 감퇴했다. 테이프가 조용하고 딜러가 쐐기 큰 가격 움직임에 강제하지 않을 때 낮은 VIX 요법에서, 매력은 마지막 시간에 지배적 인 흐름 메커니즘이됩니다.

관찰 된 패턴 : 가격은 최대 옵션 포지셔닝으로 타격을 천천히 그립니다. 이것은 때때로 불립니다 **핀닝**, 그러나 drift는 더 정확합니다. 딜러는 레벨을 방어하지 않습니다. 그들은 더 적은 주식을 필요로 하는 위치에 그들의 책을 기계적으로 rebalancing.

회사소개

Charm는 ATM 근처에 가장 강하고 expiry와 가까운, 깊은 ITM/OTM 옵션과 긴 계약에 가장 약한. 조용한 세션에서 오후 테이프는 종종 매력 지배된다 : 느린, 그라인드, 짧은, 명백한 촉매없이.

## Vanna와 매력 Drift

매력은 거의 고립에서 작동합니다. 진정으로, 낮은 변동성 세션과 결합 [vanna 노출](https://www.skylit.ai/learn/vanna-exposure) 상인이 꾸준한 "melt"라고 설명하는 것을 생산하기 위해.

- **Vanna 드리프트:** 불쾌한 압축 때, 긴 vega가 자신의 힌트를 다시 구입 한 딜러. Upward 가격 drift는, 시장에 있는 긍정적인 vanna 노출의 크기에 비례합니다.
- **공급 능력:** 별도의 시간 감퇴는 deltas를 감소시킵니다. Dealers rebalance by 사고. 더 상승, vol 이동 필요 없음.

둘 다 현재, 떨어지는 IV 및 통과 시간, 교류 더미. 각 기계장치는 개인적으로 작습니다, 그러나 함께 그들은 시간 동안 가는 비스듬한 유지할 수 있습니다.

### Cross-Expiry 상호 작용

expiration 날짜의 상호 작용은 특히 0DTE gamma가 헤드 라인 대화를 지배 할 때 중요합니다. 같은 일 옵션도 큰 감마 스윙과 함께 intraday 범위를 구동, 더 긴 vanna 노출은 0DTE 감마 맵에서만 보이지 않는 vol 압축 동안 배경 구매 흐름을 추가합니다. vol spikes에서는, 동일한 더 긴 dated vanna 플립은 흐름을 판매하기 위하여, 단기 감마 노출 지원이 출석한지 overriding.

가득 차있는 expiration 표면을 추적해서, 다만 정면 날짜는, 어디에서 상인 rebalancing 교류가 지적하는의 더 완전한 그림을 줍니다.

Heatseeker에서 이것을 보십시오

Heatseeker의 expirations를 통해 GEX/VEX 포지셔닝과 어떻게 작용하는지 추적하십시오.

[Heatseeker 사용](https://www.skylit.ai/#pricing)

## 키 속성

- 시간, 보유 가격 및 변동을 가진 델타 변화 측정
- OTM 호출 델타 가을; 델타 상승 (무거한 부정적인). Dealers는 두 경우에 rebalance
- expiry에 가까운 ATM 가까이에 가장 강한; 깊은 파업 및 장시간 선택권을 위해 negligible
- 가격이나 vol 이동이 필요없는 딜러 헤지 intraday를 이동
- 낮은 VIX 세션에서 vanna와 결합하여 피크 노출 파업을 통해 느린 오후를 생산합니다.

## 자주 묻는 질문

### 옵션 거래의 매력은 무엇입니까?

매력은 시간 패스로 옵션의 델타 변경 사항, 가격 및 불쾌한 변동을 측정합니다. delta가 각 통과 시간으로 이동하기 때문에, delta-hedging 딜러는 지속적으로 그 재고 위치를 반향하지 않을 때. 이 시간 구동 리밸런싱은 즉시 흐름을 생산합니다. 아웃-of-the-money 통화를 위해, 델타는 expiry 접근법으로 떨어졌습니다. 를 위해, delta는 더 적은 부정적인 됩니다. 두 경우에 상인은 그들의 쐐기를 조정하고, 그 조정은 체계적인 구매를 창조하거나 underlying에 있는 압력을 판매합니다.

### 주식 시장에서 오후 드립은 무엇입니까?

낮은 VIX 요법에서, 매력은 세션의 마지막 시간에 볼 수있는 느린, 연삭 가격 행동의 기본 드라이버 중 하나입니다. 무역의 날 진행으로, 더 많은 시간 가치는 감퇴되고 더 매력 몬 rebalancing는 축적했습니다. Dealers는 레벨을 방어하거나 뉴스에 응답하지 않습니다. 그들은 더 작은 헤지 요구 사항에 대한 책을 기계적으로 조정합니다. 결과는 최대 옵션 위치와 함께 파업으로 조용히 움직여지는 가격입니다. Charm는 at-the-money 파업과 expiration에 가깝습니다, 그래서 그 효과는 근처에 주간 expiry와 함께 일에 집중합니다.

### 매력과 vanna는 어떻게 함께 작동합니까?

매력과 vanna는 모두 침묵하고, 상인 교류의 촉매 자유로운 근원입니다. Charm는 시간이 지남에 따라 순수하게 작동합니다. delta는 어떤 가격이나 vol와 관계없이 expiry 접근법으로 이동합니다. Vanna는 불쾌한 휘발성을 통해 운영합니다: IV 압축으로 델타 교대 또는 확장. IV가 시간이 통과하는 동안 낮은 편도 세션에서, 둘 다 동일한 방향으로 밀어. 각 메커니즘은 개별적으로 겸손하지만, 그들은 전체 세션에 대한 합성을 유지할 수 있습니다. 두 힘을 인식하는 상인은 동시에 테이프가 명백한 뉴스 또는 순서 교류 촉매 없이 조차 판매하기 위하여 불완전하게 느낄 수 있다는 것을 이해합니다.

### Smarter 거래 시작

Skylit의 딜러 노출 도구를 사용하여 이러한 개념을보십시오.

[접속하다](https://www.skylit.ai/#pricing)[Heatseeker 사용](https://www.skylit.ai/#pricing)
