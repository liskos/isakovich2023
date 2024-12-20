c = []
a = [int(x) for x in open('17.txt')]
m = max(a)
for i in range(len(a) - 1):
    if (i + i + 1 + 2) % 10 == m % 10:
        c.append(abs(a[i] + a[i+1] - (i+i+1+2)))
print(len(c), min(c))