import itertools
a = set()

for i in itertools.product('1234', repeat=5):
    if i[0] != '1' and i != i[::-1]:
        a.add(i)
print(len(a))