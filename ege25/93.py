def f(n):
    c = 0
    while n > 0:
        if (n % 10) % 2 > 0:
            c += n % 10
        else:
            break
    return c



for i in range(1686, 13276):
        print(f(i))

