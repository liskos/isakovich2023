import itertools


k = 0
for i in itertools.permutations('012121212', r=4):
    ss = ''.join(i)
    if ss[0] != '0' and '11' not in ss and '22' not in ss and '00' not in ss:
        print(ss)
        k+=1
print(k)