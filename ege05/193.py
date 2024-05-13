def f(n):
    s = bin(n)[2:]
    if s.count("1") > s.count("0"):
        s = s + "1"
    else:
        s = s + "0"
    return int(s, 2)

for i in range(1, 10000):
    if f(i) < 90:
        print(f(i))