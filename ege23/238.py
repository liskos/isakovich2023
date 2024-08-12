def f(a, b):
    if a > b or '5' in str(a):
        return 0
    if a == b:
        return 1
    return f(a + 1, b) + f(a + 3, b) + f(a * 3, b)

print(f(1, 49))