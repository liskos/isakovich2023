def f(n):
    t = ''
    for i in str(n):
        s = bin(int(i))[2:]
        s = s.zfill(4)
        t = t + s
    t = t.replace('1', '2').replace('0', '1').replace('2', '0')
    return int(t, 2)


for i in range(1, 10000):
    if f(i) == 151:
        print(i)
        break




