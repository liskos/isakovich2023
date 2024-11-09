import itertools

a = set()
for x in range(3, 10):

    for i in itertools.product('СЕПИЯ', repeat=x):
        ss = ''.join(i)
        if ss.count('Е') <= 2 and ss.count('И') <= 2 and ss.count('Я') <= 2 and 'С' not in ss[1:] and 'П' not in ss[1:]:
            a.add(ss)
print(len(a))
