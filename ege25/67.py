a = []
for i in range(33333, 55556):
    s = str(i)
    for j in range(10):
        s = s.replace(str(j), str(j % 2))
    if i % 6 != 0  and i % 8 != 0 and i % 7 != 0 and s == '11010':
        a.append(i)
print(len(a), max(a) - min(a))