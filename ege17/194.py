def f(n):
    return bin(n).count('1') == 2 and bin(n).count('0') > 0

a = [int(x) for x in open('17data/17-9.txt')]
c = []
for i in range(len(a) - 2):
    if f(a[i]) and not(f(a[i+1])) or f(a[i+2]):
        c.append(a[i] + a[i+1] + a[i+2])
print(len(c), max(c))