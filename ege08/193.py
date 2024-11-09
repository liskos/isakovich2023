import itertools

a=set()
for i in itertools.product('01234', repeat=6):
    if i[0] == '3' and int(''.join(i), 5) % 2 == 0:
        a.add(i)
print(len(a))