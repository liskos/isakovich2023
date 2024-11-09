import itertools

k=0
for i in itertools.product('ЯСНОВИДЕЦ', repeat=5):
    ss = ''.join(i)
    if ss[0] in 'СНВДЦ' and ss[-1] in 'ЯОИЕ' and ss.count(ss[0]) == 1 and ss.count(ss[-1]) == 1:
        k+=1
print(k)