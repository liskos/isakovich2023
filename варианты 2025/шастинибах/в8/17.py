a = [int(x) for x in open('17.txt')]

k = len([x for x in a if abs(x) % 10 == 7])
c = []

for i in range(len(a) - 1):
    if ((((a[i] < 0) and (a[i+1] > 0)) or ((a[i+1] < 0) and (a[i] > 0)))
            and a[i] + a[i+1] < k):
        c.append(a[i] + a[i+1])
print(len(c), max(c))