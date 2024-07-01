for x in 0, 1:
    for y in 0, 1:
        for z in 0, 1:
            for w in 0, 1:
                f = ((not y or w) and (not w or z)) == ((z and x) or (x and y))
                if f:
                    print(x,y,z,w,"|", int(f))
