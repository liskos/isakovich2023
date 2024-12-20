import itertools

k = 0

for i in itertools.product('7101010101010101', repeat=5):
    ss = ''.join(i)
    if ss[0] != '7' and '77' not in ss and '00' not in ss and '11' not in ss and ss[0] != '1' and ss[-1] != '0':
        k += 1
print(k)