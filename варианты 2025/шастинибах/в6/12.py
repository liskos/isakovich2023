def f(s):
    while '>3' in s or '>5' in s or '>7' in s:
        if '>3' in s:
            s = s.replace('>3', '55>', 1)
        if '>5' in s:
            s = s.replace('>5', '5>3', 1)
        if '>7' in s:
            s = s.replace('>7', '3>5', 1)
    return s
c = 555555555555555555555555555555555555555555555555553555355535553555355535553555355535553555
t = 0
print(f('>' + 10 * '3' + 10 * '5' + 10 * '7'))
while c > 0:
    t += c % 10
    c = c // 10
print(t)