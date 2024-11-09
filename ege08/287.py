import itertools

k=0
for i in itertools.product('POLYGON', repeat=5):
    ss = ''.join(i)
    if ss[0] == ss[-1] and ss[1] == ss[-2] and ss[3] in 'OY':
        k+=1
print(k)
