a = [int(x) for x in open('17.txt')]



m = max(a)
h = []
for i in range(len(a) - 2):
    t = a[i:i+3]
    b = abs(sum([x for x in t if x < 0]))
    c = sum([x for x in t if x > 0])
    if b <= c and abs(a[i] * a[i+1] * a[i+2]) % 10 == m % 10:
        h.append(abs(a[i]) * abs(a[i+1]) * abs(a[i+2]))
print(len(h), max(h))