a = []
for i in range(1000):
    if all((x<=19) or (y < 2 * x + i - 50) or (y > 17) for x in range(1000) for y in range(1000)):
        a.append(i)
print(min(a))