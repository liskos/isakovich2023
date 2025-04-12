

def f(s):
    while '31' in s or '211' in s or '1111' in s:
        if '31' in s:
            s = s.replace('31', '1', 1)
        if '211' in s:
            s = s.replace('211', '13', 1)
        if '1111' in s:
            s = s.replace('1111', '2', 1)
    return s


for i in range(4, 10000):
    x = f('3' + i * '1')
    if sum(map(int, x)) == 15:
        print(i)
        break