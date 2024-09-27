def f(n):
    while '12' in n or '322' in n or '222' in n:
        if '12' in n:
            n = n.replace('12', '2', 1)
        if '322' in n:
            n = n.replace('322', '21', 1)
        if '222' in n:
            n = n.replace('222', '3', 1)
    return n

b = []
for i in range(3, 10000):
    b.append(sum(map(int, f('1' + i * '2'))))
print(max(b))