import sys
sys.stdin = open('24.txt')
a = input()

b = ((a.replace('0', '+').replace('1', '*').replace('2', '*').replace('3', '*')
     .replace('4', '*').replace('5', '*')).replace('8', '*').replace('9', '*')
     .replace('6', '*').replace('7', '*').replace('A', '*').replace('B', '*')
     .replace('C', '*').replace('D', '*').replace('E', '*').replace('F', '*').replace('0', '+').replace('1', '*').replace('2', '*').replace('3', '*')
     .replace('4', '*').replace('5', '*')).replace('8', '*').replace('9', '*').replace('6', '*').replace('7', '*').replace('A', '*').replace('B', '*').replace('C', '*').replace('D', '*').replace('E', '*').replace('F', '*')
c = map(len, b.split('*'))
print(max(c))