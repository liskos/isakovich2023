def sem(n):
    t = "0123456"
    s = ""
    while n > 0:
        s = t[n % 7] + s
        n = n // 7
    return s
def che(n):
    t = '0123'
    s = ''
    while n > 0:
        s = t[n % 4] + s
        n = n // 4
    return s

def f(n):
    b = sem(n)
    b = int(b, 10)
    b = che(b)
    if int(b, 4) % 2 == 0:
        b = b + '00'
    else:
        b = b + '32'
    return int(b, 4)

a = []
for i in range(1, 10000):
    if f(i) <= 6560:
        a.append(i)
print(sum(a))
