def f(a):
    c = 0
    while a > 0:
        c += a%10
        a = a // 10
    return c
c = []

a = [int(x) for x in open('17.txt')]

k = len([x for x in a if abs(x) % 10 == 7])


for i in range(len(a) - 1):
    if ((a[i] < 0 and a[i+1] >= 0) or (a[i+1] < 0 and a[i] >= 0)) and abs(f(a[i])) + abs(f(a[i+1])) < k:
        c.append(a[i] + a[i+1])
print(len(c), max(c))