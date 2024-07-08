c = []
a = [int(x) for x in open('17.txt')]
b = max([x for x in a if 10 <= x <= 99])
for i in range(len(a) - 1):
    if ((abs(a[i]) % 10 == 4) != (abs(a[i+1]) % 10 == 4)) and a[i] + a[i + 1] <= b:
        c.append(a[i] + a[i+1])
print(len(c), max(c))
