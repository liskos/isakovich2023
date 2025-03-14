import fnmatch

k=0
for i in range(1, 10**8):
    if fnmatch.fnmatch(str(i), '12345*76') and i % 73 == 0:
        print(i, i // 73)