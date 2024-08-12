import functools
@functools.lru_cache(None)
def f(a, b, c):
    if a > b or c < 0:
        return 0
    if a == b and c == 0:
        return 1
    return f(a + 3, b, c - 10) + f(a * 4, b, c - 10) + f(a * 5, b, c - 10)

print(f(1, 4400, 700))