def f(n):
    a = []
    while n > 0:
        a.append(str(n % 7))
        n = n // 7
    return ''.join(a)[::-1]


for x in range(1, 2300):
    r = 7 ** 350 + 7 ** 150 - x
    if f(r).count('0') == 200:
        print(x)