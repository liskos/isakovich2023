def f(n):
    a = []
    while n > 0:
        a.append(str(n % 5))
        n = n // 5
    return ''.join(a)[::-1]

for i in range(1001):
    r = f(5 ** 50 - i)
    if str(r).count('4') == 47:
        print(i)