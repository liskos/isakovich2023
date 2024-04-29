def f(n):
    s = bin(n)[2:]
    b = s[1:].replace("0", "2").replace("1", "0").replace("2","1")
    return int(b, 2)

k = 0
for i in range(1, 1000):
    if f(i) + i <= 123:
        k = i
print(k)