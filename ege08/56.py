import itertools


k = 0
for s, i in enumerate(itertools.product('СИРОП', repeat=5), 1):
    ss = ''.join(i)
    if ss.count('О') == 1:
        print(s, ss)
        k+=1
print(k)


