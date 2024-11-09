import itertools

a = set()
for s, i in enumerate(itertools.product('СЕПИЯ', repeat=8), 1):
    ss = ''.join(i)
    if ss.count('Е') <= 2 and ss.count('И') <= 2 and ss.count('Я') <= 2 and (ss[0] in 'СП' or ss[0] not in 'СП') and ss[1:] not in 'СП':
        a.add(ss)

print(len(a))
