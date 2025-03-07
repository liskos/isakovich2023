def prime_number(n):
    a = [True] * n
    a[0] = False
    a[1] = False
    for i in range(2, n):
        for j in range(i ** 2, n, i):
            a[j] = False
    b = [i for i in range(n) if a[i]]
    return b


prime = prime_number(200000)
prime1= [p for p in prime if p <  700]
d = []
for i in range(298435, 363249 + 1):
    for p in prime1:
        if i % p == 0 and i // p in prime and p < i // p:
            d.append(i)
            break
sr = sum(d) / len(d)
h = [[abs(x - sr), x] for x in d]
m = min(h, key=lambda x:x[0])[1]
print(len(d), m)