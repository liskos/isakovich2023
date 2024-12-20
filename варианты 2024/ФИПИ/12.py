def f(b):
    while '1111' in b or '8888' in b:
        if '1111' in b:
            b = b.replace('1111', '8', 1)
        else:
            b = b.replace('8888', '11', 1)
    return b


print(f('8'*82))