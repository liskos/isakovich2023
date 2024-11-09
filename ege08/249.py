import itertools


for s, i in enumerate(itertools.product('АПРСУ', repeat=5), 1):
    ss = ''.join(i)
    if ss[0] == 'У' and 'АА' not in ss:
        print(ss, s)
        break
