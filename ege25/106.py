def prime_number(n):
    a = [True] * n
    a[0] = False
    a[1] = False
    for i in range(2, n):
        for j in range(i ** 2, n, i):
            a[j] = False
    b = [i for i in range(n) if a[i]]
    return b


prime = prime_number(350000)
prime1= [p for p in prime if p <  828]
d = []
for i in range(631632, 684935):
    for p in prime1:
        if i % p == 0 and i // p in prime:
            d.append([ i // p - p, i, p, i // p])
            break
m = max(d, key=lambda x:x[0])[0]
print([p for p in d if p[0] == m])