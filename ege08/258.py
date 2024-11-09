import itertools

a = []
b = []
for s, i in enumerate(itertools.product('АИКЛМЬ', repeat=6), 1):
    ss = ''.join(i)
    if ss[0] == 'К' and ss[-1] == 'Ь' and ss.count('А') == 1 and ss.count('И') == 1 and ss.count('К') == 1 and ss.count('Л') == 1 and ss.count('М') == 1 and ss.count('Ь') == 1:
        print(s, ss)
        a.append(s)
        break
    if ss == 'ЬМЛИАК':
        print(ss)
        a.append(s)
        break
print(a[0] - a[1])