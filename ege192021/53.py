def f(x):
    a = [x - 1, x - 2, x - 3, x - 4, x - 5]
    if x % 2 == 0:
        a.append(x // 2)
    return a

a = [' '] * 200
for i in range(200):
    if i < 10:
        a[i] = '0'
for i in range(200):
    if a[i] == ' ' and any(a[x] == '0' for x in f(i)):
        a[i] = '1'
for i in range(200):
    if a[i] == ' ' and all(a[x] in '1' for x in f(i)):
        a[i] = '2'
for i in range(200):
    if a[i] == ' ' and any(a[x] == '2' for x in f(i)):
        a[i] = '3'
for i in range(200):
    if a[i] == ' ' and all(a[x] in '13' for x in f(i)):
        a[i] = '4'
print([i for i in range(200) if a[i] == '1'])
print([i for i in range(200) if a[i] == '2'])
print([i for i in range(200) if a[i] == '3'])
print([i for i in range(200) if a[i] == '4'])