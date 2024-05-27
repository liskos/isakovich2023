def f(n):
    s = bin(n)[2:]
    s = s + s[-2] + s[1]
    return int(s, 2)

a = []
for i in range(3, 10000):
    if f(i) <= 190:
        a.append(i)
print(max(a))
