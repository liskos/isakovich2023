import itertools
a = set()

for i in itertools.product('1234', repeat=4):
    if i[0] != '1' and i[1] != i[2]:
        a.add(i)
print(len(a))