def f(s):
    while '1' in s:
        if '10' in s:
            s = s.replace('10', '0001', 1)
        else:
            s = s.replace('1', '000', 1)
    return s

a = f('1' + 90 * '0')
print(a.count('0'))