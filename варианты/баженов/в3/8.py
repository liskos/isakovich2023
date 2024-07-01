import itertools

k = 0
for i, s in enumerate(itertools.product('ДОСТЕВКИЙ', repeat=5), 1):
    ss = ''.join(s)
    if ss.count('К') > 2:
        print(k, ss)
        k += 1


