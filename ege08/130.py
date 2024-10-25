import itertools

k=0

for s in itertools.permutations('1С11Л', r=5):
    ss = ''.join(s)
    if '11' not in ss:
        k+=1
print(k)
