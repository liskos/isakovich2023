import itertools

k=set()
for i in itertools.product('ЧОАНИМЕ', repeat=6):
    ss = ''.join(i)
    if ss.count('М') == 3:
        k.add(ss)
print(len(k))