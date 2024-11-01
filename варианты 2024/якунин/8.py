import itertools

k=0
for i in itertools.product('01234', repeat=6):
    if i[0] != '0':
        k+=1
print(k)