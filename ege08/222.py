import itertools

k=set()
for i in itertools.product('ЗЕРКАЛО', repeat=6):
    ss = ''.join(i)
    if ss.count('К') <= 4 and ss.count('З') == 1 and ss.count('Е') == 1 and ss.count('Р') == 1 and ss.count('А') == 1 and ss.count('Л') == 1 and ss.count('О') == 1:
        print(ss)
        k.add(ss)
print(len(k))