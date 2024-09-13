import itertools



for s, i in enumerate(itertools.product('АЗНС', repeat=5), 1):
    ss = ''.join(i)
    if 'САЗАН' in ss or 'ЗАНАС' in ss:
        print(s, ss)
print(787 - 292 + 2)


