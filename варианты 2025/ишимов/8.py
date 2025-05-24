import itertools


k = 0
for i in itertools.product('0123456789AB', repeat=5):
    ss = ''.join(i)
    ss = ss.replace('2', '0').replace('3', '1').replace('4', '0').replace('5', '1').replace('6', '0').replace('7', '1').replace('8', '0').replace('9', '1').replace('A', '0').replace('B', '1')
    if i.count('3') == 1 and ('01010' in ss or '10101' in ss) and i[0] != '0':
        k+=1
        print(ss)
print(k)