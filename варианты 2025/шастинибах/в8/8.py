import itertools
c = set()

for i in itertools.permutations('ПАРИЖАНКА', r=9):
    ss = ''.join(i)
    sh = ss.replace("И", 'А')
    if sh.count('АА') == 1:
        c.add(ss)
print(len(c))