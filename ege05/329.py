def f(n):
    b = bin(n)[2:]
    if n % 3 == 0:
        b = b + '010'
    else:
        b = b + bin(n % 3 * 5)[2:]
    return int(b, 2)


for i in range(1, 1000):
    if f(i) > 300:
        print(i)
        print(f(i))
