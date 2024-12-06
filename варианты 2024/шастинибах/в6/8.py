import itertools

c = []
for i in itertools.product('01', repeat=20):
    ss = ''.join(i)
    if int(ss, 2) > 99999:
        c.append(ss.count('0'))
print(c.count(19))