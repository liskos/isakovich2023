

a = [int(x) for x in open('17data/17-257.txt')]
m7 = [x for x in a if x % 2 == 0]
m13 = [x for x in a if x % 2 > 0]

for i in range(len(a)):
    if min(m7) > min(m13):
        print(len(m7), min(m7))
        break
    else:
        print(len(m13), min(m13))
        break
