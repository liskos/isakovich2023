import itertools


k = 0
for s, i in enumerate(itertools.product('ПИРОГ', repeat=5), 1):
    ss = ''.join(i)
    h = ss.replace('И', 'О').replace('РО', 'X')
    if ss.count('Р') <= 2 and 'Р' not in h:
        print(s, ss)
        k+=1
print(k)


