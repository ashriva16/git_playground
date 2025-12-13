import shutil
import subprocess
import sys


def install_torch_according_to_hardware():
    gpu = shutil.which("nvidia-smi") is not None

    if gpu:
        print("GPU detected → installing CUDA PyTorch.")
        cmd = [sys.executable, "-m", "pip", "install", "torch", "torchvision", "torchaudio"]
    else:
        print("No GPU detected → installing CPU-only PyTorch.")
        cmd = [
            sys.executable,
            "-m",
            "pip",
            "install",
            "torch",
            "torchvision",
            "torchaudio",
            "--index-url",
            "https://download.pytorch.org/whl/cpu",
        ]

    subprocess.check_call(cmd)
