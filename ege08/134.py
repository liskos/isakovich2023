import itertools

k=0

for s, i in enumerate(itertools.product('В1Р1Т1', repeat=6), 1):
    ss = ''.join(i)
    if '11' not in ss:
        k+=1
print(k)
