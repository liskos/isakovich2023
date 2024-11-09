import itertools

k=0
for i in itertools.product('ЕГЭИНФ', repeat=6):
    ss = ''.join(i)
    if ss[0] == 'Е' and 'ЕГЭ' not in ss and ss[-1] in 'ЭИ' and ss.count('ФИ') >= 2:
        k+=1
print(k)