def f(a, b, c):
    return hex(a)[2:3] == '0' or hex(b)[2:3] == '0' or hex(c)[2:3] == '0'

a = [int(x) for x in open('17data/17-7.txt')]
c = []
for i in range(len(a) - 2):
    if :
        c.append(a[i] + a[i+1] + a[i+2])
print(len(c), max(c))