import itertools
k = 0

for i in itertools.product('котбус', repeat=8):
    ss = ''.join(i)
    if 'кот' in ss and ss[0] not in 'оу':
        k += 1
print(k)