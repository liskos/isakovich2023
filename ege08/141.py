import itertools

k=0

for s, i in enumerate(itertools.product('Б1РКЛ1Й', repeat=4), 1):
    ss = ''.join(i)
    if ss.count('1') > 0 and ss[0] != 'Й':
        k+=1
print(k)
