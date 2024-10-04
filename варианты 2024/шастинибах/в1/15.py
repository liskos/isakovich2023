def f(i):
    for x in range(1000):
        for y in range(1000):
            ff = (x<=19) or (y < 2 * x + i - 50) or (y > 17)
            if not ff:
                return False
    return True


for i in range(1000):
    if f(i):
        print(i)
        break
