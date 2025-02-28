def f(n):
    c = []
    for i in range(len(str(n))):
        if int(str(n)[i]) >= int(str(n)[i+1]):
            c.append(n)
    return c



for i in range(1395, 22717):
        print(f(i))

