import itertools


for s, i in enumerate(itertools.product('ЕКМОПРТЬЮ', repeat=5), 1):
    ss = ''.join(i)
    if 'Ь' not in ss[0] and ss.count('К') == 2:
        print(s, ss)