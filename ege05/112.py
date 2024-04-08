def f(n):
    s = str(n)
    a1 = int(s[0])*int(s[1])
    a2 = int(s[1])*int(s[2])
    if a2 > a1:
        a1, a2 = a2, a1
    return str(a1)+str(a2)


for i in range(100, 999):
    if f(i) == "123":
        print(i)
        break