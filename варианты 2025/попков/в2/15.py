for a in range(1, 100):
    if all(not(not(x in range(13, 20)) or (x in range(17, 25))) or not(x in range(a)) for x in range(1, 100)):
        print(a)