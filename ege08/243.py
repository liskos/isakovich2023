import itertools

k=0
for i in itertools.permutations('ВОЛКОДАВ', r=8):
    ss = ''.join(i)
    print(ss)
    k+=1
print(k//4)