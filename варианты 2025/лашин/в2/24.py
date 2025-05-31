import re
a = open('24.txt').read()
def f(s):
    if '10' in s:
        return False
    for i in range(1, 10):
        i2 = 10 - i
        pat = rf'{i}[+]{i2}'
        if re.search(pat, s):
            return False
    for i in range(1, 10):
        for i2 in range(1, 10):
            for i3 in range(1, 10):
                if i + i2 + i3 == 10:
                    pat = rf'{i}[+]{i2}[+]{i3}'
                    if re.search(pat, s):
                        return False

    return True

numb = r'(([1-9][0-9]+)|[1-9])'
pattern = rf'({numb}[+])*{numb}'

r = [x.group() for x in re.finditer(pattern, a)]
r.sort(key=len, reverse=True)
k = 0
for s in r:
    if f(s):
        print(len(s), s)
        k += 1
        if k == 10:
            break