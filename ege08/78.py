import itertools



for s, i in enumerate(itertools.product('АИОУЭ', repeat=4), 1):
    ss = ''.join(i)
    if 'ИААЭ' in ss:
        print(s, ss)
        break

