def f(x):
    return x + 2, x + 3, x * 3

a = [' '] * 1000
for i in range(1000):
        if i >= 313:
            a[i] = '0'
for i in range(1000):
        if a[i] == ' ' and any(a[x] == '0' for x in f(i)):
            a[i] = '1'
for i in range(1000):
        if a[i] == ' ' and all(a[x] == '1' for x in f(i)):
            a[i] = '2'
for i in range(1000):
        if a[i] == ' ' and any(a[x] == '2' for x in f(i)):
            a[i] = '3'
for i in range(1000):
        if a[i] == ' ' and all(a[x] in '13' for x in f(i)):
            a[i] = '4'
print([i for i in range(1000) if a[i] == '2'])
print([i for i in range(1000) if a[i] == '3'])
print([i for i in range(1000) if a[i] == '4'])