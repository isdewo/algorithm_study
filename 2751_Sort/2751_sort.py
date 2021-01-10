from sys import stdin
n = int(stdin.readline())
array = [0]*n
for i in range(n):
  array[i] = int(stdin.readline())

array.sort()


for i in range(n):
  print(array[i])