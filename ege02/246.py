for x in 0, 1:
    for y in 0, 1:
        for z in 0, 1:
            for w in 0, 1:
                f = (x == (not z or y)) and not w
                print(x, y, z, w, "|", int(f))
