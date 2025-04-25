
a1_best = 0
a2_best = 150

b = range(36, 75 + 1)
c = range(60, 110 + 1)
for a1 in range(1, 150):
    for a2 in range(a1, 150):
        a = range(a1, a2+1)
        if all(not(not(x in a)) or ((x in b) == (x in c)) for x in range(300)):
            if a2 - a1 < a2_best - a1_best:
                a1_best = a1
                a2_best = a2
print(a1_best, a2_best, a2_best-a1_best)


k = 10
a1_best = 0
a2_best = 150 * k

b = range(36 * k, 75 * k + 1)
c = range(60 * k, 110 * k + 1)
for a1 in range(33 * k, 40 * k):
    for a2 in range(105 * k, 115 * k):
        a = range(a1, a2+1)
        if all(not(not(x in a)) or ((x in b) == (x in c)) for x in range(300 * k)):
            if a2 - a1 < a2_best - a1_best:
                a1_best = a1
                a2_best = a2
print(a1_best / k, a2_best / k, (a2_best-a1_best) / k)