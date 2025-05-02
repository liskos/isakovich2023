for a in range(100):
    if all(not((x & 52 != 0) and (x & 48 == 0)) or not(x & a == 0) for x in range(2500)):
        print(a)
        break