import itertools

k=set()
for i in itertools.product('ОНИКС', repeat=6):
    ss = ''.join(i)
    if ss.count('С') == 3 and ss.count('О') == 1:
        k.add(ss)
print(len(k))