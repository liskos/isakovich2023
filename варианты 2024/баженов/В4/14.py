a = []
for x in range(17):
    n = int('9a501', 17) + (x * 17 ** 1) + int('4gb20', 17) + x + x * 17 ** 3 + int('2080d', 17) + x * 17 ** 1
    if n % 11 == 0:
        a.append(n // 11)
print(max(a))