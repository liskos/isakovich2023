def f(n):
    a = set()
    while n > 0:
        a.add(n % 17)
        n = n // 17
    b = [x for x in a if x % 2 == 0]
    return len(b)


r = 3 * 17 ** 777 + 15 * 17 ** 250 - 6 * 17 ** 100 + 2
print(f(r))