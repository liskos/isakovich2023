for i in range(8, 36):
    if (7 ** 500 - int('53', i)) % 6 == 0:
        print(i)
        break