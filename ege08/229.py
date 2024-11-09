import itertools

k=set()
for i in itertools.product('0123456', repeat=7):
    ss = ''.join(i)
    if '22' not in ss and '44' not in ss and ss[0] not in '035':
        print(ss)
        k.add(ss)
print(len(k))