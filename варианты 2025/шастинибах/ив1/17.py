a = [int(x) for x in open('17.txt')]

sr = sum(a) / len(a)

c = []
for i in range(len(a) - 1):
    if abs(a[i] + a[i+1]) > sr:
        c.append(a[i] + a[i + 1])
print(len(c), abs(min(c)))