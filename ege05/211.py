def f(n):
    a = sorted(list(str(n)))
    nmax = a[2] + a[1]
    if a[0] != '0':
        nmin = a[0] + a[1]
    elif a[1] != '0':
        nmin = a[1] + a[0]
    else:
        nmin = a[2] + a[0]
    return int(nmax) - int(nmin)


print(f(351))
for i in range(100, 1000):
    if f(i) == 60:
        print(i)
        break