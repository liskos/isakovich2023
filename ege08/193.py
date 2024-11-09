import itertools

a=set()
for i in itertools.product('01234', repeat=6):
    if i[0] == '3':
        a.add(i)
print(len(a))