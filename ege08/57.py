import itertools


k = 0
for s, i in enumerate(itertools.product('ПИРОГ', repeat=6), 1):
    ss = ''.join(i)
    if ss.count('Р') == 1:
        print(s, ss)
        k+=1
print(k)


