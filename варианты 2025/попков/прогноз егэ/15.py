p = range(84, 341 + 1)
q = range(38, 412 + 1)
a1_best = 0
a2_best = 200
for a1 in range(200):
    for a2 in range(a1, 200):
        a = range(a1, a2+1)
        if all([(not((x in p) == (x in q)) and not(x in a))==False for x in range(1, 200)]):
            if a2 - a1 < a2_best - a1_best:
                a1_best = a1
                a2_best = a2
print(a1_best, a2_best, a2_best - a1_best)
