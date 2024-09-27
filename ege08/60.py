import itertools


k = 0
for s, i in enumerate(itertools.product('АБВГЭЮЯ', repeat=5), 1):
    ss = ''.join(i)
    if 'Я' not in ss[1:-1] and 'Ю' not in ss[1:-1] and 'Э' not in ss[1:-1]:
        print(s, ss)
        k+=1
print(k)


