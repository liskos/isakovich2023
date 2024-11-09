import itertools

k=set()
for i in itertools.product('012345678', repeat=5):
    ss = ''.join(i)
    if ss[0] not in '01357' and ss[-1] not in '18' and ss.count('3') <= 1:
        k.add(ss)
print(len(k))