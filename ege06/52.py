import math

k = 0
for x in range(0, int(300*math.cos(math.pi / 6))+1):
    for y in range(-300, 300):
        if -x * math.tan(math.pi/6)<= y <= x * math.tan(math.pi/6):
            k += 1
print(k)