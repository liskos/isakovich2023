def f(b):
    while '00' not in b:
        b = b.replace('01', '130', 1)
        b = b.replace('02', '1013', 1)
        b = b.replace('03', '210', 1)
    return b

print(f())

