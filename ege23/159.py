def fi(c):
    n1 = 0
    n2 = 1
    n3 = 0
    while n3 < c:
        n3 = n1 + n2
        n1 = n2
        n2 = n3
    return n1

def f(a, b):
    if a > b:
        return 0
    if a == b:
        return 1
    return f(a + 1, b) + f(a + 4, b) + f(a + fi(a), b)

print(f(2, 16))