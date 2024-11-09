import itertools

k=set()
for i in itertools.product('ИНФА', repeat=6):
    ss = ''.join(i)
    if ss.count('Ф') == 2:
        k.add(ss)
print(len(k))