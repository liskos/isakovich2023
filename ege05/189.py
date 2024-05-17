def f(n):
    s = bin(n)[2:].zfill(8)
    s = s[:s.find("1")] + s.replace("1", "2").replace("0", "1").replace("2","0")
    return int(s, 2) + 1


print(f(98))