def f(n):
    b = hex(n)[2:]
    if n % 2 == 0:
        b = b + "f"
    else:
        b = b + '0'
    b = b + hex(sum(int(x, 16) for x in b) % 16)[2:]
    b = b + hex(sum(int(x, 16) for x in b) % 16)[2:]
    z = [b.count(x) for x in b]
    return max(list(z))  == min(list(z)) * 5


for i in range(1, 10000):
    if f(i):
        print(i)
        break



