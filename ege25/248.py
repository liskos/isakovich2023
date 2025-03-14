import fnmatch

k=0
for i in range(123407, 10**8):
    if fnmatch.fnmatch(str(i), '1234*7') and i % 141 == 0:
        print(i, i // 141)