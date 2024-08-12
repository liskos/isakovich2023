def f(x, y, x1, y1):
    if x > x1 or y > y1:
        return 0
    if x == x1 and y == y1:
        return 1
    return f(x + 1, y, x1,y1) + f(x * 2, y, x1, y1) + f(x, y + 3, x1, y1)

print(f(1, 0, 17,27))