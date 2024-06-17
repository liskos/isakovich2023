def f(n):
    b = hex(n)[2:]
    if n % 2 == 0:
        b = b + "f"
    else:
        b = b + '0'
    b = b + hex(sum(int(x, 16) for x in b) % 16)[2:]
    b = b + hex(sum(int(x, 16) for x in b) % 16)[2:]
    return b.count(max(list(b))) == b.count(min(list(b))) * 5


for i in range(1, 1000000):
    if f(i):
        print(i)
        break



