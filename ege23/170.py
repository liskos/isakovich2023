def f(a, b):
    for i in range(2, max(a, b)):
        if a % i == 0 and b % i == 0:
            return False
    return True


a = {(2, 3)}
for _ in range(5):
    b = set()
    for i in a:
        b.add((min(i[0] + 3, i[1]), max((i[0] + 3, i[1]))))
        b.add((min(i[0] * 4, i[1]), max((i[0] * 4, i[1]))))
        b.add((min(i[0], i[1] + 5), max((i[0], i[1] + 5))))
        b.add((min(i[0], i[1] * 2), max((i[0], i[1] * 2))))
    a = b.copy()
b = set()
for i in a:
    if f(*i):
        b.add(i)
print(b)
print(len(b))
print(f(2, 32))