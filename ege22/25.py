import sys
sys.stdin = open("25.txt")
b = dict()
c = dict()
for _ in range(500):
    s = input().split()
    id = int(s[0])
    t = int(s[1])
    a = list(map(int, s[2:]))
    b[id] = a
    c[id] = t

time = dict()
time[0] = 0
print(time)
for i in range(1, 501):
    m = 0
    for x in b[i]:
        m = max(m, time[x])
    time[i] = m + c[i]
print(max(time.values()))