import itertools


for i, s in enumerate(itertools.product('КОСУФ', repeat=5), 1):
    ss = ''.join(s)
    if 'Ф' not in ss and ss.count('У') == 2:
        print(i, ss)