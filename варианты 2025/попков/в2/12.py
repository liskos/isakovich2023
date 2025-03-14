def f(s):
    while '<1' in s or '<2' in s or '<3' in s:
        if '<1' in s:
            s = s.replace('<1', '111<', 1)
        if '<2' in s:
            s = s.replace('<2', '31<3', 1)
        if '<3' in s:
            s = s.replace('<3', '12<1', 1)
    return s

def is_prime(n):
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True


for i in range(1, 10):
    r = f('<<' + 13 * '1' + i * '2' + 17 * '3')
    s = sum([int(x) for x in r[:-2]])
    if is_prime(s):
        print(i, s)
        break