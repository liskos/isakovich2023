import itertools

k=0
for i in itertools.product('0123456789ABCDEF', repeat=5):
    ss = ''.join(i)
    if ss[0] not in '0F' and ss[-1] == 'A' and ss.count('3B') == 1:
        k+=1
print(k)