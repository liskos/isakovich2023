for a in range(1, 1000):
    if all((x % a == 0) or (not(x in range(60, 81)) or not(x % 22 == 0)) for x in range(1, 1000)):
        print(a)