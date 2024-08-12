import functools
@functools.lru_cache(None)
def f(a, b, c):
    if a > b or c <= 0:
        return 0
    if a == b:
        return 1
    return f(a + 3, b, c - len(str(a))) + f(a * 4, b, c - len(str(a))) + f(a * 5, b, c - len(str(a)))

print(f(1, 5500, 1000))