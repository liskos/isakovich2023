def f(x):
    k = 0
    while x > 0:
        if x % 7 == 0:
            k += 1
        x = x // 7
    return k





for i in range(1, 2031):
    s = 7 ** 170 + 7 ** 100 - i
    if f(s) == 71:
        print(i)