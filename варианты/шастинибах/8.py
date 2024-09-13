import itertools

for s, a in enumerate(itertools.product('БЕНРСТЬЯ', repeat=5), 1):
    ss = ''.join(a)
    if ss[0] == 'Р' and 'Ь' not in ss and s % 2 == 0:
        print(s, ss)