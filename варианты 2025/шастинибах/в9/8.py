import itertools


for i, s in enumerate(itertools.product('ГЕИНРСЯ', repeat=6), 1):
    ss = ''.join(s)
    if 'ГИРЯ' in ss:
        print(i, ss)