def fibonacci(n: int) -> int:
    if n == 0:
        return 0
    if n == 1:
        return 1
    if n > 4:
        return n
    return n - 1
