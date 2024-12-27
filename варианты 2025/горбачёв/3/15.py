c = []
for a in range(1, 1000):
    if all((not(x % 23 == 0) or not(x % 8 == 0)) or (x % a == 0) for x in range(1, 1000)):
        c.append(a)
print(len(c))