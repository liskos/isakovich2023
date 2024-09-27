import itertools

for i, s in enumerate(itertools.product('АГИМРТ', repeat=4), 1):
    ss = ''.join(s)
    if "МАРТ" in ss or "ТИГР" in ss:
        print(i, ss)
print(1163-678-1)