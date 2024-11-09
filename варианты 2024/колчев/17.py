a = [int(x) for x in open('17.txt')]
c = []
ma = min([x for x in a if x % 10 == 8])
for i in range(len(a) - 1):
    if (a[i] % 16 == ma and not(a[i+1] % 16 == ma)) or (not(a[i] % 16 == ma) and (a[i+1] % 16 == ma)):
        c.append(a[i]+a[i+1])
print(len(c), max(c))