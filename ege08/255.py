import itertools

k=0
for i in itertools.product('01234567', repeat=5):
    ss = ''.join(i)
    if ss[0] not in '07' and ss.count('65') + ss.count('56') == 1 and int(ss) % 2 == 0:
        k+=1
print(k)