import itertools

a = set()
for s, i in enumerate(itertools.product('КРЫША', repeat=8), 1):
    ss = ''.join(i)
    if ss.count('Ы') <= 2 and ss.count('А') <= 2 and (ss[0] in 'КРШ' or ss[0] not in 'КРШ') and ss[1:] not in 'КРШ':
        a.add(ss)

print(len(a))
