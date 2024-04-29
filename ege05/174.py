def f(n):
    s = bin(n)[2:]
    s = s.replace("0", "")
    return int(s, 2)

k = set()
for i in range(10, 2501):
    k.add(f(i))
print(len(k))