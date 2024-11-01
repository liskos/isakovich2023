import itertools

a = set()

for s, i in enumerate(itertools.product('ДЖОБС', repeat=6), 1):
    ss = ''.join(i)
    if ss.count('А') <= 2 and ss.count('Д') == 1 and ss.count('О') == 1 and ss.count('С') == 1:
        a.add(ss)

print(len(a))