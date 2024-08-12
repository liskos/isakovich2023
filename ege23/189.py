def f(a, b, c):
    if a > b or a < -40 or a > 40:
        return 0
    if a == b:
        return 1
    if ((a+2) not in c) and ((a - 3) not in c):
        return f(a+2, b, c+[a+2]) + f(a - 3, b, c + [a - 3])
    if ((a+2) in c) and ((a - 3) not in c):
        return f(a - 3, b, c + [a - 3])
    if ((a+2) not in c) and ((a - 3) in c):
        return f(a+2, b, c+[a+2])
    if ((a+2) in c) and ((a - 3) in c):
        return 0

print(f(1, 30, []))