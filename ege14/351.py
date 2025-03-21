

for x in range(1, 19):
    r = int('01418', 13) + (x * 13 ** 4) + int('10037', 14) + (x * 14 ** 3)
    d = int('20209', 19) + (x * 19 ** 3)
    if r == d:
        print(d)