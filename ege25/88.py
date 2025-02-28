def f(n):
    a = []
    while n > 0:
        a.append(str(n % 11))
        n = n // 11
    return ''.join(a)



for i in range(2031, 14313):
    if '2' not in f(i):
        print(i)


