import itertools

k=0
for i in itertools.product('10101011', repeat=5):
    ss = ''.join(i)
    if '11' not in ss and '00' not in ss:
        k+=1
print(k)