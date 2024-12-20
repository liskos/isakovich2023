import itertools
k=0
for s in itertools.product('0123456789AB', repeat=6):
    if s.count('B') == 1 and sum([s.count(x) for x in '02468A']) == 3 and s[0] != '0':
        k+=1
print(k)