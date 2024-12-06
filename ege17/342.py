
a = [int(x) for x in open('17data/17-342.txt')]
m = min([x for x in a if x % 37 == 0])
s = max([x for x in a if x % 73 == 0])
c = []
for i in range(len(a) - 1):
    if m < a[i] < s and not(m < a[i+1] < s):
        c.append(a[i] + a[i+1])
print(len(c), min(c))