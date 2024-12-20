import itertools

k = 0

for i in itertools.product('0123456789abcdef', repeat=5):

    ss = ''.join(i)
    if (ss[0] not in '013579bdf') and (ss[-1] not in '02468ace') and (i[0] != i[1]) and i[1] != i[2] and i[2] != i[3] and i[3] != i[4]:
        k += 1
print(k)