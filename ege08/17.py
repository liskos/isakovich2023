import itertools

for s, a in enumerate(itertools.product('КОР', repeat=5), 1):
    ss = ''.join(a)
    if s == 238:
        print(ss)
        break