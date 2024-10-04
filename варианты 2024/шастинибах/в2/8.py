import itertools
k = 0
for i, s in enumerate(itertools.product('ЛЮСТРА', repeat=5), 1):
    ss = ''.join(s)
    if ss.count('Ю') <= 2 and 'Л' not in ss[-1] and 'С' not in ss[-1] and 'Т' not in ss[-1] and 'Р' not in ss[-1]:
        k+=1
        print(ss, i)
print(k)
