import itertools

k=0
for i in itertools.permutations('1001010', r=7):
    ss = ''.join(i)
    if '11' not in ss and '00' not in ss:
        print(ss)
        k+=1
print(k//4)