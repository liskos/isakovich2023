import itertools

k=0
for i in itertools.product('0123456789ABCDEF', repeat=6):
    ss = ''.join(i)
    if ss[0] not in '01' and ss[4:] == 'AB':
        k+=1
print(k)