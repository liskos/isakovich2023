import fnmatch

for i in range(1000000, 10**9):
    if fnmatch.fnmatch(str(i), '123*567?') and i % 169 == 0:
        print(i, i // 169)