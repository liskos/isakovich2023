import itertools

c = [0]*21
for i in itertools.product('01', repeat=20):
    ss = ''.join(i)
    c[ss.count('0')] += 1
for i in range(21):
    print(i, c[i])