import itertools


k = 0
for s, i in enumerate(itertools.product('ЛЕТО', repeat=4), 1):
    ss = ''.join(i)
    if ss[0] == 'Л' or ss[0] == 'Т':
        k+=1
        print(ss)
print(k)

