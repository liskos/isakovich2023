import itertools


for i in itertools.permutations('1234567890', r=5):
    ss = ''.join(i)
    if ss[0] == '0' and int(ss) % 5 == 0:
        print(ss)

