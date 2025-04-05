def p(n):
    a = []
    while n > 0:
        a.append(n % 5)
        n = n // 5
    return a
a = []
for x in range(1, 2006):
    r = 5 ** 150 + 5 ** 98 - x
    a.append([str(p(r)).count('0'), x])
print(max(a))
