import itertools


k = 0
for i in itertools.product('012141618', repeat=5):
    s = ''.join(i)
    if s[0] != '0' and s.count('0') == 1 and '10' not in s and '01' not in s and '101' not in s:
        k += 1
print(k)