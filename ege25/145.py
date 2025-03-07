def f(n):
    a = str(n)
    for i in range(len(a)):
        if int(a[i]) < 3 and sum(map(int, a)) % 10 == 0:
            return a


for i in range(1000000, 1300001, 10):
    if f(i):
        print(i)