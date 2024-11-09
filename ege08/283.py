import itertools

k=0
for i in itertools.product('АНТИУОПЯ', repeat=16):
    ss = ''.join(i)
    if 'АНТИУТОПИЯ' in ss:
        k+=1
print(k)
