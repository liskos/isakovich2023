import itertools

k = 0

for s in itertools.permutations('1ЙСБ1РГ'):
    ss = ''.join(s)
    if 'Й1' not in ss and ss[0] != 'Й':
        k += 1

print(k)
