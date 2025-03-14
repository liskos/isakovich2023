def f(n):
    if n < 3:
        return n * 4
    if n >= 3 and n % 2 > 0:
        return n * 2
    if n >= 3 and n % 2 == 0:
        return 5 * f(n - 2) + n ** 2

k = 0
for n in range(1, 1000):
    if 999 >= f(n) >= 100 and f(n) % 2 == 0:
        k+=1
print(k)