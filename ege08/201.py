import itertools

a=set()
for i in itertools.product('0123456789ABCDEF', repeat=5):
    ss = ''.join(i)
    for i in range(2):
        if ss[i] >= ss[i+1]:
            print(ss)
            a.add(ss)
print(len(a))