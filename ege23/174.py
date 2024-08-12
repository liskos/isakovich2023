import functools
@functools.lru_cache(None)
def f(a, b, c):
    if a > b or a == 30 or a == 40:
        return 0
    if a == b:
        return 1
    if c == '**':
        return f(a + 1, b, '+') + f(a + 3, b, '-')
    else:
        return f(a + 1, b, '-') + f(a + 3, b, '+') + f(a * 2, b, '**')

print(f(3, 20, '') * f(20, 60, ''))