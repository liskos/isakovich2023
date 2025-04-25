import fnmatch

for i in range(7993, 10**10, 7993):
    if fnmatch.fnmatch(str(i), '4*4736*1') and i % 7993 == 0:
        print(i, i // 7993)

