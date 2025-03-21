k = 0

for x in range(100):
    r = int('13152', x) + int('7025', 100) + (x * 100 ** 2)
    if r % 11 == 0:
        k += 1
print(k)