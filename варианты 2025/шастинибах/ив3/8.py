import itertools

k = 0
for i in itertools.product('0123456789ABCDEF', repeat=5):
    ss = ''.join(i)
    ss = ss.replace('E', 'D').replace('F', 'D')
    if i[0] != '0' and i.count('7') >= 1 and ss.count('D') == 2 and 'DD' in ss:
        k+=1
        print(ss)
print(k)