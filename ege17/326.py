def f(n):
    a = []
    while n > 0:
        a.append(str(n % 5))
        n = n // 5
    return ''.join(a)[::-1]

a = [int(x) for x in open('17data/17-324.txt')]
sr = sum([x for x in a if x % 31 == 0]) // len([x for x in a if x % 31 == 0])
c = []
for i in range(len(a) - 2):
    if (str(f(a[i] + a[i+1] + a[i+2])) == str(f(a[i] + a[i+1] + a[i+2]))[::-1]) and (a[i] + a[i+1] + a[i+2]) // 3 > sr:
        c.append(a[i] + a[i+1] + a[i+2])
print(len(c), min(c))