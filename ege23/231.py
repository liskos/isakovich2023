def f(a, b):
    if a > b:
        return 0
    if a == b:
        return 1
    return f(a + 3, b) + f(a * 5, b)
print(f(1, 362))