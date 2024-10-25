import itertools

k=0

for s, i in enumerate(itertools.product('А1И1У1', repeat=6), 1):
    ss = ''.join(i)
    if ss.count('1') >= 3:
        k+=1
print(k)
