import itertools

for i, s in enumerate(itertools.product('АПРСУ', repeat=5), 1):
    ss = ''.join(s)
    if (ss.count('У') <= 1) and ('АА' not in ss):
        print(i, ss)


