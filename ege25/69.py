a = []
for i in range(64444, 77564):
    s = str(i)
    for j in range(10):
        s = s.replace(str(j), str(j % 2))
    if i % 9 != 0  and i % 13 != 0 and i % 17 != 0 and s == '00111':
        a.append(i)
print(len(a), max(a) - min(a))