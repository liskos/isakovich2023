for x in range(1, 3052):
    a = []
    r = 4 ** 151 + 7 ** 283 + 6 ** 82 - 5 * x
    while r > 0:
        a.append(r % 8)
        r //= 8
    if a.count(1) == 26:
        print(x)
        break
