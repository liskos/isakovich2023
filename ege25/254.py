import fnmatch

for i in range(1, 10**7):
    if fnmatch.fnmatch(str(i), '9*?') and i % 9998 == 0:
        print(i, i // 9998)