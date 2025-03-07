import fnmatch

for i in range(100000000, 10**9):
    if fnmatch.fnmatch(str(i), '1?34567?9') and i % 17 == 0:
        print(i, i // 17)