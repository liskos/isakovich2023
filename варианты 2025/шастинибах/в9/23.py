

def f(a, b):
    if a < b or a == 26 or a == 30:
        return 0
    if a == b:
        return 1
    return f(a - 3, b) + f((a +1)// 2, b)

print(f(69, 14))