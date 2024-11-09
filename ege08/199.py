import itertools

k = 0
for i in itertools.product('ABCDE', repeat=4):

    if set(i[:1]) <= set("AE") and set(i[1:])<= set("BCD") and g[0] <= g[1] and s[0] >= s[1]:
        k+=1
    elif len(g) == 1 and s[0] >= s[1] >= s[2]:
        k+=1
    elif len(g) == 0 and s[0] >= s[1] >= s[2] >= s[3]:
        k+=1
    elif len(g) == 3 and g[0] <= g[1] <= g[2]:
        k+=1
    elif len(g) == 4 and g[0] <= g[1] <= g[2] <= g[3]:
        k+=1
print(k)