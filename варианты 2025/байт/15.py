a1best = 0
a2best = 0
m = 0
k = 10
p = range(15*k, 30*k+1)
q = range(60*k, 80*k+1)
for a1 in range(58*k, 63*k):
    for a2 in range(78*k, 83*k):
        a = range(a1, a2+1)
        if all((x not in a) or (x in p) or not((x not in a) or (x not in q)) for x in range(100*k)) and a2-a1 > m:
            m = a2-a1
            a1best = a1
            a2best = a2
print(m/k, a1best/k, a2best/k)
