import itertools

k = 0
for i in itertools.permutations('01212121212121212', r=6):
    ss = ''.join(i)
    if '111' not in ss and '222' not in ss and ss[0] != '0' and '000' not in ss:
        k += 1


print(k)