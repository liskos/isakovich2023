import itertools

k=set()
for i in itertools.permutations('ВАЙФУ', r=4):
    ss = ''.join(i)
    if ss[0] != 'Й' and 'ВФ' not in ss and 'ФВ' not in ss:
        k.add(ss)
print(len(k))