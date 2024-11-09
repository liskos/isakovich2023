import itertools

k=0
for i in itertools.product('1234567', repeat=):
    ss = ''.join(i)
    for x in ss:
        
    print(ss)
    k+=1
print(k)