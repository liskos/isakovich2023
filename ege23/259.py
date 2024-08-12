import functools
@functools.lru_cache(None)
def f(a, b):
    if a > b or a == 3000:
        return 0
    if a == b:
        return 1
    return f(a + 3, b) + f(a + 5, b) + f(a * 2, b)

@functools.lru_cache(None)
def g(a, b):
    if a > b or a == 5000:
        return 0
    if a == b:
        return 1
    return g(a + 3, b) + g(a + 5, b) + g(a * 2, b)


print(f(1, 5000) * f(5000,10000) + g(1, 3000) * g(3000, 10000))