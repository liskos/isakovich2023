import itertools

k=set()
for i in itertools.product('012345678', repeat=7):
    ss = ''.join(i)
    if '000' not in ss[4:] and '111' not in ss[4:] and ss[0] not in '0246' and '222' not in ss[4:] and '333' not in ss[4:] and '444' not in ss[4:] and '555' not in ss[4:] and '666' not in ss[4:] and '777' not in ss[4:] and '888' not in ss[4:]:
        k.add(ss)
print(len(k))