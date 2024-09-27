import itertools


k = 0
for s, i in enumerate(itertools.product('ПИРОГ', repeat=6), 1):
    ss = ''.join(i)
    h = ss.replace('И', 'О')
    if ss.count('Р') == 1 and 'РО' in h:
        print(s, ss)
        k+=1
print(k)


