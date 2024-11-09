import itertools

k=set()
for i in itertools.product('01234567', repeat=5):
    ss = ''.join(i)
    if ss.count('6') == 1 and ss[0] != '0':
        if ss.find('6') == 0:
            if ss[ss.find('6') + 1] not in '1357':
                k.add(ss)
        if ss.find('6') == 4:
            if ss[ss.find('6') - 1] not in '1357':
                k.add(ss)
        if 0 < ss.find('6') < 4:
            if ss[ss.find('6') - 1] not in '1357' and ss[ss.find('6') + 1] not in '1357':
                k.add(ss)
print(len(k))