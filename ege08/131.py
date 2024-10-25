import itertools

k=0

for s, i in enumerate(itertools.product('1Р11Л', repeat=5), 1):
    ss = ''.join(i)
    if '11' not in ss:
        k+=1
print(k)
