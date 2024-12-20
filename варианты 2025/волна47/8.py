import itertools

for i, s in enumerate(itertools.product('АЙЛМ', repeat=5), 1):
    ss = ''.join(s)
    if 'М' not in ss and 'Л' not in ss and 'ЙЙ' not in ss:
        print(i, ss)

