def delit(n, m):
    return n % m == 0
b = range(50, 81)

for a in range(100):
    if all((not(x in b) or not delit(x, 7)) or (x + a >= 90) for x in range(100)):
        print(a)