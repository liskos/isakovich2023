import itertools

k=0
for i in itertools.permutations('0123456789ABCDEF', r=12):
    if i[0] != '0' and all([i[x] > i[x+1] for x in range(11)]):
        s = ''.join(i)
        for x in '02468ACE':
            s = s.replace(x, '0')
        for x in '13579BDF':
            s = s.replace(x, '1')
        if '11' not in s and '00' not in s:
            k+=1

print(k)