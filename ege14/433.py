def f(n):
    a = []
    while n > 0:
        a.append(n%5)
        n = n // 5
    return a


print(f(7 * 5 ** 123 + 6 * 5 ** 111 - 5 * 25 ** 50 + 4 * 125 ** 30 - 3 * 5 ** 10).count(4))