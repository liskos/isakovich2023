def f(s):
    while '>1' in s or '>2' in s or '>0' in s:
        if '>1' in s:
            s = s.replace('>1', '22>', 1)
        if '>2' in s:
            s = s.replace('>2', '2>', 1)
        if '>0' in s:
            s = s.replace('>0', '1>', 1)
    return s

c = []
for i in range(7, 100):
    s = f('>' + 19 * '0' + i * '1' + 19 * '2')[:-1]
    s = str(sum([int(x) for x in s]))
    if s[-1] == s[-2]:
        print(i)
        break
