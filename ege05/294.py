def f(n):
    if n % 2 == 0:
        n = list(str(n))
        n.sort(reverse=True)
        n = ''.join(n)
        n = int(n) // 2
    else:
        n = sorted(list(str(n)))
        n = "".join(n)
        n = int(n) * 2
    return n


a = []
for i in range(1000, 10000):
    if f(i) == i + 1:
        a.append(f(i))
print(min(a))
