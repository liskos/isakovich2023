def f(a):
    return not(a % 3 == 0 and a // 3 % 3 == 0) and sum(map(int, str(a))) % 5 == 0


a = [int(x) for x in open('17data/17-4.txt')]
c = []
for i in range(len(a)):
    if f(a[i]):
        c.append(a[i])
print(len(c), max(c))