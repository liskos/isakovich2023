def f(n):
    s = str(n)
    if int(s[0]) % 4 == 0:
        s = '9' + s[1:]
    elif int(s[0]) % 2 == 0:
        s = '3' + s[1:]
    return s

a = []
for i in range(1000, 10000):
    s = f(i)
    if s[0] == '9' and int(s) % 8 == 4:
        a.append(i)
print(len(a))