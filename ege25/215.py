def tr(n):
    a = []
    while n > 0:
        a.append(str(n % 3))
        n = n // 3
    return ''.join(a)[::-1]



import fnmatch

for i in range(10000, 10**6):
    if fnmatch.fnmatch(tr(i), '2?1?2?1?2?1') and int(tr(i), 3) % 148 == 0:
        print(i, int(tr(i), 3) // 148)