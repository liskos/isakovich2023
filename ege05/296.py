def f(n):
    s1 = 0
    s2 = 0
    for i in str(n)[::2]:
        x = int(i)*2
        if x > 9:
            s1 += x % 10 + x // 10
        else:
            s1 += x
    for i in str(n)[1::2]:
        s2 += int(i)
    if (s1 + s2) % 10 == 0:
        return True
    else:
        return False



print(f(4096830803098323))
for i in range(1234567891011121, 1234567891011121+10000000):
    if f(i):
        print(i % 10**8)
        break