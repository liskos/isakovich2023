def f(a, b, c, d, g):
    if a > b:
        return 0
    if a == b:
        return 1
    if c == "*":
        return f(a * 2, b, c,'+', g) + f(a + 3, b,c, d, '-' )
    if d == '+':
        return f(a + 1, b, '*') + f(a + 3,b,c,d, '-' )
    if g == '-':
        return f(a + 1, b,'*') + f(a * 2, b,c, '+', g)
    else:
        return f(a + 1, b,'*', d, g) + f(a * 2, b,c, '+', d, g) + f(a + 3, b,)
print(f(5001, 45789, '','',''))