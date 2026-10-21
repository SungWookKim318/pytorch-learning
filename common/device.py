import torch


def get_device() -> torch.device:
    """CUDA → MPS → CPU 순서로 사용 가능한 디바이스를 반환합니다."""
    if torch.cuda.is_available():
        return torch.device("cuda")
    if torch.backends.mps.is_available():
        return torch.device("mps")
    return torch.device("cpu")
