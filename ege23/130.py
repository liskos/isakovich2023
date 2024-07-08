def f(a, b, c):
    if a == b:
        return 1
    if a > b or a > 5:
        return 0
    return f(a + 2, b,c + 1) + f(a + 3, b, c + 1) + f(a * 2, b, c + 1)

s = set()
for i in range(1, 1000):
    if f(10,i,0) > 0:
        s.add(i)
print(len(s))