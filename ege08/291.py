import itertools

k=0
for i in itertools.product('101020311', repeat=5):
    ss = ''.join(i)
    if '323' not in ss and '020' not in ss:
        k+=1
print(k)
