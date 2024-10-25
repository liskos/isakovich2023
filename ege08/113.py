import itertools

k = 0

for s, i in enumerate(itertools.product('П1СК11Ь', repeat=7), 1):
    ss = ''.join(i)
    if 'Ь1' not in ss and ss[0] != 'Ь' and ss.count('П') == 1 and ss.count('С') == 1 and ss.count('К') == 1 and ss.count('Ь') == 1:
        k += 1

print(k)
