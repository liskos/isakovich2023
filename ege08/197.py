import itertools

a = set()
for s, i in enumerate(itertools.product('КСЕНИЯ', repeat=8), 1):
    ss = ''.join(i)
    if ss.count('Е') <= 2 and ss.count('И') <= 2 and ss.count('Я') <= 2 and (ss[0] in 'КСН' or ss[0] not in 'КСН') and ss[1:] not in 'КСН':
        a.add(ss)

print(len(a))
