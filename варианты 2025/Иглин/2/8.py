import itertools
k = 0
for i in itertools.product('EGPWZ', repeat=6):
    ss = ''.join(i)
    if ss.count('E') <= 2:
        k+=1
        if 'EZGGWP' in ss:
            print(k, ss)