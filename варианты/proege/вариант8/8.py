import itertools

a = []
for i in itertools.product('01234567', repeat=5):
    if i.count('1') == 0 and i[0] != i[1] and i[1] != i[2] and i[2] != i[3] and i[3] != i[4] and int(i[0]) % 2 != int(i[1]) % 2 or int(i[1]) % 2 != int(i[2]) % 2 or int(i[2]) % 2 != int(i[3]) % 2 or int(i[3]) % 2 != int(i[4]) % 2:
        a.append(i)
print(len(a))