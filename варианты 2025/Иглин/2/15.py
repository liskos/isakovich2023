
for a in range(1, 1000):
    if all(not(x % a == 0) or (x % 55 == 0) or not(y % 101 == 0) for y in range(1, 6000) for x in range(1, 6000)):
        print(a)
        break