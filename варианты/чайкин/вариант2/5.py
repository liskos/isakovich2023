def f(n):
    s = ""
    m = n
    while m > 0:
        s = str(m % 8) + s
        m = m // 8
    if sum(map(int, str(n))) % 2 == 0:
        s += str(n % 3)
    else:
        s = max(map(str, s)) + s
    return int(s, 8)


print(f(6))
print(f(5))
for i in range(1, 100000):
    if f(i) > 127:
        print(i)
        break