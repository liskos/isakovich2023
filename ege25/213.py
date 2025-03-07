import fnmatch

for i in range(100000000, 10**10):
    if fnmatch.fnmatch(oct(i)[2:], '1?345?700') and int(oct(i), 8) % int('114', 8) == 0:
        print(i, int(oct(i), 8) // int('114', 8))