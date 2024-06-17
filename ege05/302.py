def f(n):
    s = str(n)
    if int(str(n)[0]) % 2 == 0:
        n1 = int(s[0]) + int(s[2])
        n2 = abs(int(s[1]) - int(s[3]))
        return n1 + n2
    else:
        s =int(''.join(sorted(list(s))))
        s = bin(s)[2:]
        return s.count('1')


a = []
for i in range(1000, 10000):
    if f(i) > 20:
        a.append(i)
print(len(a))