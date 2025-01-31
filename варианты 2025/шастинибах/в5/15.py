c = []
for a in range(1, 100):
    if all(not(not(x % 10 == 5) and (x % 10 == 4)) or (x > a - 11) for x in range(1, 100)):
        print(a)
