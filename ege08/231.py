import itertools

k=set()
for i in itertools.product('012345678', repeat=7):
    ss = ''.join(i)
    if '000' not in ss and '111' not in ss and ss[-1] not in '347' and '222' not in ss and '333' not in ss and '444' not in ss and '555' not in ss and '666' not in ss and '777' not in ss and '888' not in ss and ss[0] != '0':
        k.add(ss)
print(len(k))