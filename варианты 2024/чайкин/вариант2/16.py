def f(n):
    s = "*"
    if n > 1:
        s += f(n-2)
        s += f(n // 2)
        s += "*"
    s += "*"
    return s

print(f(127).count("*"))
