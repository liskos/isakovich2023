import itertools

k=set()
for i in itertools.product('ПОЛЯКВ', repeat=4):
    ss = ''.join(i)
    if 'ВО' in ss or 'ОЛ' in ss or 'ЛК' in ss:
        k.add(ss)
print(len(k))