import itertools

k = 0
for i in itertools.product('001Г', repeat=6):
    if i[0] == '0' and i[-1] == 'Г':
        k+=1
print(k)