import itertools

k=0
for i in itertools.permutations('10010101', r=8):
    ss = ''.join(i)
    if '11' not in ss and '00' not in ss:
        print(ss)
        k+=1
print(k//8)