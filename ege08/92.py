import itertools


k = 0
for s, i in enumerate(itertools.product('МАНОК', repeat=5), 1):
    ss = ''.join(i)
    if ss.count('М') == 1 and ss.count('А') == 1 and ss.count('Н') == 1 and ss.count('О') == 1 and ss.count('К') == 1 and 'О' not in ss[0] and 'АО' not in ss:
        k += 1
        print(s, ss)
print(k)



