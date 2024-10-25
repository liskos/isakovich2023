import itertools

k = 0

for s, i in enumerate(itertools.product('1ЙСБ1РГ', repeat=7), 1):
    ss = ''.join(i)
    if 'Й1' not in ss and ss[0] != 'Й' and ss.count('Й') == 1 and ss.count('С') == 1 and ss.count('Б') == 1 and ss.count('Р') == 1 and ss.count('Г') == 1:
        k += 1

print(k)
