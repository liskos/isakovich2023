

a = [int(x) for x in open('17data/17-324.txt')]
sr = sum([x for x in a if x % 37 > 0]) // len([x for x in a if x % 37 > 0])
c = []
for i in range(len(a) - 2):
    if (bin(a[i] + a[i+1] + a[i+2])[2:] == bin(a[i] + a[i+1] + a[i+2])[2::-1]) and (min(a[i], a[i+1], a[i+2]) > sr):
        c.append(a[i] + a[i+1] + a[i+2])
print(len(c), max(c))