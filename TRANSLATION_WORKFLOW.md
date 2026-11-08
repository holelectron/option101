# 한국어 번역 고도화: 42개 문서 실행 안내

## 현재 상태

- 영어 원문 45개 보존
- Options Greeks, Gamma Exposure, Dealer Positioning의 한국어 번역 3개는 문맥 중심으로 수동 개선 완료
- 나머지 42개는 기존 Argos 자동 번역 초안 상태
- GPT 일괄 번역 스크립트와 용어집 준비 완료. **아직 실행되지 않았음**

## 일괄 번역 실행

1. GitHub 저장소의 **Settings → Secrets and variables → Actions → New repository secret**에서 이름 `OPENAI_API_KEY`로 본인 OpenAI API 키를 저장합니다.
2. [Improve Korean Translations (GPT)](https://github.com/holelectron/option101/actions/workflows/translate-skylit-gpt.yml) → **Run workflow**를 누릅니다.
3. 우선 `limit=1`로 시험하고, 성공·비용·번역 품질을 확인한 다음 `limit=0`으로 나머지 42개를 실행합니다.
4. 각 문서는 모든 섹션을 번역한 후 링크/제목/표 개수 등을 검증합니다. 실패한 문서는 기존 파일을 유지하고 결과를 `docs/skylit/translation_quality_report.json`에 기록합니다.
5. 커밋되면 VitePress 배포 워크플로가 변경된 한국어 페이지를 재빌드합니다.

### 모델과 비용

- 기본값: `gpt-6.1-sol` (GitHub Actions workflow 환경 변수에서 변경 가능)
- OpenAI API는 ChatGPT 구독과 별도로 사용량에 따라 과금됩니다.
- 처음에는 1개 문서로 토큰 사용량·비용과 품질을 확인하세요.
- API 키를 이 저장소에 평문 파일로 올리거나 채팅 메시지에 붙여 넣지 마세요.

## 보존 및 검증 기준

- 영어 `.md`와 원본 `.html`은 절대 수정하지 않습니다.
- 앞서 검수한 3개 한국어 문서도 자동 번역 대상에서 제외합니다.
- 문단을 요약하지 않고 원문 전체를 번역합니다.
- 제목 구조, 표의 행 수, 하이퍼링크 URL 일치 여부를 자동 검사합니다.
- 수치 마커에 차이가 있으면 품질 보고서에 기록하고 사람이 검토해야 합니다.
- 자동 검사를 통과해도 문맥·전문성의 완전한 정확성을 보장하지는 않습니다.

## 주요 파일

- [금융 번역 용어집](TRANSLATION_GLOSSARY.md)
- [GPT 번역 스크립트](scripts/translate_skylit_gpt.py)
- [GPT 번역 워크플로](.github/workflows/translate-skylit-gpt.yml)
- [전체 한국어 문서](docs/skylit/KO_INDEX.md)

## 주의

원문에 있는 시장 해석은 원저자와 데이터 공급사의 모델에 따른 것입니다. 원문을 번역한다는 이유로 시장 메커니즘을 확정적인 투자 신호로 받아들이면 안 됩니다.