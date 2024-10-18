import itertools

for i, s in enumerate(itertools.product('ЕЛОПР', repeat=5), 1):
    ss = ''.join(s)
    if ss[-1] == 'Е' or ss[-1] == 'О':
        print(ss)