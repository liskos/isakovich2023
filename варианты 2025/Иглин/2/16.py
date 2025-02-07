def f(n):
    if n > 999:
        return n
    else:
        return 10 + n ** 2 + f(n + 4)

print(f(1111) + f(222))