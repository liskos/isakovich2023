def f(n):
    s = bin(n)[2:-2]
    return int(s, 2)

k = set()
for i in range(20, 601):
    k.add(f(i))
print(len(k))