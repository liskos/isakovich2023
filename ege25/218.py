def s(n):
    a = []
    while n > 0:
        a.append(n % 9)
        n = n // 9
    return a




import fnmatch

for i in range(3045803,10**9):
    if fnmatch.fnmatch(str(i), '3?458*3') and sorted(s(i), reverse=True) == s(i):
        print(i, sum(s(i)))