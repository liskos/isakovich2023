c = []
for a in range(1, 100):
    if all((y > 10) or (x * a > y + x) for x in range(1, 100) for y in range(1, 100)):
        c.append(a)
print(min(c))