import itertools

k=0
for i in itertools.permutations('1П1ЛЬС1Н', r=7):
    ss = ''.join(i)
    if '1Ь1' not in ss:
        k+=1
print(k)