

for x in range(1, 17):
    r = int('19061', 12) + (x * 12 ** 2) + int('33930', 17) + (x * 17 ** 0)
    d = int('60005', 15) + (x * 15 ** 2)
    if r == d:
        print(d)