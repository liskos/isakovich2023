import itertools

k=0

for s in itertools.permutations('ЗД1Н11', r=6):
    ss = ''.join(s)
    if '11' not in ss:
        k+=1
print(k)
