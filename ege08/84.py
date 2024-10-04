import itertools



for s, i in enumerate(itertools.product('АГИЛМОРТ', repeat=4), 1):
    ss = ''.join(i)
    if 'ИМ' in ss[1:]:
        print(s, ss)


