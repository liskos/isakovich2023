import functools
@functools.lru_cache(None)
def f(a, b, c):
    if a > b or a == 12 or a == 20:
        return 0
    if a == b:
        return 1
    if c == '**':
        return f(a + 1, b, '+') + f(a + 2, b, '-')
    else:
        return f(a + 1, b, '-') + f(a + 2, b, '+') + f(a * 3, b, '**')

print(f(2, 15, '') * f(15,30,'') * f(30, 38, ''))