def f(n):
    s1 = sum(int(x) for x in str(n) if int(x) % 2 == 1)
    s2 = sum(map(int, str(n)[1::2]))
    return abs(s1 - s2)




print(f(1234))

for i in range(1, 10000000):
    if f(i) == 30:
        print(i)
        break