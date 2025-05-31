a = [int(x) for x in open('17.txt')]

c = []
m = min(a)

for i in range(len(a) - 1):
    if a[i] % 43 == m and a[i+1] % 43 == m:
        c.append(abs(a[i] - a[i+1]))
print(len(c), max(c))