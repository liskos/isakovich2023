

def f(n, k):
    for i in range(2, n):
        if n % i == 0 and k == 1:
            return True
        elif n % i == 0:
            return f(n // i, k - 1)
    return False

r = 0
for k in range(1, 28):
    x = 9500000 + k
    if f(x, 3):
        r += 1
        print(k)
        if r == 5:
            break