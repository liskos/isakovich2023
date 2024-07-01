import functools

@functools.lru_cache(None)

def f(n):
    if n < 3:
        return n + 1
    if n >= 3 and n % 2 == 1:
        return 3 * f(n - 1) + 17
    if n >= 3 and n % 2 == 0:
        return f(n - 3) + 4 * n



k = 0
for i in range(4, 1000):
    if f(i) < 8000:
        k += 1
print(k)