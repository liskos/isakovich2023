import itertools


for i, s in enumerate(itertools.product('АКМС', repeat=6), 1):
    ss = ''.join(s)
    if 'С' not in ss and 'КК' not in ss and 'М' not in ss:
        print(i, ss)