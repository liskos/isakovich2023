
a = []
for x in range(1, 13):
        r = (int('5370623', 13) + (x * 13 ** 3)) - (int('603502', 13) + (x * 13 ** 1) + (x * 13 ** 4))
        if r % 3 == 0:
            a.append(x)
print(max(a))