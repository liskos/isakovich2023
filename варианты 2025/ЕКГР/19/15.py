
a1_best = 0
a2_best = 150

b = range(36, 75 + 1)
c = range(60, 110 + 1)
for a1 in range(1, 150):
    for a2 in range(a1, 150):
        a = range(a1, a2)
        if all(not(not(x in a)) or ((x in b) == (x in c)) for x in range(300)):
            if a2 - a1 < a2_best - a1_best:
                a1_best = a1
                a2_best = a2
print(a2_best-a1_best)