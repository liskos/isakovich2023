import itertools



for s, i in enumerate(itertools.permutations('КОРАБЛИК'), 1):
    ss = ''.join(i)
    if 'К' in ss[0] or 'Р' in ss[0] or 'Б' in ss[0] or 'Л' in ss[0]:
        print(s, ss)
        break

