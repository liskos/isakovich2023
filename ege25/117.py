def prime_number(n):
    a = [True] * n
    a[0] = False
    a[1] = False
    for i in range(2, n):
        for j in range(i ** 2, n, i):
            a[j] = False
    b = [i for i in range(n) if a[i]]
    return b

def prime3(x):
    prime1 = [p for p in prime if p < 193]
    for i in prime1:
        if x % i == 0:
            prime2 = [p for p in prime if p > i]
            for j in prime2:
                if x // i % j == 0 and x // i // j in prime and x // i // j > j:
                    return True
    return False



prime = prime_number(37000)
d = []
for i in range(105673, 220784 + 1):
    if prime3(i):
        d.append(i)
print(len(d), max(d))