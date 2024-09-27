import itertools


k = 0
for s, i in enumerate(itertools.product('АБВГДЯ', repeat=3), 1):
    ss = ''.join(i)
    if 'Я' not in ss[1] and 1 >= ss.count('Я') >= 0:
        print(s, ss)
        k+=1
print(k)


