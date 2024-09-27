def f(n):
    s = str(n)
    if s.count("1") % 4 == 0:
        s = "1" + s[:-2]
    else:
        s += s.count("1") % 4 * 3
    return s


