
a = []
for i in range(100000, 1000000, 5):
    s = str(i)
    for x in "2468":
        s = s.replace(x, "0")
    for y in "3579":
        s = s.replace(y, '1')
    if len(set(str(i))) == 6 and ('00' not in s) and ('11' not in s):
        a.append(i)
print(len(a))
