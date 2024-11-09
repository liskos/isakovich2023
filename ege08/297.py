import itertools

k=0
for i in itertools.product('01234567', repeat=5):
    ss = ''.join(i)
    if ss[0] != '0' and ('000' in ss in '111' in ss or '222' in ss or '333' in ss or '444' in ss or '555' in ss or '666' in ss or '777' in ss):
        k+=1
print(k)
