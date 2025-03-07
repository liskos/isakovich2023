import fnmatch

for i in range(10000000, 10**10):
    if fnmatch.fnmatch(hex(i)[2:], '1?DED?BABA') and int(hex(i), 16) % int('BA', 16) == 0:
        print(i, int(hex(i), 16) // int('BA', 16))