import itertools

a=set()
for i in itertools.product('АБВГД', repeat=3):
    ss = ''.join(i)
    if 'АБ' in ss or 'БВ' in ss or 'ВГ' in ss or 'ГД' in ss:
        print(ss)
        a.add(ss)
print(len(a))