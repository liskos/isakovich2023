import itertools

b = set()
for s, i in enumerate(itertools.product('ВИДЕО', repeat=6), 1):
    ss = ''.join(i)
    if ss.count('И') >= 1 and ss.count('Е') >= 1:
        b.add(ss)
print(len(b))
