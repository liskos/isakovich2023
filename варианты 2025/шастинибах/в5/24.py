s = open('24.txt').read()
a = []
print(len(s))
for i in range(len(s)):
    print(i)
    if s[i] == 'L':
        j = i + 1
        while s[j] != 'O' and j < len(s):
            j = j+1
            if s[j] == "L":
                continue
        if s[j] != 'O':
            break
        while s[j] != 'V' and j < len(s):
            j = j+1
        if s[j] != 'V':
            break
        while s[j] != 'E' and j < len(s):
            j = j+1
        if s[j] != 'E':
            break
        a.append(s[i:j+1])
    if i % 50000 == 0:
        print(i // 50000, "%")
a = sorted(a, key=len, reverse=True)
print(a)
print(len(a), a[0])