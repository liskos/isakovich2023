import itertools


for i, s in enumerate(itertools.product('ДНОР', repeat=6), 1):
    ss = ''.join(s)
    if ss[-1] != 'Н' and 'Р' not in ss and ss.count('О') <= 2:
        print(i, ss)