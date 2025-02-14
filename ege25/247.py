import fnmatch

k=0
for i in range(700011, 10**10, 13):
    if not(fnmatch.fnmatch(str(i), '*0??3*')) and not(fnmatch.fnmatch(str(i), '*4??2')) and not(fnmatch.fnmatch(str(i), '*1*')):
        k+=1
        print(i, sum([int(x) for x in str(i)]))
        if k == 5:
            break