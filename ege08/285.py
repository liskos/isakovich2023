import itertools

k=0
for i in itertools.product('0123456789AB', repeat=6):
    ss = ''.join(i)
    if int(ss, 12) % int(ss[0], 12) == 0:
        k+=1
print(k)
