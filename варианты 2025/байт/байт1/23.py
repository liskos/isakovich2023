def f(a, b):
    if a > b:
        return 0
    if a == b:
        return 1
    return f(a + 1, b) + f(a + 5, b) + f(a * 5, b)

print(f(3, 10) * f(10, 25))
print(f(3, 20) * f(20, 25))
print(f(3, 10) * f(10, 20) * f(20, 25))