def s(n):
    a = []
    while n > 0:
        a.append(str(n % 7))
        n = n // 7
    return ''.join(a)[::-1]

def s1(n):
    a = []
    while n > 0:
        a.append(n % 7)
        n = n // 7
    return a


import fnmatch

for i in range(1058606, 2 * 10**9):
    if fnmatch.fnmatch(str(i), '1*586?6') and int(s(i)) == int(s(i)[::-1]):
        print(i, sum(s1(i)))