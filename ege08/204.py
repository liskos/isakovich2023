import itertools

k=0
for i in itertools.permutations('0101010101', r=6):
    ss = ''.join(i)
    if '11' in ss or '00' in ss:
        k+=1
print(k)