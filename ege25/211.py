import fnmatch

for i in range(10000000, 10**10):
    if fnmatch.fnmatch(hex(i)[2:], '1?DED?CED') and int(hex(i), 16) % int('79', 16) == 0:
        print(i, int(hex(i), 16) // int('79', 16))