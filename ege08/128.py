import itertools

k=0

for s, i in enumerate(itertools.product('1П1РТ', repeat=5), 1):
    ss = ''.join(i)
    if '11' not in ss and ss.count('П') == 1 and ss.count('Р') == 1 and ss.count('Т') == 1:
        k+=1
print(k)
