import itertools

k=0

for s, i in enumerate(itertools.product('В1Р1Н', repeat=5), 1):
    ss = ''.join(i)
    if '11' not in ss and ss.count('В') == 1 and ss.count('Р') == 1 and ss.count('Н') == 1:
        k+=1
print(k)
