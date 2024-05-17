for x in '1234567':
    s1 = f'{x}1{x}'
    s2 = f'{x}3{x}3'
    s = int(s1, 16) + int(s2, 8)
    print(s, x)