import itertools

k=set()
for i in itertools.permutations('ТЬЮРИНГ', r=6):
    ss = ''.join(i)
    if ss[0] != 'Ь' and 'ЮЬ' not in ss and 'ИЬ' not in ss:
        k.add(ss)
print(len(k))