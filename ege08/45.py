import itertools


k = 0
for s, i in enumerate(itertools.product('КЛОУН', repeat=5), 1):
    ss = ''.join(i)
    if 'У' in ss:
        print(s, ss)
        k+=1
print(k)


