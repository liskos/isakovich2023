import itertools

a = set()

for s, i in enumerate(itertools.product('КЛЕЙ', repeat=6), 1):
    ss = ''.join(i)
    if ss.count('Й') <= 1 and ss[-1] != 'Й' and ss[0] != 'Й' and 'ЙЕ' not in ss and 'ЕЙ' not in ss:
        a.add(ss)

print(len(a))