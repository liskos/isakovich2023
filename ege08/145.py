import itertools

k=0

for s, i in enumerate(itertools.product('11У1А', repeat=6), 1):
    ss = ''.join(i)
    if ss.count('1') >= 3:
        k+=1
print(k)
