def f(n):
    if n % 2 == 0:
        n = list(str(n))
        n = n.sort(reverse=True)
    return n
print(f(1488))