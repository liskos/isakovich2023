k = 10
l = range(1300 * k, 2550 * k + 1)
n = range(1750 * k, 3400 * k + 1)
a1_best = 0
a2_best = 10000 * k
for a1 in range(1748 * k, 1752 * k):
    for a2 in range(2548 * k, 2551 * k):
        a = range(a1, a2+1)
        if all((not(x in l) or not((x in n) and not(x in a)) or not(x in l)) for x in range(10000 * k)):
            if a2 - a1 < a2_best - a1_best:
                a1_best = a1
                a2_best = a2
print(a1_best / k, a2_best / k, (a2_best - a1_best) / k)