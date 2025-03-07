def f(x):
    a = [x + 1, x + 4, x * 2]
    return a


a = [' '] * 700
for i in range(700):
    if i >= 51:
        a[i] = '0'

for i in range(700):
    if a[i] == ' ' and any(a[x] == '0' for x in f(i)):
        a[i] = '1'
for i in range(700):
    if a[i] == ' ' and all(a[x] == '1' for x in f(i)):
        a[i] = '2'
for i in range(700):
    if a[i] == ' ' and any(a[x] in '2' for x in f(i)):
        a[i] = '3'
for i in range(700):
    if a[i] == ' ' and all(a[x] in '13' for x in f(i)):
        a[i] = '4'


print([x for x in range(700) if a[x] == '1'])
print([x for x in range(700) if a[x] == '2'])
print([x for x in range(700) if a[x] == '3'])
print([x for x in range(700) if a[x] == '4'])