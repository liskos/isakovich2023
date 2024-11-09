import itertools
k=0
for i in itertools.product('0123456789', repeat=7):
    if int(i[1]) ** 2 == int(i[0]) and int(i[2])** 2 == int(i[0]) and int(i[-2]) ** 3 == int(i[-1]) and i[0] != '0':
        k+=1
print(k)