def f(n):
    s = bin(n)[2:]
    while len(s) < 8:
        s = "0" + s
    s = s.replace("1", "2").replace("0", "1").replace("2","0")
    return int(s, 2) + 1


print(f(153))