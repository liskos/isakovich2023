import itertools


k = 0
for s, i in enumerate(itertools.product('СИРОП', repeat=5), 1):
    ss = ''.join(i)
    h = ss.replace('Р', 'С').replace('П', 'С')
    if ss.count('О') == 1 and 'СО' in h:
        print(s, ss)
        k+=1
print(k)


