def f(n):
    s = bin(n-1)[2:]
    while len(s) < 8:
        s = "0" + s
    s = s.replace("1", "2").replace("0", "1").replace("2","0")
    return int(s, 2)

for i in range(1, 256):
    if f(i) == 113:
        print(i)
        break
