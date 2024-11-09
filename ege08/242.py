import itertools

k=0
for i in itertools.permutations('АТТЕСТАТ', r=8):
    ss = ''.join(i)
    print(ss)
    k+=1
print(k//24//2)