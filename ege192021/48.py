def f(x):
    a = [x + 1, x * 2, x * 3]
    b = [i for i in a if i % 2 > 0]
    return a

a = [' '] * 200
for i in range(200):
    if i >= 43:
        a[i] = '0'
for i in range(200):
    if a[i] == ' ' and any(a[x] == '0' for x in f(i)):
        a[i] = '1'
for i in range(200):
    if a[i] == ' ' and all(a[x] == '1' for x in f(i)):
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