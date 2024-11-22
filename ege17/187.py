def f(a, b, c):
    return bin(a)[2:].count('1') == 3 and bin(b)[2:].count('1') == 3 and bin(c)[2:].count('1') == 3


a = [int(x) for x in open('17data/17-6.txt')]
c = []
for i in range(len(a) - 2):
    if f(a[i], a[i+1], a[i+2]):
        c.append(a[i] + a[i+1] + a[i+3])
print(len(c), max(c))