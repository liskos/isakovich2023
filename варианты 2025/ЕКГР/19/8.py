import itertools


for i, s in enumerate(itertools.product('АБДЕОП', repeat=6), 1):
    ss = ''.join(s)
    if ss[0] == 'О' and ss.count('А') == 1 and ss.count('Б') == 1 and ss.count('Д') == 1 and ss.count('Е') == 1 and ss.count('О') == 1 and ss.count('П') == 1:
        print(i, ss)