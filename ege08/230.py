import itertools

k=set()
for i in itertools.product('012345678', repeat=7):
    ss = ''.join(i)
    if '00' not in ss and '11' not in ss and ss[0] not in '037' and '22' not in ss and '33' not in ss and '44' not in ss and '55' not in ss and '66' not in ss and '77' not in ss and '88' not in ss:
        k.add(ss)
print(len(k))