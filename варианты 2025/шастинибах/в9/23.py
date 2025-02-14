

def f(a, b):
    if a < b and a == 26 and a == 30:
        return 0
    if a == b:
        return 1
    return f(a - 3, b) + f(a / 2 + 1, b)

print(f(69, 14))