import itertools

a = set()

for s, i in enumerate(itertools.product('КАЛИЙ', repeat=6), 1):
    ss = ''.join(i)
    if ss.count('Й') <= 1 and ss[-1] != 'Й' and ss[0] != 'Й' and 'ЙИ' not in ss and 'ИЙ' not in ss:
        a.add(ss)

print(len(a))