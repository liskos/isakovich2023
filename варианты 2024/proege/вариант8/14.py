n = 4 * 3125 ** 2019 + 3 * 625 ** 2020 - 2 * 125 ** 2021 + 25 ** 2022 - 4 * 5 ** 2023 - 2024
a = 0
while n > 0:
    if n % 25 > 10:
        a += 1
    n = n // 25
print(a)