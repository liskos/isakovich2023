def f(a, b):
    if a > b:
        return 0
    if a == b:
        return 1
    return f(a + 3, b) + f(a * 4, b) + f(a * 5, b)

def h(a, b, c):
    if a > b:
        return 0
    if a == b:
        return c == c[::-1]
    else:
        return h(a + 3, b, c + "A") + h(a * 4, b, c + "B") + h(a * 5, b, c + "C")

print(f(1, 16) * h(16, 152, '') * f(152, 725))