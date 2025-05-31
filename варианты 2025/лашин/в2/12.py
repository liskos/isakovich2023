def f(s):
    while '52' in s or '5252' in s or '225' in s:
        if '52' in s:
            s = s.replace('52', '222', 1)
        if '5252' in s:
            s = s.replace('5252', '555', 1)
        if '225' in s:
            s = s.replace('225', '522', 1)
    return s

a = []
for n in range(3, 10001):
    r = map(int, f(10 * '5' + '2' * n))
    s = [int(x) for x in r if x % 2 == 0]
    if sum(s) % 10 == 0:
        a.append(n)
print(sum(a))