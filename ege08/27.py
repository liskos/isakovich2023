import itertools


k = 0
for s, i in enumerate(itertools.product('КРОТ', repeat=6), 1):
    ss = ''.join(i)
    if ss.count('О') == 1:
        k+=1
        print(ss)
print(k)

