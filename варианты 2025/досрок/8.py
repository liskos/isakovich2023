import itertools
a = set()
k = 0
for i in itertools.product('ДГИАШЭ', repeat=5):
    if i[0] not in 'ИАЭ' and i[-1] not in 'ДГШ':
        print(i)
        k+=1
        a.add(i)
print(len(a))