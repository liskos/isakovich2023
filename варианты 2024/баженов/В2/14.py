n = 17 * 1331 ** 166 - 5 * 121 ** 20 - 3 * 11 ** 77 + 1334
a = []
while n > 0:
    a.append(n % 11)
    n = n // 11
print(sum(a))