import itertools

k = 0

for i in itertools.product('ПРИКАЗ', repeat=5):
    ss = ''.join(i)
    if (ss.count('П') <= 1 and ss.count('Р') <= 1 and
        ss.count('З') <= 1 and ss.count('И') <= 1 and
        ss.count('А') <= 1 and ss.count('К') <= 1):
        k+=1



print(k)
