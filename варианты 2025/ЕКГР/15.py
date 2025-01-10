c = []
for a in range(1, 1000):
    if (all((x - 3 * y < a) or (y > 400) or (x > 56)) for x in (1, 1000) for y in (1, 1000)):
        print(a)
