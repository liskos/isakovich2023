import itertools

k=0
for i in itertools.product('ТИМАШЕВСК', repeat=4):
    ss = ''.join(i)
    if ss[0] not in 'ИАЕШ':
        k+=1
print(k)
