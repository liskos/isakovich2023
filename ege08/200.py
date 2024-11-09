import itertools

a=set()
for i in itertools.product('0123456789', repeat=3):
    ss = ''.join(i)
    for i in range(2):
        if int(ss[i]) >= int(ss[i+1]):
            print(ss)
            a.add(ss)
print(len(a))