def f(s):
    while '>3' in s or '>2' in s or '>0' in s:
        if '>3' in s:
            s = s.replace('>3', '22>', 1)
        if '>2' in s:
            s = s.replace('>2', '2>', 1)
        if '>0' in s:
            s = s.replace('>0', '3>', 1)
    return s


c = []
for i in range(1, 1000):
    c.append(sum(map(int, '>' + '0' * 17 + i * '3' + 17 * '2')))
print()