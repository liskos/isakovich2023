for x in '0123456789A':
    for y in '123456789ABCD':
        s = int(f'{y}23{x}C', 14) + int(f'A{x}910', 11)
        if s % 23 == 0:
            print(int(x, 11) + int(y, 14), s // 23)