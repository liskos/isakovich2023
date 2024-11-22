def f(n):
    return bin(n).count('1') > 5 and bin(n).count('1') % 2 > 0

a = [int(x) for x in open('17data/17-8.txt')]
c = []
for i in range(len(a) - 1):
    if f(a[i]) or f(a[i+1]):
        c.append(a[i] + a[i+1])
print(len(c), max(c))