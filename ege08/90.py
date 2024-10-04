import itertools


k = 0
for s, i in enumerate(itertools.product('КРОЙ', repeat=4), 1):
    ss = ''.join(i)
    if ss.count('К') == 1 and ss.count('Р') == 1 and ss.count('О') == 1 and ss.count('Й') == 1 and 'Й' not in ss[0] and 'ОЙ' not in ss:
        k += 1
        print(s, ss)
print(k)



