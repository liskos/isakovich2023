import itertools

k=0
for i in itertools.product('ОГЭИНФ', repeat=6):
    ss = ''.join(i)
    if ss[0] in 'ЭО' and 'ОГЭ' not in ss and ss[4:] == 'НФ' and ss.count('ИГ') >= 1:
        k+=1
print(k)