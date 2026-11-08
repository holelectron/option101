# option101 · Options Trading Knowledge Hub

**VitePress 기반 옵션 거래 학습 라이브러리** — Skylit Learn 45개 문서, 영어 원문과 한국어 번역을 카테고리별로 탐색합니다.

## 📚 [START HERE — 문서 전체 목차](START_HERE.md)

- [영어 원문 전체 목차](docs/skylit/INDEX.md)
- [한국어 번역 목차](docs/skylit/KO_INDEX.md) (번역 작업 완료 후 생성)
- [옵션 학습 로드맵](OPTIONS_STUDY.md)
- [Skylit 원문 수집 결과](docs/skylit/manifest.json)

## 🖥️ VitePress 문서 사이트

로컬 미리보기:

```bash
npm install
npm run docs:dev
```

프로덕션 빌드와 미리보기:

```bash
npm run docs:build
npm run docs:preview
```

- 홈: `docs/index.md` (영문), `docs/ko/index.md` (한국어)
- VitePress 설정: `docs/.vitepress/config.mts`
- 시각 디자인: `docs/.vitepress/theme/custom.css`
- 자동 빌드: [Validate VitePress Site](https://github.com/holelectron/option101/actions/workflows/vitepress-build.yml)
- 사이트 빌드 ZIP: 성공한 Actions 실행의 **Artifacts**에서 `option101-vitepress-site` 다운로드

사이트 빌드는 `scripts/prepare-site.mjs`가 번역본을 `docs/ko/skylit` 아래에 복사한 뒤 실행합니다. 아직 번역되지 않은 문서는 영어 원문 링크를 가진 안내 페이지로 표시합니다. 생성된 경로는 소스 번역 파일(`*.ko.md`)과 별개입니다.

### 🔒 공개 범위

원문이 포함된 **Private** 저장소를 외부에 게시하지 않도록 GitHub Pages 자동 배포는 설정하지 않았습니다. GitHub Actions에서 사이트 빌드와 비공개 아티팩트만 생성합니다. Pages 또는 외부 호스팅을 활성화하면 원문이 외부에 공개될 수 있습니다.

## 번역 및 원문

- 영어 HTML과 Markdown은 `docs/skylit/<category>/`에 보관
- 한국어 자동 번역 초안은 `*.ko.md`로 보관
- [한국어 번역 워크플로](https://github.com/holelectron/option101/actions/workflows/translate-skylit.yml)

> 자동 번역의 전문 용어와 숫자는 영어 원문을 대조해야 합니다. 자료는 학습용이며 투자 권유가 아닙니다.

## 한국어 번역 품질 개선

- [금융 용어집 및 한국어 스타일 기준](TRANSLATION_GLOSSARY.md)
- [나머지 42개 문서 GPT 재번역 안내](TRANSLATION_WORKFLOW.md)

기존 고품질 번역 3개는 보호하며, 다른 42개는 사용자가 API 키를 Actions Secret으로 등록한 후 수동으로 실행할 수 있습니다. 번역은 API 사용량에 따라 비용이 발생합니다.
