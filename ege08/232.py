import itertools

k=set()
for i in itertools.product('012345678', repeat=7):
    ss = ''.join(i)
    if '00' not in ss[5:] and '11' not in ss[5:] and ss[0] not in '026' and '22' not in ss[5:] and '33' not in ss[5:] and '44' not in ss[5:] and '55' not in ss[5:] and '66' not in ss[5:] and '77' not in ss[5:] and '88' not in ss[5:]:
        k.add(ss)
print(len(k))