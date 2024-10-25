import itertools



for s, i in enumerate(itertools.product('УОА', repeat=5), 1):
    ss = ''.join(i)
    if s == 100:
        print(s, ss)
        break

