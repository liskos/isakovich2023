import ast


def ch(n):
    a = []
    while n > 0:
        a.append(str(n % 4))
        n = n // 4
    return ''.join(a)[::-1]

a = []
for x in range(1, 3001):
    r = 4 ** 210 + 4 ** 110 - x
    a.append(ch(r).count('0'))
    if ch(r).count('0') == 105:
        print(ch(r).count('0'), x)