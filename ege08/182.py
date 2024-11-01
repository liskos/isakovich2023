import itertools


for s, i in enumerate(itertools.product('АВДПР', repeat=4), 1):
    ss = ''.join(i)
    if 'А' not in ss:
        print(s, ss)

#195
