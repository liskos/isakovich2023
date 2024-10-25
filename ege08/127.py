import itertools



for s, i in enumerate(itertools.product('ЬСОНЕ', repeat=4), 1):
    ss = ''.join(i)
    if s == 100:
        print(s, ss)
        break

