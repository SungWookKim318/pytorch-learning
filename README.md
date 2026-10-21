# pytorch-learning

『파이토치 첫걸음』(최건호, 한빛미디어)으로 PyTorch와 딥러닝을 학습하는 저장소입니다.
최종 목표는 Computer Graphics → Neural Rendering(NeRF, 3D Gaussian Splatting)으로 이어지는 기초 다지기입니다.

## 환경 설정 (macOS / Windows 공통)

```bash
# uv 설치: https://docs.astral.sh/uv/getting-started/installation/
uv sync                 # .venv 생성 + 의존성 설치
uv run python -c "from common.device import get_device; print(get_device())"
uv run jupyter lab
```

- Python 3.12, PyTorch 최신 안정 버전 (`uv.lock`으로 고정)
- macOS는 MPS, Windows는 기본적으로 CPU를 사용합니다. Windows에서 CUDA를 쓰려면 `pyproject.toml`에 PyTorch CUDA 인덱스를 추가하세요.

## 구조

```
common/      # 챕터 간 공용 코드 (device 선택 등)
chapters/    # ch03_ ~ ch10_ : 챕터별 코드 + notes.md (Ch1–2는 읽기만)
data/        # 데이터셋 (git 제외)
outputs/     # 체크포인트, 결과 이미지 (git 제외)
```

## 진행 상황

- [ ] Ch1 딥러닝에 대하여
- [ ] Ch2 파이토치
- [ ] Ch3 선형회귀분석
- [ ] Ch4 인공 신경망
- [ ] Ch5 합성곱 신경망
- [ ] Ch6 순환 신경망
- [ ] Ch7 학습 시 생길 수 있는 문제점과 해결 방안
- [ ] Ch8 뉴럴 스타일 트랜스퍼
- [ ] Ch9 오토인코더
- [ ] Ch10 생성적 적대 신경망

## 다음 단계: Neural Rendering과의 연결

- **Ch3–4** 경사하강법, 역전파, MLP → NeRF의 MLP, 3DGS 파라미터 최적화
- **Ch5** CNN, VGG 특징 → LPIPS 등 렌더링 품질 지표
- **Ch7** 초기화, 학습률, 옵티마이저 → NeRF/3DGS 학습 튜닝
- **Ch8** 입력 이미지 자체를 최적화 → 미분 가능 렌더링과 같은 사고방식
- **Ch9–10** latent 표현, 생성 모델 → 생성형 3D
