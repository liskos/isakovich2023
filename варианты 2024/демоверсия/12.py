def f(n):
    while '52' in n or '2222' in n or '1122' in n:
        if '52' in n:
            n = n.replace('52', '11', 1)
        if '2222' in n:
            n = n.replace('2222', '5', 1)
        if '1122' in n:
            n = n.replace('1122', '25', 1)
    return n


a = []
for i in range(4, 10000):
    s = "5" + i * "2"
    if sum(map(int, f(s))) == 64:
      a.append(i)

print(max(a))