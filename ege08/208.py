import itertools

k=0
for i in itertools.permutations('ДЕЙКСТРА', r=6):
    ss = ''.join(i)
    if ss.count('Й') == 1 and ('ЙЕ' not in ss or 'ЙА' not in ss):
        k+=1
print(k)