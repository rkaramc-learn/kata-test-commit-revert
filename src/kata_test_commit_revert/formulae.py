import functools


@functools.lru_cache(maxsize=None)
def fibonacci(n: int) -> int:
    if n < 0:
        raise ValueError("n must be non-negative")
    if n == 0:
        return 0
    if n == 1:
        return 1
    if n > 4:
        return fibonacci(n - 1) + fibonacci(n - 2)
    return n - 1
