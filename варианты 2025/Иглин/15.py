c = []
for a in range(1, 100):
    if all(not(x % a == 0) or (not(not(x % 55 == 0))) or not(y % 101 == 0) for y in range(1, 100) for x in range(1, 100)):
        c.append(a)
print(min(c))