import itertools

k=set()
for i in itertools.product('ТИХОРЕЦК', repeat=4):
    ss = ''.join(i)
    if ('ТИ' in ss or 'ИХ' in ss or 'ХО' in ss) and ss.count('И') + ss.count('О') + ss.count('Е') == 2:
        k.add(ss)
print(len(k))