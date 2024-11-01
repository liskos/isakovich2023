import itertools
a = set()

for i in itertools.product('1234', repeat=5):
    if i[0] != '1' and i[0] != i[1] and i[3] != i[4]:
        a.add(i)
print(len(a))