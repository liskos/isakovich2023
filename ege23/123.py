def f(a, b, c):
    if a == b:
        return 1
    if a > b or c > 5:
        return 0
    return f(a + 1, b, c + 1) + f(a * 2, b, c + 1) + f(a + a % 4, b, c + 1)

k = 0
for i in range(1, 81):
    if f(i, 80, 0) > 0:
        k+=1
print(k)