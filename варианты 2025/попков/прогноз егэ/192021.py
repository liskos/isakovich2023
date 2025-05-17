def f(x):
    if x % 2 == 0:
        a = [x - 3, x // 2]
    else:
        a = [x - 3, (x + 3) // 2]
    return a


a = [' '] * 400
for i in range(400):
    if i <= 24:
        a[i] = '0'

for i in range(400):
    if a[i] == ' ' and any(a[x] == '0' for x in f(i)):
        a[i] = '1'

for i in range(400):
    if a[i] == ' ' and all(a[x] == '1' for x in f(i)):
        a[i] = '2'
for i in range(400):
    if a[i] == ' ' and any(a[x] == '2' for x in f(i)):
        a[i] = '3'

for i in range(400):
    if a[i] == ' ' and all(a[x] in '13' for x in f(i)):
        a[i] = '4'

print([i for i in range(400) if a[i] == '1'])
print([i for i in range(400) if a[i] == '2'])
print([i for i in range(400) if a[i] == '3'])
print([i for i in range(400) if a[i] == '4'])