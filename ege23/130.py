def f(a, b, c):
    if a > b or c > 5:
        return 0
    if a == b and c == 5:
        return 1
    return f(a + 2, b,c + 1) + f(a + 3, b, c + 1) + f(a * 2, b, c + 1)

s = set()
for i in range(1, 1000):
    if f(10,i,0) > 0:
        s.add(i)
print(len(s))