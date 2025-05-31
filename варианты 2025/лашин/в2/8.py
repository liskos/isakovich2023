import itertools

k = 0
for i in itertools.product('0123456789AB', repeat=5):
    ss = ''.join(i)
    ss = ss.replace('2', '0').replace('3','1').replace('4','0').replace('5','1').replace('6','0').replace('7','1').replace('8','0').replace('9','1').replace('A','0').replace('B','1')
    if i[0] != '0' and '00' not in ss and '11' not in ss and i.count('0') <= 2 and i.count('1') <= 2 and i.count('2') <= 2 and i.count('3') <= 2 and i.count('4') <= 2 and i.count('5') <= 2 and i.count('6') <= 2 and i.count('7') <= 2 and i.count('8') <= 2 and i.count('9') <= 2 and i.count('A') <= 2 and i.count('B') <= 2:
        k+=1
        print(i)
print(k)