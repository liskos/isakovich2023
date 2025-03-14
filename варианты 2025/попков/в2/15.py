a1_best = 0
a2_best = 0
k = 20
for a1 in range(10*k, 15*k):
    for a2 in range(15*k, 18*k):
        a = range(a1, a2+1)
        if a2 - a1 > a2_best - a1_best and all(not(not(x in range(13*k, 19*k+1)) or (x in range(17*k, 24*k+1))) or not(x in a) for x in range(1, 100*k)):
            a1_best = a1
            a2_best = a2

print(a1_best/k, a2_best/k)