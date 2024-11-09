import itertools

k=0
for i in itertools.product('АНТИУОПЯ', repeat=16):
    ss = ''.join(i)
    if 'АНТИУТОПИЯ' in ss and ss[0] != 'А' and ss[-1] != 'Я':
        k+=1
print(k)
