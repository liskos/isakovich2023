import itertools

k=0
for i in itertools.product('0123456', repeat=5):
    ss = ''.join(i)
    if ss[0] != '0' and ss.count('0') + ss.count('2') + ss.count('4') + ss.count('6') >= 3 and sum(map(int, ss)) % sum(map(int, ss)) == 0 and sum(map(int, ss)) % 1 == 0:
        k+=1
print(k)
