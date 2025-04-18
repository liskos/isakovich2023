a = open('24data/k7c-1.txt').read()
k = 0
for i in range(len(a) - 2):
    s = a[i:i+3]
    if s[0] in 'BCD' and s[1] != s[0] and s[1] in 'BDE' and s[2] != s[1] and s[2] in 'BCE':
        k += 1
print(k)