import itertools

k=0

for s, i in enumerate(itertools.product('1С11Л', repeat=5), 1):
    ss = ''.join(i)
    if '11' not in ss and ss.count('С') == 1 and ss.count('Л') == 1:
        k+=1
print(k)
