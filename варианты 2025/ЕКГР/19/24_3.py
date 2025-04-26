s = open("24.txt").read()
import time
t1 = time.time()

a1 = [i for i in range(len(s)) if s[i:i+3] == "RSQ"]   # поиск первого вхождения RSQ
a2 = [] # список индексов символов после RSQ не равных Q
for i in a1:
    j = i + 3
    if j == len(s): break
    while s[j] == "Q":
        j += 1
    a2.append(j)
m = 10**10
k = 130
for i1, i2 in zip(a1,a2[k-1:]): # берем пары индексов между которыми 130 RSQ и последний не Q
    m = min(m , i2 - i1 + 1) # включая края
print(m)


print(time.time() - t1)