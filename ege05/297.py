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
    return s1 + s2



print(f(4096830803098323))
for i in range(10**15, 10**16):
    if f(i) == 30:
        print(i % 10**8)
        break