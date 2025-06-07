
l = range(1300, 2550 + 1)
n = range(1750, 3400 + 1)
a1_best = 0
a2_best = 0
for a1 in range(1200, 2600):
    for a2 in range(1747, 3402):
        a = range(a1, a2+1)
        if all(not(not(x in l) or ((x in n) and not(x in a)) or not(x in l)) for x in range(10000)) == False:
            if a2 - a1 > a2_best - a1_best:
                a1_best = a1
                a2_best = a2
print(a1_best, a2_best, (a2_best - a1_best))