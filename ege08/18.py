import itertools

for s, a in enumerate(itertools.product('ИОУ', repeat=5), 1):
    ss = ''.join(a)
    if s == 240:
        print(ss)
        break
