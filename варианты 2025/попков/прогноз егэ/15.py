# p = range(84, 341 + 1)
# q = range(198, 412 + 1)
# a1_best = 0
# a2_best = 500
# for a1 in range(500):
#     for a2 in range(a1, 500):
#         a = range(a1, a2+1)
#         if all([(not((x in p) == (x in q)) and not(x in a))==False for x in range(1, 500)]):
#             if a2 - a1 < a2_best - a1_best:
#                 a1_best = a1
#                 a2_best = a2
# print(a1_best, a2_best, a2_best - a1_best)


k = 10
p = range(84 * k, 341 * k + 1)
q = range(198 * k, 412 * k + 1)
a1_best = 0
a2_best = 500 * k
for a1 in range(82 * k, 87 * k):
    for a2 in range(410 * k, 414 * k):
        a = range(a1, a2+1)
        if all([(not((x in p) == (x in q)) and not(x in a))==False for x in range(1, 500 * k)]):
            if a2 - a1 < a2_best - a1_best:
                a1_best = a1
                a2_best = a2
print(a1_best / k, a2_best / k, (a2_best - a1_best) / k)
