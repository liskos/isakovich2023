def f(a):
    global b
    global c
    for x in range(26000 * k):
        if not (not (x in a) or (not (x in b) == (x in c))):
            return False
    return True
k = 10
b = range(999 * k, 25482 * k + 1)
c = range(12345 * k, 19841 * k + 1)
a1_best = 0
a2_best = 0
for a1 in range(9985, 10000):
    for a2 in range(123435, 123445):
        a = range(a1, a2+1)
        if f(a):
            if a2 - a1 > a2_best - a1_best:
                a1_best = a1
                a2_best = a2
print(a1_best / k, a2_best / k, (a2_best - a1_best) / k)