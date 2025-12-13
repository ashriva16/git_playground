from functools import wraps

import torch
from torch.profiler import profile


# Torch profiler
def torch_profile_decorator(logger_dir):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            with profile(
                schedule=torch.profiler.schedule(wait=1, warmup=1, active=3),
                on_trace_ready=torch.profiler.tensorboard_trace_handler(logger_dir),
                record_shapes=True,
                with_stack=True,
                profile_memory=True,
                use_cuda=True,
                with_profiler=True,
                with_flops=True,
            ) as _:
                result = func(*args, **kwargs)
            return result

        return wrapper
