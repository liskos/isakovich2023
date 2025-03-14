import fnmatch

k=0
for i in range(123407, 10**8):
    if fnmatch.fnmatch(str(i), '12*4?65') and i % 161 == 0:
        print(i, i // 161)