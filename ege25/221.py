import fnmatch


def prime(n):
    a = [True] * n
    a[0] = False
    a[1] = False
    for i in range(2, n):
        for j in range(i ** 2, n, i):
            a[j] = False
    b = sorted([str(i) for i in range(n) if a[i]])
    return b


for i in range(4679000, 10**10):
    if fnmatch.fnmatch(''.join(prime(i)), '27*39?') or fnmatch.fnmatch(''.join(prime(i)), '34*2?7'):
        print(i, max(prime(i)))