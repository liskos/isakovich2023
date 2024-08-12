import functools
@functools.lru_cache(None)
def f(a, b, c):
    if a > b or a == 23:
        return 0
    if a == b:
        return 1
    if c == '**':
        return f(a + 2, b, '+') + f(a * 2, b, '-')
    else:
        return f(a + 1, b, '**') + f(a + 2, b, '+') + f(a * 2, b, '-')

print(f(3, 11, '') * f(11, 79, ''))