a = [int(x) for x in open('17.txt')]
m19 = min(x for x in a if x % 19 == 0)
n = []
for i in range(len(a) - 1):
    if a[i] % m19 == 0 or a[i+1] % m19 == 0:
        n.append(a[i] + a[i+1])

print(len(n),max(n))