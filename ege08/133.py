import itertools

k=0

for s, i in enumerate(itertools.product('ЗД1Н11', repeat=6), 1):
    ss = ''.join(i)
    if '11' not in ss and ss.count('Д') == 1 and ss.count('Н') == 1:
        k+=1
print(k)
