def f(s):
    while '<1' in s or '<2' in s or '<3' in s:
        if '<1' in s:
            s = s.replace('<1', '111<')
        if '<2' in s:
            s = s.replace('<2', '31<3')
        if '<3' in s:
            s = s.replace('<3', '12<1')
    return s


for i in range(1, 10):
    r = f('<<' + 13 * '1' + i * '2' + 17 * '3')
    print(sum([int(x) for x in r[:-2]]))