import itertools

k=set()
for i in itertools.permutations('СОТКАПЛЗ', r=5):
    ss = ''.join(i)
    if ss[-1] not in 'ОА' and 'ЗЛО' not in ss:
        k.add(ss)
print(len(k))