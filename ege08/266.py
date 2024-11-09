import itertools

k = 0
for s, i in enumerate(itertools.product('ДЕЙНПТЬЯ', repeat=4), 1):
    ss = ''.join(i)
    if ss.count('Е') + ss.count('Я') == 0 and len(set(i)) == 4:
        print(ss)
        k+=1

print(k)