import itertools

k = 0

for s, i in enumerate(itertools.product('ОБЪЕМ', repeat=4), 1):
    ss = ''.join(i)
    if ss.count('О') == 1 and ss[-1] != 'Ъ' and ss[0] != 'Ъ':
        k+=1

print(k)