import fnmatch

for i in range(1592608//1996, 10**10//1996+1):
    x = i * 1996
    if fnmatch.fnmatch(str(x), '1592*6?8'):
        print(x, i)

# 1592464688 797828
# 1592484648 797838