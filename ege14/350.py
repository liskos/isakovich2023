

for x in range(14):
    r = int('33640', 11) + (x * 11 ** 0) + int('07946', 12) + (x * 12 ** 4)
    d = int('55087', 14) + (x * 14 ** 2)
    if r == d:
        print(d)