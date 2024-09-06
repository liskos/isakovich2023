a = []
for x in range(19):
    n = int('98897021', 19) + (x * 19 ** 2) + int('20923', 19) + (x * 19 ** 3)
    if n % 18 == 0:
        a.append(n // 18)
print(max(a))