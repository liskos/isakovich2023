a = [int(x) for x in open('17.txt')]
def f(a):
    return a % 11 == 0 and abs(a) % 10 == 3

c = []
for i in range(len(a) - 2):
    if ((f(a[i]) and f(a[i+1]) and not(f(a[i+2]))) or (f(a[i]) and not(f(a[i+1])) and f(a[i+2])) or (not(f(a[i])) and f(a[i+1]) and f(a[i+2]))):
        c.append(2*(a[i] + a[i+1] + a[i+2]))
print(len(c), min(c))