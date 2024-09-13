import itertools



for s, i in enumerate(itertools.product('ОПРТ', repeat=5), 1):
    ss = ''.join(i)
    if 'ТОПОР' in ss or 'РОПОТ' in ss:
        print(s, ss)
print(787 - 532 + 1)


