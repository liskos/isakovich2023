k = 10
a1_best = 0*k
a2_best = 100*k

p = range(17*k, 58*k+1)
q = range(29*k, 80*k+1)
for a1 in range(25*k, 31*k):
    for a2 in range(56*k, 60*k):
        a = range(a1, a2+1)
        if all(not(x in p) or not((x in q) and not(x in a)) or not(x in p) for x in range(100*k)):
            if a2-a1 < a2_best-a1_best:
                a2_best = a2
                a1_best = a1
print(a1_best/k, a2_best/k, (a2_best-a1_best)/k)

