for a in range(1000):
    if all(not(((x & 117) != 0) and (x & 91) == 0) or not((x & a) == 0) for x in range(1000)):
        print(a)