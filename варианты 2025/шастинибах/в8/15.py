k = 0
for a in range(1, 10000):
    if all((x % a == 0) or ((x not in range(170, 221)) or (x % 24 != 0)) for x in range(1, 10000)):
        k += 1
print(k)