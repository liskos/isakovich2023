import itertools

k=0
for i in itertools.product('010101', repeat=5):
    ss = ''.join(i)
    if '11' in ss or '00' in ss:
        k+=1
print(k)