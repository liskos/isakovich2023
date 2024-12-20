import itertools


for i, s in enumerate(itertools.product('ДИК1О', repeat=5), 1):
    ss = ''.join(s)
    if ss.count('1') == 2 and '11' not in ss:
        print(i, ss)