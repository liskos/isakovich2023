a = open('24.txt').read()
k = 0
m = 0
left = 0
for right in range(len(a)+1):
    if a[right-3:right] == 'LND':
        k+=1
    while k > 10000:
        if a[left:left+3] == 'LND':
            k-=1
        left += 1
    left2 = left
    while a[left2] != a[right-1]:
        left2 += 1
    m = max(m, right-left2)
print(m)