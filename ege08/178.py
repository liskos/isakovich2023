import itertools

a = set()

for s, i in enumerate(itertools.product('АЛКОШ', repeat=5), 1):
    ss = ''.join(i)
    if ss.count('А') + ss.count('О') > 0:
        a.add(ss)

print(len(a))