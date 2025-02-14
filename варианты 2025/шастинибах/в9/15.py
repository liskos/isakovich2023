for a in range(1, 1000):
    if all((a + 2 * x > 400 - a) and (a % 100 + 120 % a > 140) for x in range(1, 100)):
        print(a)