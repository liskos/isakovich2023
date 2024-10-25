import itertools

k=0

for s, i in enumerate(itertools.product('1Н2СЙ', repeat=4), 1):
    ss = ''.join(i)
    if ss.count('1') + ss.count('2') > 0 and ss[0] != 'Й':
        k+=1
print(k)
