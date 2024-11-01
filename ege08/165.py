import itertools

k=0
for i in itertools.permutations('0123456789ABCDEF', r=4):
    s = ''.join(i)
    for x in '02468ACE':
        s = s.replace(x, '0')
    for x in '13579BDF':
        s = s.replace(x, '1')
    if '11' not in s and '00' not in s and i[0] != '0':
        k+=1
print(k)

