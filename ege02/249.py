for x in 0, 1:
    for y in 0, 1:
        for z in 0, 1:
            for w in 0, 1:
                f = y and (x != (not z or w))
                print(x, y, z, w, "|", int(f))