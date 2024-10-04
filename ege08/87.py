import itertools



for s, i in enumerate(itertools.product('ВЕКНО', repeat=5), 1):
    ss = ''.join(i)
    if ss.count('Н') == 2 and ss.count('К') == 2:
        print(s, ss)




