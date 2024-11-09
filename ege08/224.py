import itertools

k=set()
for i in itertools.product('01234567', repeat=4):
    ss = ''.join(i)
    if ss[0] in '246' and ss[0] != '0':
        print(ss)
        k.add(ss)
print(len(k))