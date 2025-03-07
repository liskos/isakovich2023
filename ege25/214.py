import fnmatch

for i in range(1, 10**6):
    if fnmatch.fnmatch(bin(i)[2:], '1?1?1?1?1??1') and int(bin(i), 2) % int('101101', 2) == 0:
        print(i, int(bin(i), 2) // int('101101', 2))