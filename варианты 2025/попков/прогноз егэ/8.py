import itertools
k = 0

for i in itertools.product('01234567', repeat=7):
    ss = ''.join(i)
    ss = ss.replace('0', '8').replace('1', '9').replace('2', '8').replace('3','9').replace('4','8').replace('5','9').replace('6','8').replace('7','9')
    if i[0] != '0' and i.count('0') == 2 and '88' not in ss and '99' not in ss:
        k += 1
print(k)