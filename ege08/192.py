import itertools
k = 0
a = set()
for i in itertools.product('МАРИНА', repeat=8):
    ss = ''.join(i)
    if set(ss[:4]) == set('МАРИ') and set(ss[-4:]) <= set('ИНА'):
        a.add(ss)
a = sorted(a)
print(a.index('МАРИАННА'))


