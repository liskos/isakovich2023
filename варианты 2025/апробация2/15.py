for a in range(1, 100):
    for a1 in range(10, 200):
        if all(not(x in range(17, 59)) or not(((x in range(29, 81)) and not(x in range(a, a1)))) or not(x in range(17, 59)) for x in range(100)):
            print(a, a1)
            break
