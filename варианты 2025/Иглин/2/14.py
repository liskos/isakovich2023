c = []
for x in range(1, 34):
    r = int('GP4502', 34) + (x * 34) + (int('P70', 34) + (x * 34 ** 0)) * (int('AI98', 34) + (x * 34 ** 4))
    if r % 13 == 0:
        print(x, r // 13)

