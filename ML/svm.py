import torch

# Print the installed PyTorch version
print(f"PyTorch Version: {torch.__version__}")

# Check if a CUDA-enabled GPU is available (should be True for GPU install)
print(f"CUDA Available: {torch.cuda.is_available()}")

# Get the number of available GPUs (will be 0 for CPU install)
print(f"GPU Count: {torch.cuda.device_count()}")