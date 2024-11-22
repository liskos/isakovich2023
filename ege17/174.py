def f(a):
    return a > 100 and 7 >= (a // 100) >= 3 and (a % 100 // 10) <= 4


a = [int(x) for x in open('17data/17-4.txt')]
c = []
for i in range(len(a)):
    if f(a[i]):
        c.append(a[i])
print(len(c), min(c))