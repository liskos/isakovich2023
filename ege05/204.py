def f(n):
    s = bin(n)[2:]
    s = s + str(s.count("1") % 2)
    s = s + str(s.count("1") % 2)
    return int(s, 2)


for i in range(1, 10000):
    if f(i) > 80:
        print(f(i))
        break
