import itertools

a = set()
for s, i in enumerate(itertools.permutations('ЗАПИСЬ'), 1):
    ss = ''.join(i)
    if ss[0] != 'Ь' and 'АЬ' not in ss and 'ИЬ' not in ss:
        a.add(ss)

print(len(a))