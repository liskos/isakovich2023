import itertools

k=0
for i in itertools.product('101020111', repeat=5):
    ss = ''.join(i)
    if ss.count('1') + ss.count('2') < ss.count('0') and '020' not in ss:
        k+=1
print(k)
