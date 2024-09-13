import itertools


k = 0
for s, i in enumerate(itertools.product('КУМА', repeat=5), 1):
    ss = ''.join(i)
    if ss[0] == 'Т' or ss[0] == 'К' and ss[-1] == 'У' or ss[-1] == 'А':
        k+=1
        print(ss)
print(k)

