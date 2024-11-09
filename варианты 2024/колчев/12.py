def f(s):
    while '111' in s or '88' in s:
        if '88' in s:
            s = s.replace('88', '1111')
        if '111' in s:
            s = s.replace('111', '8')
    return s


print(f('1' * 81))