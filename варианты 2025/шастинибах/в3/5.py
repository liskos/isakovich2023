def tr(n):
    t = "012"
    s = ""
    while n > 0:
        s = t[n % 3] + s
        n = n // 3
    return s

def f(n):
    b = tr(n)
    if sum(map(int, b)) % 2 == 0:
        b = '1' + b + '2'
    else:
        b = '2' + b + '0'
    return int(b, 3)

c = []
for i in range(1, 1000):
    if f(i) > 100:
        c.append(f(i))
print(min(c))