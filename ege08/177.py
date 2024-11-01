import itertools

a = set()

for s in itertools.product('ДЖОБС', repeat=6):
    ss = ''.join(s)
    if ss.count('Ж') <= 2 and ss.count('Д') == 1 and ss.count('О') == 1 and ss.count('С') == 1:
        a.add(ss)

print(len(a))