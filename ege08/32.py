import itertools


k = 0
for i in itertools.product('ABCD', repeat=3):
    ss = ''.join(i)
    t = True
    if ss[0] == 'A' and ss[1] != 'D':
        t = False
    if ss[2] == 'A' and ss[1] != 'D':
        t = False
    if ss[1] == 'A' and ss[0] != 'D' and ss[2] != 'D':
        t = False
    if ('BC' not in ss) and ('CB' not in ss) and t:
        k+=1
        print(ss)
print(k)

