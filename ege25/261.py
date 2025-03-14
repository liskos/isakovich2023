import fnmatch



def f(n):
    a = set()
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            a.add(n // i)
            a.add(i)
    return a



for i in range(1, 17 * 10**6 + 1):
    if fnmatch.fnmatch(str(i), '*1?*?68*') and i % 161 == 0:
        print(i, i // 161)