a = []
for i in range(1000):
    if all((x + y <= 24) or (y <= x - 2) or (y >= i)for x in range(1000) for y in range(1000)):
        a.append(i)
print(max(a))