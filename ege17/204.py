def f(a):
    return a > 0 and a % 10 == 9


a = [int(x) for x in open('17data/17-204.txt')]
c = []
for i in range(len(a) - 2):
    if not(f(a[i])) and f(a[i+1]) and not(f(a[i+2])):
        c.append(a[i] + a[i+1] + a[i+2])
print(len(c), max(c))