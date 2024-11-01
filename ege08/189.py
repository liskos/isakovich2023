import itertools

a = set()
for s, i in enumerate(itertools.product('КОРНЕТ', repeat=5), 1):
    ss = ''.join(i)
    if ss.count('О') <= 1 and ss.count('Е') <= 1:
        a.add(ss)

print(len(a))
