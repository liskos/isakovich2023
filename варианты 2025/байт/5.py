def p(n):
    a = []
    while n > 0:
        a.append(str(n%5))
        n = n // 5
    return ''.join(a)[::-1]

def d(n):
    k = 0
    while n > 0:
        k += n % 10
        n = n // 10
    return k
def f(n):
    b = p(n)
    if n % 5 == 0:
        b = b[0] + b + b[-1]
    else:
        b = b + p(d(int(b)))
    return int(b, 5)


for i in range(50, 100):
    if f(i) % 5 == 0:
        print(f(i))