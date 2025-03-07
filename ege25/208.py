import fnmatch

for i in range(100000, 10**6):
    if fnmatch.fnmatch(str(i), '12*45*') and i % 51 == 0:
        print(i, i // 51)