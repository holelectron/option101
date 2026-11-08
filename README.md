# option101 · Options Trading Knowledge Hub

**VitePress 기반 옵션 거래 학습 라이브러리** — Skylit Learn 45개 문서, 영어 원문과 한국어 번역을 카테고리별로 탐색합니다.

## 📚 [START HERE — 문서 전체 목차](START_HERE.md)

- [영어 원문 전체 목차](docs/skylit/INDEX.md)
- [한국어 번역 목차](docs/skylit/KO_INDEX.md) (45개 재번역 완료)
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

사이트 빌드는 `scripts/prepare-site.mjs`가 번역본을 `docs/ko/skylit` 아래에 복사한 뒤 실행합니다. 현재 45개 문서 모두 한국어 번역 파일이 있습니다. 생성된 경로는 소스 번역 파일(`*.ko.md`)과 별개입니다.

### 사이트 공개 범위

GitHub 저장소는 Private이지만 GitHub Pages 사이트는 공개 배포합니다. [한국어 학습 사이트](https://holelectron.github.io/option101/ko/)에서 확인할 수 있습니다. 원문과 번역 자료를 웹에서 공개하므로 사용 권한 및 저작권 조건을 확인하세요.

## 번역 및 원문

- **45개 문서 전부** 문맥 기반 자연스러운 한국어로 재번역 완료(2026-11-08)
- 영어 Markdown·HTML은 `docs/skylit/<category>/`에 보존
- 한국어 파일은 동일 폴더의 `*.ko.md`에 보존
- [금융 용어집](TRANSLATION_GLOSSARY.md)
- [한국어 목차](docs/skylit/KO_INDEX.md)
- [번역 완료 현황·검수 원칙](TRANSLATION_WORKFLOW.md)

기존 Argos 자동 번역 스크립트는 기존 한국어 파일을 덮어쓰지 않습니다. 선택적인 GPT API 자동화는 별도 준비돼 있으나 **현재 번역을 열람하거나 사이트를 배포하는 데 API 키는 필요하지 않습니다.** AI 작성 번역으로, 독립적인 전문 감수를 의미하지 않습니다. 학습용 자료이며 투자 권유가 아닙니다.
