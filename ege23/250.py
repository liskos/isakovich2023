for i in range(1, 100):
    for a in range(1, 100):
        f = ((5 + 3 + i) * a + i + 3) * a + i
        if f == 329:
            print(a + i)