import itertools
a = []
for i in itertools.product('0123456', repeat=5):
    if i[0] != '0' and i.count('5') == 1 and i[0] != i[2] and i[1] != i[3] and i[2] != i[4]:
        a.append(i)
print(len(a))
