import sys
sys.stdin = open('24.txt')
a = input()

b = a.replace('+', '*').replace('**', '* *').replace('**', '* *')
c = map(len, b.split())
print(max(c))