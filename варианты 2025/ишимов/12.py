def f(s):
    while '1' in s:
        if '18' in s:
            s = s.replace('18', '88881', 1)
        else:
            s = s.replace('1', '8888', 1)
    return s

r = f('1' + 70 * '8')
print(str(r).count('8'))