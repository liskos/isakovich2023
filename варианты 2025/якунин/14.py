s = int('723', 8) * int('B13A', 16) - int('10011101010', 2)
a = []
while s > 0:
    a.append(s % 4)
    s //= 4
print(a.count(0))
