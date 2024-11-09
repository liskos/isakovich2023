import itertools

k=set()
for i in itertools.product('ПИКАЧУ', repeat=6):
    ss = ''.join(i)
    if ss.count('У') >= 2:
        k.add(ss)
print(len(k))