
def f(a, b):
    if int(a, 2) < int(b, 2):
        return 0
    if a == b:
        return 1
    if a == '1' + (len(a) - 1) * '0':
        return f(bin(int(a, 2) - 1)[2:], b)
    return f(bin(int(a, 2) - 1)[2:], b) + f('1' + (len(a) - 1) * '0', b)


print(f('10001', '1'))