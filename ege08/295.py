import itertools

k=0
for i in itertools.product('012345678', repeat=6):
    ss = ''.join(i)
    if ss.count('1') + ss.count('3') + ss.count('5') + ss.count('7') <= 2 and sum(map(int, ss)) % 6 == 0 and sum(map(int, ss)) % 4 > 0 and ss[0] != '0':
        k+=1
print(k)
