import itertools

k=set()
for i in itertools.product('ПСКАЛЬ', repeat=4):
    ss = ''.join(i)
    if ss[0] != 'Ь' and 'ЬЬ' not in ss:
        k.add(ss)
print(len(k))