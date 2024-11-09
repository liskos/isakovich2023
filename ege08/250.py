import itertools


for s, i in enumerate(itertools.product('ЕКЛОСТ', repeat=5), 1):
    ss = ''.join(i)
    if ss[0] == 'С' and 'ОО' in ss:
        print(ss, s)
        break
