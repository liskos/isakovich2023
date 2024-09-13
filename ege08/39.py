import itertools


k = 0
for s, i in enumerate(itertools.product('ABCDX', repeat=4), 1):
    ss = ''.join(i)
    if ss.count('X') == 1:
        print(s, ss)
        k+=1
print(k)


