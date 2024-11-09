import itertools

k=0
for i in itertools.product('CONST', repeat=16):
    ss = ''.join(i)
    if 'CC' not in ss and 'OO' not in ss and 'NN' not in ss and 'SS' not in ss and 'TT' not in ss and ss[0] != 'S' and ss[-1] != 'S':
        k+=1
print(k)