for x in 0, 1:
    for y in 0, 1:
        for z in 0, 1:
            for w in 0, 1:
                        f = w or (not x or y) and (not(not z) or x)
                        if not f:
                            print(x, y, z,w,"|", int(f))
