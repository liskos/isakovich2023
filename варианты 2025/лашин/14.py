def ch(a):
    s = []
    while a > 0:
        s.append(a%4)
        a = a // 4
    return s
print((4 ** 8 + 4 ** 5-263168))
for x in range(1, 10000000):
    r = 4 ** 8 + 4 ** 5 - x
    if ch(r).count(0) == 8 and len(ch(r)) == 9:
        print(x, ch(r))
    if len(ch(r)) == 8:
        break
