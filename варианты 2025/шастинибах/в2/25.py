def s(n):
    k = 0
    for i in range(1, int(n ** 0.5) + 1):
        if n % i == 0 and i != n // i:
            k += i
            k += n // i
        elif n % i == 0:
            k += i
    return k


for i in range(1000, 10000):
    if s(i) % 100 == 23:
        print(i, s(i))