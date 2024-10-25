import itertools

k=0

for s, i in enumerate(itertools.product('К1Б1Л1', repeat=6), 1):
    ss = ''.join(i)
    if '11' not in ss:
        k+=1
print(k)
