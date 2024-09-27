def f(n):
    while '?1' in n or '?2' in n or '?3' in n:
        if '?1' in n:
            n = n.replace('?1', '123?', 1)
        if '?2' in n:
            n = n.replace('?2', '4?1', 1)
        if '?3' in n:
            n = n.replace('?3', '2?12', 1)
    return n

b = 0
s = f('?' + ('1' * 302) + (109 * '2') + ('3' * 224))
for i in s[:-1]:
    b += int(i)
print(b)