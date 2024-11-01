import itertools



for s, i in enumerate(itertools.product('АВИКНСТ', repeat=4), 1):
    ss = ''.join(i)
    if ss[0] != 'А' and ss[0] != 'И' and ss[-1] == 'А' or ss[-1] == 'И':
        print(s, ss)
#1492