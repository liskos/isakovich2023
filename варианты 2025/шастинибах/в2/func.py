def func(kl_a, kl_b):
    xa = 0
    ya = 0
    xb = 0
    yb = 0
    s = 10 ** 6
    for x1, y1 in kl_a:
        for x2, y2 in kl_b:
            t = ((x2 - x1)**2 + (y2 - y1)**2) ** 0.5
            if t < s:
                xa = x1
                ya = y1
                xb = x2
                yb = y2
                s = t
    return s, xa+xb, ya+yb