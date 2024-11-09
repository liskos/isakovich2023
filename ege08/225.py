import itertools

k=set()
for i in itertools.product('01234', repeat=5):
    ss = ''.join(i)
    if ss.count('0') + ss.count('2') + ss.count('3') <= 3 and ss[0] != '0':
        print(ss)
        k.add(ss)
print(len(k))