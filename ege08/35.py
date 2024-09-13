import itertools



for s, i in enumerate(itertools.product('ДКМО', repeat=5), 1):
    ss = ''.join(i)
    if 'ДОМОК' in ss or 'КОМОД' in ss:
        print(s, ss)
print(493 - 238 + 2)


