import itertools



for s, i in enumerate(itertools.product('ВЕКНО', repeat=5), 1):
    ss = ''.join(i)
    if ss.count('О') == 1 and ss.count('Е') == 1:
        print(s, ss)




