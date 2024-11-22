import itertools


for i, s in enumerate(itertools.product('АИКМНОРТФ', repeat=6)):
    ss = ''.join(s)
    if ss[0] != 'А' and ss.count('И') == 0 and ss.count('Р') == 3:
        print(i, ss)
        break