import itertools
a = []
for i in itertools.product('0123456789ab', repeat=5):
    s = ''.join(i)
    if s[0] != '0' and s.count('7') == 1 and s.count('9') + s.count('a') + s.count('b') <= 3:
        a.append(s)
print(len(a))