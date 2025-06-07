def prime(n):
    a = [True] * n
    a[0] = False
    a[1] = False
    for i in range(2, n):
        for j in range(i**2, n, i):
            a[j] = False
    b = [i for i in range(n) if a[i]]
    return b
k = 0
p = prime(100000)
for i in range(456789+1, 10**10):
    b = [x for x in p if i % x == 0]
    b.sort()
    smi = sum(b[:2])
    sma = sum(b[-2:])
    if (smi + sma) % 114 == 39 and len(b) >= 4:
        print(i, smi + sma)
        k+=1
        if k == 5:
            break