a = [int(x) for x in open('17.txt')]
d = []
c = min([x for x in a if x > 0 and x % 10 == 4])
for i in range(len(a) - 2):
    if sum(int(x) for x in str(abs(a[i]))) + sum(int(x) for x in str(abs(a[i+1]))) + sum(int(x) for x in str(abs(a[i+2]))) == c:
        d.append(a[i] + a[i+1] + a[i+2])

print(len(d), max(d))
