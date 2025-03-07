import fnmatch

for i in range(123450608, 10**9):
    if fnmatch.fnmatch(str(i), '12345?6?8') and i % 17 == 0:
        print(i, i // 17)