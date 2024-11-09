import itertools

a = set()
for s, i in enumerate(itertools.product('ЛИДА', repeat=10), 1):
    ss = ''.join(i)
    if ss.count('А') <= 2 and ss.count('И') <= 2 and (ss[0] in 'ЛД' or ss[0] not in 'ЛД') and ss[1:].count('Д') + ss[1:].count('Л') == 0:
        print(ss)
        a.add(ss)

print(len(a))
