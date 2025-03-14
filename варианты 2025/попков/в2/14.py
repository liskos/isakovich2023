for x in '123456789abcdefghijklmnopqrstuvwxy':
    s = int(f'6{x}qr{x}', 35) + int(f'{x}59sh', 35) + int(f'ph{x}69yw', 35)
    rez = max([[str(s).count(str(i)), i] for i in range(1, 10)], key=lambda x:(x[0], x[1]))[1]
    if s % (rez ** 2) == 0:
        print(s // (rez ** 2))
