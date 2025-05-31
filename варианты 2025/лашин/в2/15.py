b = range(999, 25482 + 1)
c = range(12345, 19841 + 1)
a1_best = 0
a2_best = 500
for a1 in range(500):
    for a2 in range(a1, 500):
        a = range(a1, a2+1)
        if all([(not(not(x in a) or (not(x in b) == (x in c))))==False for x in range(100, 500)]):
            if a2 - a1 < a2_best - a1_best:
                a1_best = a1
                a2_best = a2
print(a1_best, a2_best, a2_best - a1_best)