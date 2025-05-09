import itertools

k = 0
for i in itertools.permutations(range(17), r=6):
    ss = ''.join([str(x % 2) for x in i])
    if '111' not in ss and '000' not in ss and i[0] != 0:
        k += 1


print(k)