import fnmatch


for i in range(103703, 4938272):
    x = i * 2025
    if fnmatch.fnmatch(str(x), '21?3*145?5'):
        print(x, i)
