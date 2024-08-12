import functools
@functools.lru_cache(None)
def f(a, b, c):
    if a > b or a == 20 or a == 58:
        return 0
    if a == b:
        return c <= 6
    return f(a + 1, b, c + 1) + f(a + 3, b, c) + f(a * 3, b, c)

print(f(3, 37, 0) * f(37, 95, 0))