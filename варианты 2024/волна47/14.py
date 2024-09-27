a = []
def sh(n):
    t = "012345"
    s = ""
    while n > 0:
        s = t[n % 6] + s
        n = n // 6
    return s
for i in range(2031):
    s = (6 ** 260) + (6 ** 160) + (6 ** 60) - i
    if str(sh(s)).count('0') == 202:
        a.append(int(sh(i), 6))
print(max(a))
