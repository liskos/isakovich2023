import itertools


k = 0
for s, i in enumerate(itertools.product('АБВГДЯ', repeat=5), 1):
    ss = ''.join(i)
    if 'Я' not in ss[1:-1] and ss.count('Я') == 1:
        print(s, ss)
        k+=1
print(k)


