import itertools

k=0

for s, i in enumerate(itertools.product('1СП1КТ', repeat=6), 1):
    ss = ''.join(i)
    if '11' not in ss:
        k+=1
print(k)
