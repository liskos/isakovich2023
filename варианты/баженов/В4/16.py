import functools
@functools.lru_cache(None)
def f(n):
    if n <= 2:
        return 0
    if n > 2 and n % 2 == 0:
        return 3 * n * n + 2 * n - 16
    if n > 2 and n % 2 != 0:
        return f(n - 2) + f(n - 3) + f(n - 4)
for i in range(5010): f(i)
print(f(5001) - f(4999) - f(4997))