# option101 한국어 번역 완료 현황

**2026-11-08 기준: Skylit Learn 45개 문서의 문맥 기반 한국어 재번역 완료.**

| 구분 | 완료 / 전체 |
| --- | --- |
| Academy | 12 / 12 |
| Greeks | 8 / 8 |
| Heatseeker | 7 / 7 |
| Flowseeker | 6 / 6 |
| Tools | 12 / 12 |
| **합계** | **45 / 45** |

영어 원문 Markdown과 HTML은 그대로 유지하고, 각 문서에 별도의 `*.ko.md` 번역본을 작성했습니다. 번역은 ChatGPT에서 직접 작성한 후 GitHub에 커밋했으며 **OpenAI API 키나 GitHub의 유료 API 번역 실행은 필요하지 않았습니다.**

## 검수와 자료 성격

- [금융 용어집](TRANSLATION_GLOSSARY.md)의 용어를 바탕으로 자연스러운 한국어로 작성했습니다.
- 원문 장·절, 표, 숫자, 링크, 사례 및 금융 모델의 단서를 비교했습니다.
- 업체·요금·기능·평점·연구 결과에 관한 내용은 원문 작성 시점의 주장입니다. 최신 사실 및 독립 검증을 의미하지 않습니다.
- [기존 자동 검토 파일](docs/skylit/manual_translation_review.json)은 생성 시점의 기록이므로 지금의 최종 상태와 다를 수 있습니다.
- **전체 문서는 AI 재번역본이며 전문 번역사·금융 자격자의 독립 감수 완료를 의미하지 않습니다.** 중요한 거래 판단에는 영어 원문과 현재 공급업체 자료를 확인하세요.

## 보존 및 실행

- [한국어 전체 목차](docs/skylit/KO_INDEX.md)
- [영어 원문 목차](docs/skylit/INDEX.md)
- [VitePress 한국어 홈페이지](https://holelectron.github.io/option101/ko/)
- 기존 `scripts/translate_skylit.py`는 이미 존재하는 `*.ko.md` 파일을 덮어쓰지 않도록 수정했습니다.
- `.github/workflows/translate-skylit-gpt.yml`은 **선택적인 추가 재번역 자동화**이며 실행하려면 별도의 OpenAI API 키와 비용이 필요합니다. 현재 45개 문서를 보는 데 사용할 필요는 없습니다.
- GitHub Pages 배포는 `.github/workflows/deploy-pages.yml`에서 수행합니다.

자료는 학습용이며 투자 권유가 아닙니다.
