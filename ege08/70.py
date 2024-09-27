import itertools


k = 0
for s, i in enumerate(itertools.product('АБВГ', repeat=5), 1):
    ss = ''.join(i)
    if 'Г' not in ss[0:-1] and ss.count('Г') <= 1:
        print(s, ss)
        k+=1
print(k)


