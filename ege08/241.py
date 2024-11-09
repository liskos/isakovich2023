import itertools

k=0
for i in itertools.permutations('10011010', r=8):
    ss = ''.join(i)
    if '11' in ss and '00' in ss:
        print(ss)
        k+=1
print(k//11)