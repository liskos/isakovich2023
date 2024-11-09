import itertools

k=0
for i in itertools.product('ГОЛ', repeat=20):
    ss = ''.join(i)
    if 'ГГ' not in ss and 'ОО' not in ss and 'ЛЛ' not in ss and ss[0] != 'Г' and ss[-1] != 'Г' and ('ОГЛ' in ss or 'ЛГО' in ss):
        k+=1
print(k)