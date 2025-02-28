a = []
for i in range(57888, 74556):
    s = str(i)
    for j in range(10):
        s = s.replace(str(j), str(j % 2))
    if i % 7 != 0  and i % 9 != 0 and i % 13 != 0 and s == '11000':
        a.append(i)
print(len(a), max(a) - min(a))