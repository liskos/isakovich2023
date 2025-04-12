for a in range(100):
    if all((5 < y) or (x > 32) or (x + 2 * y < a) for x in range(30, 100) for y in range(6)):
        print(a)