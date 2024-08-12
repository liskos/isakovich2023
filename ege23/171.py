import functools
@functools.lru_cache(None)
def f(a, b, c):
    if a > b or a == 23:
        return 0
    if a == b:
        return 1
    if c:
        return f(a + 2, b, False) + f(a * 2, b, False)
    else:
        return f(a + 1, b, True) + f(a + 2, b, False) + f(a * 2, b, False)

print(f(3, 11, False) * f(11, 79, False))