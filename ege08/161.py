import itertools

k=0
for i in itertools.permutations('01234567', r=6):
    s = ''.join(i)
    s = s.replace('3', '1').replace('5', '1').replace('7', '1').replace('2', '0').replace('4',
                                                                                                            '0').replace(
        '6', '0')
    if '11' not in s and '00' not in s and i[0] != '0':
        k+=1
print(k)

