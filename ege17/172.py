def f(a):
    return bin(a)[-4:] == '1001' and a % 5 == 1 and a // 5 % 5 == 1


a = [int(x) for x in open('17data/17-4.txt')]
c = []
for i in range(len(a)):
    if f(a[i]):
        c.append(a[i])
print(sum(c), max(c))