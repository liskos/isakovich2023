x = 4 ** 644 + 4 ** 322 + 16 ** 35 - 64 ** 3
k = 0
t = []
def ch(n):
    t = "0123"
    s = ""
    while n > 0:
        s = t[n % 4] + s
        n = n // 4
    return s
n = ch(x)
print(n.count('3'))