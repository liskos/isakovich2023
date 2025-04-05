p = range(15, 142 + 1)
q = range(38, 167 + 1)
a1_best = 0
a2_best = 200
for a1 in range(200):
    for a2 in range(a1, 200):
        a = range(a1, a2+1)
        if all([not((not(x in q)) or not(not(x in a) and (x in p)) or not(x in q))==False for x in range(1, 200)]):
            if a2 - a1 < a2_best - a1_best:
                a1_best = a1
                a2_best = a2
print(a1_best, a2_best, a2_best - a1_best)

k = 10
p = range(15 * k, 142 * k + 1)
q = range(38 * k, 167 * k + 1)
a1_best = 0
a2_best = 200 * k
for a1 in range(36 * k, 40 * k):
    for a2 in range(137 * k, 150 * k):
        a = range(a1, a2+1)
        if all([not((not(x in q)) or not(not(x in a) and (x in p)) or not(x in q))==False for x in range(1, 200 * k)]):
            if a2 - a1 < a2_best - a1_best:
                a1_best = a1
                a2_best = a2
print(a1_best / k, a2_best / k, (a2_best - a1_best) / k)

