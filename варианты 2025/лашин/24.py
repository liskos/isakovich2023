def f(x):
    r = []
    for i in range(len(x)):
        if x[i] == '(':
            k1 = 1
            k2 = 0
            for j in range(i+1, len(x)):
                if x[j] == '(':
                    k1 += 1
                elif x[j] == ')':
                    k2 += 1
                if k1 == k2:
                    r.append(x[i:j+1])
                    break
    return r



s = open('24.txt').readline()
while '++' in s:
    s = s.replace('++', '+ +')
while '()' in s:
    s = s.replace('()', ' ')
while ')(' in s:
    s = s.replace(')(', ' ')
while '(+' in s:
    s = s.replace('(+', ' ')
while '+)' in s:
    s = s.replace('+)', ' ')
while '+(' in s:
    s = s.replace('+(', ' ')
while ')+' in s:
    s = s.replace(')+', ' ')
r = []
for x in s.split():
    r.extend(f(x))

rez = []
for x in r:
    try:
        if eval(x) % 2 == 0:
            rez.append([len(x), eval(x), x])
    except SyntaxError:
        continue
    except TypeError:
        continue
st = sorted(rez, reverse=True)
print(*st[:10], sep="\n")