# option101 — Options Trading Knowledge Base

개인 학습용 옵션 거래 지식 저장소입니다.

## Skylit 학습 문서 원문 보관

- 원본: https://www.skylit.ai/learn
- 보관 위치: [docs/skylit](docs/skylit)
- 아카이브 목차: [docs/skylit/INDEX.md](docs/skylit/INDEX.md) (수집 실행 후 생성)
- 실행 기록: [GitHub Actions](https://github.com/holelectron/option101/actions/workflows/archive-skylit.yml)

[Archive Skylit Learn](https://github.com/holelectron/option101/actions/workflows/archive-skylit.yml) 워크플로는 사이트의 개별 학습 문서를 찾아 원본 HTML과 Markdown으로 저장하고, `manifest.json`에 성공/실패 목록을 기록합니다.

수동 실행: **Actions → Archive Skylit Learn → Run workflow**.

로컬 실행:

```bash
python -m pip install -r requirements.txt
python scripts/sync_skylit.py
```

사이트 연결, 렌더링 방식, 접근 제한, GitHub Actions 권한 설정에 따라 수집이 실패할 수 있습니다. `docs/skylit/manifest.json`과 Actions 로그를 확인하세요. 자동 수집 성공 전에는 문서 원문이 저장소에 존재하지 않습니다.

## 옵션 거래 학습

[OPTIONS_STUDY.md](OPTIONS_STUDY.md) — 옵션 기초, Greeks, 변동성, GEX/VEX, 옵션 플로우, 전략, 리스크 관리 및 백테스트를 체계적으로 정리할 목차입니다.

원본 Skylit 문서와 독립적으로 작성한 학습 노트를 분리해 관리합니다.

> 교육·연구 목적의 자료이며 투자 권유가 아닙니다. 원문 복제는 권한이 허용한 범위에서만 사용하세요.
