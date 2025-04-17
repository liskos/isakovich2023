a1_best = 0
a2_best = 100

p = range(10, 40 + 1)
q = range(20, 50 + 1)

for a1 in range(10, 100):
    for a2 in range(a1, 100):
        a = range(a1, a2 + 1)
        if all(not(x in p) or not(((x in q) and not(x in a)) or not(x in p)) for x in range(9, 60)):
            if a2 - a1 < a2_best - a1_best:
                a2_best = a2
                a1_best = a1
print(a2_best-a1_best, a2_best, a1_best)