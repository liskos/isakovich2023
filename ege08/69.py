import itertools


k = 0
for s, i in enumerate(itertools.product('АБВГДЕ', repeat=4), 1):
    ss = ''.join(i)
    if 'Г' not in ss[1:-1] and ss.count('Г') == 1:
        print(s, ss)
        k+=1
print(k)


