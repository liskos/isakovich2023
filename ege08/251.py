import itertools

k=0
for i in itertools.product('ОБЩЕСТВ', repeat=5):
    ss = ''.join(i)
    if ss[0] not in 'ЩБ' and 'ВВ' in ss[3:] and 'ВЕ' not in ss and 'ЕВ' not in ss and 'ТБ' in ss:
        k+=1
print(k)