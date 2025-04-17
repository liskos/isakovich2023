def f(s):
    while '21' in s or '1112' in s:
        if '21' in s:
            s = s.replace('21', '12', 1)
        else:
            s = s.replace('1112', '2', 1)
    return s


print(f('2' + '1' * 50))