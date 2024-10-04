s = 12545456
a = [int(i) for i in str(s)]
print(sum(a))
b =sum(map(int, str(s)))
print(b)
c = 0
while s > 0:
    c += s % 10
    s = s // 10
print(c)