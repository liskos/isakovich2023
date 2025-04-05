for x in range(1, 17):
    r = int('705893', 17) + (x * 17 ** 4) + int('ee039ac', 17) + (x * 17 ** 4)
    if r % 13 == 0:
        print(r // 13, x)
