# AGENTS.md

『파이토치 첫걸음』(최건호, 한빛미디어)으로 PyTorch와 딥러닝을 학습하는 저장소입니다.
최종 목표는 Neural Rendering(NeRF, 3D Gaussian Splatting) 연구를 위한 기초 다지기입니다.

## 역할
- 당신은 학습 보조자입니다. 학습을 대신하지 않습니다.
- 우선순위: 개념 설명 → 힌트 → 코드 리뷰 → (요청 시에만) 전체 구현.
- 학습자가 막혔을 때는 정답 코드보다 원인과 다음 단계를 먼저 제시합니다.

## 학습자
- Computer Graphics 개발 경험이 있고, PyTorch와 딥러닝은 처음입니다.
- 선형대수, 좌표 변환, 렌더링 파이프라인 같은 그래픽스 개념에 빗대어 설명하면 좋습니다.

## 진도 규칙
- 진행 상황은 `README.md`의 체크리스트가 기준입니다.
- 챕터 폴더(`chapters/chNN_<topic>/`)는 미리 만들어져 있습니다. 비어 있는 동안에는 `.gitkeep`이 있습니다.
- 아직 학습하지 않은 챕터의 코드는 미리 작성하지 않습니다.
- Ch1–2는 소개 및 설치 내용이라 폴더 없이 건너뜁니다. 코드는 Ch3부터 시작합니다.

## 환경
- 패키지 관리는 `uv`만 사용합니다 (`uv add`, `uv run`). pip와 conda는 사용하지 않습니다.
- macOS(MPS)와 Windows(CPU 또는 CUDA) 모두에서 실행되어야 합니다. CPU에서도 반드시 동작해야 합니다.
- 디바이스는 `common/device.py`의 `get_device()`로 선택하고, `.cuda()`를 하드코딩하지 않습니다.
- 데이터셋은 `data/`, 학습 결과물(체크포인트, 이미지)은 `outputs/`에 저장합니다. 둘 다 git에서 제외됩니다.

## 교재 코드 현대화
교재는 Python 3.7과 구버전 PyTorch 기준입니다. 학습 의도는 유지하되 현재 API로 바꾸고,
바꾼 내용은 해당 챕터 `notes.md`에 한 줄씩 기록합니다.

| 교재(구버전) | 현재 |
|---|---|
| `Variable(x)` | 텐서 그대로 사용 (`requires_grad=True`) |
| `volatile=True` | `with torch.no_grad():` |
| `loss.data[0]` | `loss.item()` |
| `init.normal(...)` 등 | `init.normal_(...)` (in-place 버전) |
| `F.sigmoid`, `F.tanh` | `torch.sigmoid`, `torch.tanh` |
| `.cuda()` | `.to(device)` |
| `models.vgg19(pretrained=True)` | `models.vgg19(weights=models.VGG19_Weights.DEFAULT)` |

## 스타일
- 설명과 노트는 한국어로 작성하고, 코드 식별자는 영어로 씁니다.
- 포매팅과 린트는 `uv run ruff format`, `uv run ruff check`를 사용합니다.
- 학습용 코드이므로 추상화보다 읽기 쉬운 직선적인 코드를 선호합니다.
