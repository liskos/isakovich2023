import itertools

k=0
for i in itertools.product('12121', repeat=4):
    ss = ''.join(i)
    if '11' not in ss and '22' not in ss:
        k+=1
print(k)