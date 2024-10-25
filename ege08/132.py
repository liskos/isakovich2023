import itertools

k=0

for s in itertools.permutations('1СП1КТ', r=6):
    ss = ''.join(s)
    if '11' not in ss:
        k+=1
print(k)
