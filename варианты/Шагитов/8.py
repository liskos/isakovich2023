import itertools

for i, s in enumerate(itertools.product('ИНФОРМАТК', repeat=6), 1):
    ss = ''.join(s)
    if "ФОРМАТ" in ss:
        print(i, ss)