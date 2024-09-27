import itertools


k = 0
for s, i in enumerate(itertools.product('ПИРОГ', repeat=4), 1):
    ss = ''.join(i)
    h = ss.replace('П', 'Р').replace('Г', 'Р').replace('РО', 'X')
    if ss.count('О') <= 2 and 'О' not in h:
        print(s, ss)
        k+=1
print(k)


