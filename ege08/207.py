import itertools

k=0
for i in itertools.permutations('РЕЖИМДНО', r=6):
    ss = ''.join(i)
    if ss[0] in 'РЖМДН' and ss[1] in 'ЕИО' and ss[-1] in 'ЕИО':
        k+=1
print(k)